# 🌺 🌸 🌿 Production-Ready TripPlanner Multi-AI Agent Project 🍀 🌱 🪴

## System Design or Project Pipeline
### Main Pipeline

![TripPlanner](https://github.com/user-attachments/assets/45f1226e-2e3c-4ae7-999f-9ff0db143bc7)

Let's Start with LLM OpenAI: (GPT-3.5 Turbo):

![Screenshot 2024-12-22 014852](https://github.com/user-attachments/assets/c33b9de0-e125-4ee7-8fff-67dc952dfe0f)

- In this example, I am loading the **GPT-3.5 Turbo** model.  
- This model is efficient, cost-effective, and performs exceptionally well for most tasks.  
- Make sure to load the OpenAI API key properly.  
- It is recommended to store the API key securely using a `.env` file or a similar approach.  


* Web Research Agent
  ![Screenshot 2024-12-22 014625](https://github.com/user-attachments/assets/83e0f923-6e4e-4763-b11d-09980ea09458)



### Deployment Pipeline

![Deployment Pipeline TripPlanner ](https://github.com/user-attachments/assets/2aa5d232-3766-4ac1-b48a-eb055ac1f7e7)


## Guide for Developers 🌿🎇✨💚🎆🌱🎇✨💚🎆 

### Project tree structure

```bash
├── .github/workflows/
│   └── deploy.yml
├── deployment/
│   └── app.py
├── docs/
│   ├── Agentic RAG Pipeline.md
│   └── Types of Agentic RAG.md
├── flowcharts/
│   └── project_pipeline.jpg
├── log/
│   └── timestamp(log)
├── notebooks/
│   └── TripPlanner_Multi_AI_Agent_Experimental.ipynb  
├── src/agentic/
│   ├── agents/
│   │   ├── reporter_agent.py
│   │   ├── travel_agent.py
│   │   └── web_research_agent.py
│   ├── exception/
│   │   └── __init__.py
│   ├── logger/
│   │   └── __init__.py
│   ├── tools/
│   │   ├── get_weather_data.py
│   │   ├── search_articles.py
│   │   ├── search_flights.py
│   │   ├── search_images.py
│   │   └── serper_search.py
│   └── utils/
│       ├── __init__.py
│       └── main_utils.py
├── .gitignore
├── demo.py
├── LICENSE
├── README.md
├── requirements.txt
├── scripts.sh
├── setup.py
└── template.py
```


## 📜 License
This project is licensed under the **MIT License**.  
You are free to use, modify, and share this project, as long as proper credit is given to the original contributors.  
For more details, check the [LICENSE](LICENSE) file. 🏛️

