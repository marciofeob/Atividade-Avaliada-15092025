from auth import login_user, create_user
from db import get_connection

def menu():
    print("1. Criar usuário")
    print("2. Login")
    print("0. Sair")

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro válido.")

def app(usuario):
    print(f"\nBem-vindo, {usuario['nome']}! Nível: {usuario['nivel']}")
    while True:
        if usuario['nivel'] in ['Administrador', 'Operador']:
            print("\n1. Inserir venda")
            print("2. Inserir conta a receber")
            print("3. Ver vendas")
            print("4. Ver contas a receber")
        elif usuario['nivel'] == 'Vendedor':
            print("\n3. Ver vendas")
            print("4. Ver contas a receber")

        print("0. Sair")

        op = input("Escolha: ").strip()

        if op not in ['0','1','2','3','4']:
            print("Opção inválida. Tente novamente.")
            continue

        if op == "0":
            break

        conn = get_connection()
        cur = conn.cursor()

        try:
            if op == "1" and usuario['nivel'] in ['Administrador', 'Operador']:
                data = input("Data (YYYY-MM-DD): ").strip()
                valor = input_float("Valor: ")
                cur.execute(
                    "INSERT INTO vendas (data, valor, usuario) VALUES (%s, %s, %s)",
                    (data, valor, usuario['id'])
                )
                conn.commit()
                print("Venda inserida.")

            elif op == "2" and usuario['nivel'] in ['Administrador', 'Operador']:
                idvenda = input_int("ID da Venda: ")
                datavenc = input("Data vencimento (YYYY-MM-DD): ").strip()
                valor = input_float("Valor: ")
                cur.execute(
                    "INSERT INTO contasreceber (idvenda, datavencimento, valor, usuario) VALUES (%s, %s, %s, %s)",
                    (idvenda, datavenc, valor, usuario['id'])
                )
                conn.commit()
                print("Conta a receber inserida.")

            elif op == "3":
                cur.execute("SELECT * FROM vendas")
                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("Nenhuma venda encontrada.")

            elif op == "4":
                cur.execute("SELECT * FROM contasreceber")
                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("Nenhuma conta a receber encontrada.")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        finally:
            cur.close()
            conn.close()

if __name__ == "__main__":
    while True:
        menu()
        op = input("Escolha: ").strip()

        if op == "1":
            nome = input("Nome: ").strip()
            senha = input("Senha: ").strip()
            nivel = input("Nível (Administrador, Operador, Vendedor): ").strip()
            if nivel not in ['Administrador', 'Operador', 'Vendedor']:
                print("Nível inválido. Escolha entre: Administrador, Operador, Vendedor.")
                continue
            create_user(nome, senha, nivel)
            print("Usuário criado.")

        elif op == "2":
            nome = input("Nome: ").strip()
            senha = input("Senha: ").strip()
            usuario = login_user(nome, senha)
            if usuario:
                app(usuario)
            else:
                print("Login inválido.")

        elif op == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")