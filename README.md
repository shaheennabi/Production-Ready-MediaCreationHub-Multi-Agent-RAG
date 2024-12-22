# 🌺 🌸 🌿 Production-Ready TripPlanner Multi-AI Agent Project 🍀 🌱 🪴

## System Design or Project Pipeline
### Main Pipeline

![TripPlanner](https://github.com/user-attachments/assets/45f1226e-2e3c-4ae7-999f-9ff0db143bc7)

### Let's Start with LLM OpenAI: (GPT-3.5 Turbo):

![Screenshot 2024-12-22 014852](https://github.com/user-attachments/assets/c33b9de0-e125-4ee7-8fff-67dc952dfe0f)

- In this example, I am loading the **GPT-3.5 Turbo** model from **taskflowai.OpenaiModels**.  
- This model is efficient, cost-effective, and performs exceptionally well for most tasks.  
- Make sure to load the OpenAI API key properly.  
- It is recommended to store the API key securely using a `.env` file or a similar approach.  

### Now let's task about the Agents:
Web Research Agent: 

  ![Screenshot 2024-12-22 014625](https://github.com/user-attachments/assets/83e0f923-6e4e-4763-b11d-09980ea09458)

- Here, I define the **Web Research Agent**, which is responsible for conducting web-based research and retrieving relevant information.  
- I assign the role of "Web Research Agent" to the agent, ensuring it focuses on researching destinations and finding related images.  
- The **goal** is set to perform thorough and comprehensive research with a visual focus.  
- I specify **attributes** like diligence, thoroughness, and visual-focus to guide the agent's behavior during tasks.  
- I load the OpenAI model using `LoadModel.load_openai_model()` to empower the agent with natural language processing capabilities.  
- I include tools like:
  - **SerperSearch**: For detailed web searches.  
  - **WikiArticles**: To fetch related articles for context.  
  - **WikiImages**: To search and retrieve relevant images.
 
Travel Agent:

![Screenshot 2024-12-22 014556](https://github.com/user-attachments/assets/2d985f64-b996-45a1-9114-534d8969f110)

- Here, I define the **Travel Agent**, which is designed to assist travelers with their queries, focusing on searching for flights and retrieving weather data.  
- The **role** assigned to the agent is "Travel Agent," ensuring its primary function is to help travelers.  
- The **goal** is set to assist travelers by providing relevant information such as flight details and weather conditions.  
- I specify **attributes** like friendliness, hard work, and attention to detail to ensure the agent delivers thorough and useful responses.  
- I load the OpenAI model using `LoadModel.load_openai_model()` to provide natural language processing capabilities.  
- I include tools like:
  - **SearchFlights**: A tool for searching and retrieving flight information using the Amadeus API.  
  - **GetWeatherData**: A tool for fetching real-time weather data from weather.com API.  

Reporter Agent:  

![Screenshot 2024-12-22 014515](https://github.com/user-attachments/assets/6928996a-69c2-49f2-af66-911be403e60f)

- Here, I define the **Travel Report Agent**, which aggregates data from various agents like the Web Search Agent and Travel Agent to generate comprehensive and summarized travel reports.  
- The **role** assigned to the agent is "Travel Report Agent," ensuring its focus on collecting and synthesizing travel-related information.  
- The **goal** is to write detailed, visual-oriented, and comprehensive travel reports based on inputs from other agents, covering destination details, dates, weather reports, flight information, and events at the location.  
- I specify **attributes** like friendliness, hard work, visual focus, and attention to detail to ensure the agent delivers well-structured, insightful, and informative reports.  
- I load the OpenAI model using `LoadModel.load_openai_model()` to provide natural language processing and text generation capabilities.  
- The agent relies on tools and data from other agents, such as:
  - **Web Search Agent**: Provides destination details and event-related information.  
  - **Travel Agent**: Supplies weather reports and flight information.  

### Now let's talk about Tools

Wiki Image Search Tool:

![Screenshot 2024-12-22 021339](https://github.com/user-attachments/assets/d3e1323f-fb04-47a2-a588-bb4a2ac7f589)

- Here, I define the **WikiImages tool**, which is responsible for searching images from Wikipedia using **TaskflowAI's WikipediaTools**.  
- The **goal** of the tool is to fetch relevant images based on specific queries or topics.  
- It leverages **WikipediaTools** from TaskflowAI to access and retrieve image data from Wikipedia.  

Wiki Article Search Tool: 

![Screenshot 2024-12-22 021756](https://github.com/user-attachments/assets/e36413f9-799f-41e0-b513-09fec0a69f9a)

- Here, I define the **WikiArticles tool**, which is responsible for fetching articles from Wikipedia using **TaskflowAI's WikipediaTools**.  
- The **goal** of the tool is to retrieve relevant articles based on specific queries or topics.  
- It utilizes **WikipediaTools** from TaskflowAI to access and fetch article data from Wikipedia.  

Serper Search Tool:

![Screenshot 2024-12-22 021920](https://github.com/user-attachments/assets/2152df64-700d-428f-a86e-597091f7af79)

- Here, I define the **SerperSearch tool**, which is responsible for performing web searches using **TaskflowAI's WebTools**.  
- The **goal** of the tool is to retrieve search results from the web based on specific queries or topics.  
- It leverages **WebTools** from TaskflowAI to perform search operations using the SerperSearch API.  

Weather Fetching Tool:

![Screenshot 2024-12-22 022133](https://github.com/user-attachments/assets/f573e7f3-abf5-4ace-9c81-c0d0abb28be4)

- Here, I define the **GetWeatherData tool**, which is responsible for fetching weather data using **TaskflowAI's WebTools** and the **Weather.com API**.  
- The **goal** of the tool is to retrieve weather-related information based on location or other relevant queries.  
- It utilizes **WebTools** from TaskflowAI to interact with the Weather.com API and fetch weather data.  

Search Fligts Tool: 

![Screenshot 2024-12-22 022445](https://github.com/user-attachments/assets/39e79100-0d2d-46db-a877-935fc0ce67f3)

- Here, I define the **SearchFlights tool**, which is responsible for searching flights using **TaskflowAI's AmadeusTools** and the **Amadeus API**.  
- The **goal** of the tool is to retrieve flight information based on specific queries such as origin, destination, dates, and other relevant parameters.  
- It leverages **AmadeusTools** from TaskflowAI to interact with the Amadeus API for flight searches.  

### Ok, so now let's talk the `app.py` where everything is bought together (see how tasks are defined, to later engage with UI)

Research Destination Task (streamlit UI):

![Screenshot 2024-12-22 023831](https://github.com/user-attachments/assets/c3a36834-c2d6-49c5-bf30-214399da5f67)

- In this code snippet, I import the necessary modules from TaskflowAI, including **Task**, **set_verbosity**, and **Web Research Agent** from `src.agentic.agents.web_research_agent`.
- The `research_destination` function takes a **destination** and **interests** as input to gather detailed information about the destination.
- The function utilizes the **WebResearchAgent**, which combines tools like **WikipediaTools** (for article and image searches) and **SerperSearch** (for web searches) to extract relevant data.
- The `Task.create` method invokes the **WebResearchAgent** to fetch high-quality images, attraction details, and relevant activities based on user interests.
- The research output is formatted in clean markdown, ensuring well-structured and informative reports.


Research Events Task (streamlit UI):

<img width="753" alt="Research Events task" src="https://github.com/user-attachments/assets/a39322b5-0473-4e9c-92ea-9ce70874f336" />

- The `research_events` function utilizes the **WebResearchAgent** imported from `src.agentic.agents.web_research_agent`.
- The **WebResearchAgent** employs tools like **WikipediaTools** (for image searches) and **SerperSearch** (for web search) to collect event-related data.
- The function generates a detailed report about events in a specified **destination** during given **dates**, based on provided **interests**. 
- The instruction includes:
  - Event name, date, time, venue/location, ticket information, and a short description.
  - Images formatted as `![Event Name](https://full-image-url)` or `![Description](https://full-image-url)`.
  - Ensuring URLs are complete and starting with `http://` or `https://`.
  - Formatting the entire response in clean markdown with images placed naturally within the content.


Research Weather (streamlit UI):

<img width="699" alt="Research Weather Task" src="https://github.com/user-attachments/assets/328577fe-57fc-4394-98c9-ffc2871d9258" />

- The `research_weather` function uses the **TravelAgent** imported from `src.agentic.agents.travel_agent`. 
- The **TravelAgent** employs tools like **GetWeatherData**, which fetches weather information using the Weather.com API.
- The function generates a weather report for a specific **destination** and **dates**. 
- The instruction includes:
  - Temperature ranges.
  - Precipitation chances.
  - General weather patterns.
  - Recommendations for clothing and gear.

Search Flights Task (streamlit UI):

<img width="790" alt="Search Flights task" src="https://github.com/user-attachments/assets/002b296b-fa9b-4fc3-bdfc-b0085f63e0f8" />

- The `search_flights` function uses the **TravelAgent**, imported from `src.agentic.agents.travel_agent`.
- The **TravelAgent** utilizes tools like **SearchFlights**, which leverages the Amadeus API to search for flight options.
- The function identifies flights from a **current location** to a **destination** on specific **dates**.
- The instruction specifies:
  - Finding the top 3 affordable and convenient flight options.
  - Providing concise bullet-point details for each option.

Write Travel Report Task (streamlit UI):

<img width="730" alt="Write  travel report task " src="https://github.com/user-attachments/assets/ee1c64cb-78b4-42e4-86fb-95be412e996c" />

- The `write_travel_report` function uses the **ReporterAgent**, imported from `src.agentic.agents.reporter_agent`.
- The **ReporterAgent** combines multiple reports (destination, events, weather, and flight reports) into a single comprehensive travel report.
- The instruction for creating the travel report includes:
  - Retaining all images from the destination and events reports.
  - Organizing information with a clear and logical structure.
  - Preserving all markdown formatting.
  - Ensuring images are properly displayed with captions.
  - Incorporating all essential information from each individual report section.


### Have a Look (How it Appears via UI While Running the `Main Pipeline`)

<img width="958" alt="1" src="https://github.com/user-attachments/assets/ff149519-e5fd-4271-abf0-d5eb9d8fca82" />
<img width="956" alt="2" src="https://github.com/user-attachments/assets/5e13255a-16c7-4510-bdf3-d0385c176034" />
<img width="959" alt="3" src="https://github.com/user-attachments/assets/563c21d2-f15a-4402-9f6c-fea788ad5090" />
<img width="959" alt="4" src="https://github.com/user-attachments/assets/4e5a60dc-c40c-4740-82b8-5d4ff6dc908f" />
<img width="958" alt="5" src="https://github.com/user-attachments/assets/01845f17-4dee-4ebb-bc2f-2bb90bbc7f20" />
<img width="959" alt="6" src="https://github.com/user-attachments/assets/ed802136-072a-4b0b-b705-2d2bd00d7be6" />
<img width="959" alt="7" src="https://github.com/user-attachments/assets/eb1799c5-bbe2-43ce-a1c3-13db53d6af69" />
<img width="959" alt="8" src="https://github.com/user-attachments/assets/26e91312-4b7a-49ef-92df-be60069aea20" />
<img width="959" alt="9" src="https://github.com/user-attachments/assets/72b54321-bc6f-418f-95b3-c980fd05e1fd" />
<img width="954" alt="10" src="https://github.com/user-attachments/assets/52c7f0e3-57a9-4f60-a04c-d97a0e41c15e" />
<img width="958" alt="11" src="https://github.com/user-attachments/assets/8e7bda45-96e8-426d-a558-6af7ab082346" />
<img width="947" alt="12" src="https://github.com/user-attachments/assets/6fc5a251-b140-4e8f-acf4-84dd6e4dbc1e" />
<img width="959" alt="13" src="https://github.com/user-attachments/assets/60c05b81-a9db-45d4-8635-a9c49e646d91" />
<img width="959" alt="14" src="https://github.com/user-attachments/assets/ca81265a-19eb-4a51-8fb5-4af9e5441e1a" />
<img width="957" alt="15" src="https://github.com/user-attachments/assets/e7411c35-41eb-4a22-8998-e23d1e9e95e1" />
<img width="958" alt="16" src="https://github.com/user-attachments/assets/e6d5bce8-b33e-4681-9bae-ea51d11b4f1d" />
<img width="957" alt="17" src="https://github.com/user-attachments/assets/92fa0f85-de82-467e-b8fa-fe252b89c80f" />
<img width="956" alt="18" src="https://github.com/user-attachments/assets/29a63694-5913-40df-8f55-7c99a61f228c" />
<img width="958" alt="19" src="https://github.com/user-attachments/assets/e7adf831-760e-4486-9b2c-74f9f6d6fee3" />
<img width="956" alt="21" src="https://github.com/user-attachments/assets/06043e1d-16ce-44c7-ba68-56d14c35f1ec" />
<img width="959" alt="22" src="https://github.com/user-attachments/assets/fba03c7f-aef3-4f35-96c3-eb64af957ac0" />
<img width="957" alt="23" src="https://github.com/user-attachments/assets/9d4f1e02-8dad-40c8-b946-3fceac5f1158" />
<img width="959" alt="24" src="https://github.com/user-attachments/assets/1c121042-2468-490c-b241-5bad92ed006c" />
<img width="956" alt="25" src="https://github.com/user-attachments/assets/02502c0e-a714-4515-8558-c906d8cdd747" />
<img width="959" alt="26" src="https://github.com/user-attachments/assets/e7312a43-7e5b-4824-ac48-c4ad164e6c77" />
<img width="959" alt="27" src="https://github.com/user-attachments/assets/dfe4c8e3-e70a-410c-bf7d-5054d4a1412b" />
<img width="956" alt="28" src="https://github.com/user-attachments/assets/2a1a099c-b011-45de-9729-61c6b62b6382" />

* end to `main pipeline`

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

