from agent.nodes.extract import extract_node

state = {
    "input": "I am a CSE student with GPA 3.7 and want to study in Canada"
}

res = extract_node(state)

print(res)
