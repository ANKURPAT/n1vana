from mcp.server import MCPServer
from db import init_db, get_conn
from tools.write import write_memory
from tools.search import search_memory
from config import DEFAULT_AGENT_ID
import uuid

init_db()
server = MCPServer("n1vana")

def ensure_agent(agent_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT OR IGNORE INTO agents (id, name) VALUES (?, ?)",
        (agent_id, agent_id)
    )
    conn.commit()
    conn.close()

def ensure_session(agent_id, session_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT OR IGNORE INTO sessions (id, agent_id) VALUES (?, ?)",
        (session_id, agent_id)
    )
    conn.commit()
    conn.close()

@server.tool()
def n1vana_write(agent_id: str = DEFAULT_AGENT_ID,
                 session_id: str = None,
                 role: str = "user",
                 content: str = "") -> str:
    if not session_id:
        session_id = str(uuid.uuid4())

    ensure_agent(agent_id)
    ensure_session(agent_id, session_id)
    return write_memory(agent_id, session_id, role, content)

@server.tool()
def n1vana_search(agent_id: str = DEFAULT_AGENT_ID,
                  query: str = "",
                  limit: int = 5):
    ensure_agent(agent_id)
    return search_memory(agent_id, query, limit)

if __name__ == "__main__":
    server.run()
