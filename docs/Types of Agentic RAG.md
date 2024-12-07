# Types of Agentic RAG based on Functions

**RAG agents** can be categorized based on their **function**, offering a spectrum of capabilities ranging from simple to complex, with varying **costs** and **latency**. They can serve purposes like **routing**, **one-shot query planning**, **utilizing tools**, employing **reason + act (ReAct) methodology**, and **orchestrating dynamic planning** and execution.


## Routing Agent

The routing agent employs a Large Language Model (LLM) to determine which downstream RAG pipeline to select. This process constitutes agentic reasoning, wherein the LLM analyzes the input query to make an informed decision about selecting the most suitable RAG pipeline. This represents the fundamental and simple form of agentic reasoning.

![Routing-agent](https://github.com/user-attachments/assets/375cb08c-6201-484b-a61e-3c937ae61399)

