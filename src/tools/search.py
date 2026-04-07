from db import get_conn
from embeddings import embed
from vector_store import VectorStore

vs = VectorStore()

def search_memory(agent_id, query, limit=5):
    vector = embed(query)
    ids = vs.search(vector, limit)

    if not ids:
        return []

    conn = get_conn()
    cur = conn.cursor()

    placeholders = ",".join("?" for _ in ids)
    cur.execute(f"""
    SELECT content, role, created_at
    FROM memories
    WHERE embedding_id IN ({placeholders})
      AND agent_id = ?
    """, (*ids, agent_id))

    rows = cur.fetchall()
    conn.close()
    return rows
