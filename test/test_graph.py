from agent.graph import build_graph

graph = build_graph()

session_id = "test_session_1"

# 🔹 Case 1: Missing info
res1 = graph.invoke(
    {
        "input": "I want scholarship",
        "session_id": session_id
    },
    config={"configurable": {"thread_id": session_id}}
)

print("\n--- CASE 1 ---")
print(res1)


# 🔹 Case 2: Full info
res2 = graph.invoke(
    {
        "input": "I am a CSE student with GPA 3.8 want scholarship in Canada",
        "session_id": session_id
    },
    config={"configurable": {"thread_id": session_id}}
)

print("\n--- CASE 2 ---")
print(res2)


# 🔹 Case 3: Essay request
res3 = graph.invoke(
    {
        "input": "write me an essay",
        "session_id": session_id
    },
    config={"configurable": {"thread_id": session_id}}
)

print("\n--- CASE 3 ---")
print(res3)
