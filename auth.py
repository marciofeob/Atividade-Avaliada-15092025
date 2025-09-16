import bcrypt
from db import get_connection

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def create_user(nome, senha, nivel):
    conn = get_connection()
    cur = conn.cursor()
    hashed = hash_password(senha)
    sql = "INSERT INTO usuarios (nome, senha, nivel_acesso) VALUES (%s, %s, %s)"
    cur.execute(sql, (nome, hashed, nivel))
    conn.commit()
    cur.close()
    conn.close()

def login_user(nome, senha):
    conn = get_connection()
    cur = conn.cursor()
    sql = "SELECT idusuario, senha, nivel_acesso FROM usuarios WHERE nome = %s"
    cur.execute(sql, (nome,))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user and check_password(senha, user[1]):
        return {"id": user[0], "nome": nome, "nivel": user[2]}
    return None