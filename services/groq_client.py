from services.db import get_db_connection
import os
from groq import Groq



def get_groq_client():
    api_key = ""
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")
    return Groq(api_key=api_key)


Prompt = """Eres un asistente virtual inteligente y amable. Tu objetivo es responder las preguntas del usuario basandote en la informacion de los documentos proporcionados.

## Instrucciones:
1. Responde SIEMPRE basandote en el contexto de los documentos cuando sea relevante.
2. Si la informacion no esta en los documentos, dilo honestamente: "No tengo informacion sobre eso en mis documentos."
3. Se conciso pero completo en tus respuestas.
4. Manten un tono profesional y amigable.
5. Si el usuario saluda, responde cordialmente.
6. Responde en el mismo idioma que el usuario.

## Documentos de referencia:
"""


def get_response_from_groq(query):
    client = get_groq_client()
    Prompt_with_context = f"{Prompt}"
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "system", "content": Prompt_with_context}, {"role": "user", "content": query}],
        temperature=0.7,
        max_tokens=1000,
    )
    return response.choices[0].message.content or ""


def get_items():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM items")
        return cursor.fetchall()


def get_item_by_code(code):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM items WHERE code = %s", (code,))
        return cursor.fetchone()