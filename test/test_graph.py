from agent.graph import build_graph

def test_and_save_graph():
    # Build graph
    graph = build_graph()

    # Get internal graph structure
    graph_structure = graph.get_graph()

    # 🔹 Save as PNG
    png_bytes = graph_structure.draw_mermaid_png()

    with open("langgraph_structure.png", "wb") as f:
        f.write(png_bytes)

    print("✅ Graph image saved as langgraph_structure.png")


if __name__ == "__main__":
    test_and_save_graph()
