# Types of Agentic RAG based on Functions

**RAG agents** can be categorized based on their **function**, offering a spectrum of capabilities ranging from simple to complex, with varying **costs** and **latency**. They can serve purposes like **routing**, **one-shot query planning**, **utilizing tools**, employing **reason + act (ReAct) methodology**, and **orchestrating dynamic planning** and execution.


## Routing Agent

The routing agent employs a Large Language Model (LLM) to determine which downstream RAG pipeline to select. This process constitutes agentic reasoning, wherein the LLM analyzes the input query to make an informed decision about selecting the most suitable RAG pipeline. This represents the fundamental and simple form of agentic reasoning.

![Routing-agent](https://github.com/user-attachments/assets/375cb08c-6201-484b-a61e-3c937ae61399)

An alternative routing involves choosing between summarization and question-answering RAG pipelines. The agent evaluates the input query to decide whether to direct it to the summary query engine or the vector query engine, both configured as tools.


![Routing-agent-1](https://github.com/user-attachments/assets/dc9597ea-7071-4a24-87df-6adca8b2afce)

## One-shot query planning agent

The query planning agent divides a complex query into parallelizable subqueries, each of which can be executed across various RAG pipelines based on different data sources. The responses from these pipelines are then amalgamated into the final response. Basically, in query planning, the initial step involves breaking down the query into subqueries, executing each one across suitable RAG pipelines, and synthesizing the results into a comprehensive response.

![One-shot-query-planning-agent](https://github.com/user-attachments/assets/b4933764-661f-459a-8a40-04ea321d46c3)

## Tool use agent

In a typical RAG, a query is submitted to retrieve the most relevant documents that semantically match the query. However, there are instances where additional data is required from external sources such as an API, an SQL database, or an application with an API interface. This additional data serves as context to enhance the input query before it is processed by the LLM. In such cases, the agent can utilize a RAG too spec.

![Tool-use-agent](https://github.com/user-attachments/assets/b1740d3d-43e1-49d2-8cef-74016ee8c29c)

## ReAct agent
ReAct = Reason + Act with LLMs

Moving to a higher level involves incorporating reasoning and actions that are executed iteratively over a complex query. Essentially, this encompasses a combination of routing, query planning, and tool use into a single entity. A ReAct agent is capable of handling sequential multi-part queries while maintaining state (in memory). The process involves the following steps:

1. Upon receiving a user input query, the agent determines the appropriate tool to utilize, if necessary, and gathers the requisite input for the tool.
2. The tool is invoked with the necessary input, and its output is stored.
3. The agent then receives the tool’s history, including both input and output and, based on this information, determines the subsequent course of action.
4. This process iterates until the agent completes tasks and responds to the user.

![ReAct-agent](https://github.com/user-attachments/assets/8fd1936e-19ce-4e21-ae2a-ae60403e2c9d)

## Dynamic planning & execution agent

ReAct currently stands as the most widely adopted agent; however, there’s a growing necessity to address more intricate user intents. As the deployment of agents in production environments increases, there’s a heightened demand for enhanced reliability, observability, parallelization, control, and separation of concerns. Essentially, there’s a requirement for long-term planning, execution insight, efficiency optimization, and latency reduction.

At a fundamental level, these efforts aim to segregate higher-level planning from short-term execution. The rationale behind such agents involves:

1. Outlining the necessary steps to fulfill an input query plan, essentially creating the entire computational graph or directed acyclic graph (DAG).
2. Determine the tools, if any, required for executing each step in the plan and perform them with the necessary inputs.
   
This necessitates the presence of both a planner and an executor. The planner typically utilizes a large language model (LLM) to craft a step-by-step plan based on the user query. Thereupon, the executor executes each step, identifying the tools needed to accomplish the tasks outlined in the plan. This iterative process continues until the entire plan is executed, resulting in the presentation of the final response.

![Dynamic-planning](https://github.com/user-attachments/assets/64594924-8708-4a6c-981e-25ad14d7afb0)



RAG (Retrieval-Augmented Generation) agents can be categorized by their **function**, offering a spectrum of capabilities ranging from **simple to complex** with varying **costs and latency**. These agents address different challenges and use cases within RAG pipelines, balancing efficiency and sophistication.

Copied from or (because it was well written) -> Resource credit: [LeewayHertz](https://www.leewayhertz.com)  

