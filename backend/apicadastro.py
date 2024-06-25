# main.py
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, constr, EmailStr
import psycopg2
from psycopg2.extras import RealDictCursor
from db import get_connection

app = FastAPI()

class FuncCadastro:
    nome: constr(min_length=1, max_length=100) # type: ignore
    email: EmailStr
    cpf: constr(min_length=11, max_length=11) # type: ignore
    senha: constr(min_length=1, max_length=100) # type: ignore

@app.post("/cadastro/")
def create_funcionario(func: FuncCadastro):
    conn = get_connection()
    cursor = conn.cursor()

    # Verifica se o CPF está permitido
    cursor.execute("SELECT cpf FROM funcinterno WHERE cpf = %s", (func.cpf,))
    cpf_permitido = cursor.fetchone()
    if not cpf_permitido:
        raise HTTPException(status_code=400, detail="CPF não permitido")

    # Insere os dados do funcionário
    try:
        cursor.execute("""
            INSERT INTO funccadastro (nome, email, cpf, senha)
            VALUES (%s, %s, %s, %s)
            RETURNING id
        """, (func.nome, func.email, func.cpf, func.senha))
        func_id = cursor.fetchone()[0]
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Erro ao inserir dados")
    finally:
        cursor.close()
        conn.close()

    return {"id": func_id, "nome": func.nome, "email": func.email, "cpf": func.cpf}

# Endpoint para puxar todos funcionários
# ex: curl -X GET "http://127.0.0.1:8000/funcionarios/"
@app.get("/funcionarios/")
def list_funcionarios():
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    
    try:
        cursor.execute("SELECT * FROM funccadastro")
        funcionarios = cursor.fetchall()
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail="Erro ao buscar dados")
    finally:
        cursor.close()
        conn.close()

    return funcionarios

# Endpoint para puxar um funcionário por ID
# ex: curl -X GET "http://127.0.0.1:8000/funcionario/1"
@app.get("/funcionario/{func_id}")
def get_funcionario(func_id: int):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    
    try:
        cursor.execute("SELECT * FROM funccadastro WHERE id = %s", (func_id,))
        funcionario = cursor.fetchone()
        if not funcionario:
            raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail="Erro ao buscar dados")
    finally:
        cursor.close()
        conn.close()

    return funcionario
