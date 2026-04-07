import uuid
from db import get_conn
from embeddings import embed
from vector_store import VectorStore

vs = VectorStore()

def write_memory(agent_id, session_id, role, content):
    conn = get_conn()
    cur = conn.cursor()

    memory_id = str(uuid.uuid4())
    vector = embed(content)
    embedding_id = vs.add(vector)

    cur.execute("""
    INSERT INTO memories (id, agent_id, session_id, role, content, embedding_id)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (memory_id, agent_id, session_id, role, content, embedding_id))

    conn.commit()
    conn.close()
    return memory_id
