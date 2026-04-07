# n1vana

**n1vana** is a minimal, local-first MCP memory server for AI agents.

It provides persistent memory using SQLite and FAISS, exposed via MCP tools so agents can store and recall relevant past context efficiently.

---

## Features

- ✅ MCP-native tools
- ✅ Local-only (no cloud dependencies)
- ✅ Persistent storage (SQLite)
- ✅ Semantic memory recall (FAISS)
- ✅ Agent + session scoped memory
- ✅ Simple, hackable architecture
- ✅ Open-source friendly

---

## MCP Tools

### `n1vana.write`

Stores a memory entry.

**Input**
```json
{
  "agent_id": "default",
  "session_id": "optional",
  "role": "user | assistant | system",
  "content": "text to store"
}
```
### `n1vana.search`
Retrieves relevant past memories.
**Input**
```json
{  "agent_id": "default",  "query": "search text",  "limit": 5}
```

### Setup
1. Install dependencies
`pip install mcp faiss-cpu numpy sqlite-utils`
2. Run the server
```sh
mkdir -p data
python src/server.py
```

### License
MIT
