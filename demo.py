import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Retrieve the API keys from environment variables
#openai_api_key = os.getenv("OPENAI_API_KEY")
weather_api_key = os.getenv("WEATHER_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")
amadeus_api_key = os.getenv("AMADEUS_API_KEY")
amadeus_api_secret = os.getenv("AMADEUS_API_SECRET")
groq_api_key = os.getenv("GROQ_API_KEY")



### imports

from taskflowai import Agent, Task, OpenaiModels,GroqModels, WebTools, AmadeusTools, WikipediaTools, set_verbosity
import streamlit as st

set_verbosity(True)



### Agents
# Define Agents
web_researcher = Agent(
    role="Web Researcher",
    goal="Search the web thoroughly for information and write comprehensive reports",
    llm=GroqModels.llama_3_1_70b,
    tools=[
        WebTools.serper_search, 
        WikipediaTools.search_articles, 
        WikipediaTools.search_images
    ]
)

travel_agent = Agent(
    role="Travel Agent",
    goal="Assist users with their travel-related queries",
    llm=GroqModels.llama_3_1_70b,
    tools=[
        WebTools.serper_search, 
        WebTools.get_weather_data, 
        AmadeusTools.search_flights
    ]
)

reporter_agent = Agent(
    role="Travel Report Agent",
    goal="Write comprehensive travel reports",
    llm=GroqModels.llama_3_1_70b,
)




### Tasks

# Define Tasks
def research_destination_task(destination, interests):
    return Task.create(
        agent=web_researcher,
        context=f"User's Intended Destination: {destination}\n\nUser's Interests: {interests}\n",
        instruction="""
        Research the given destination using Wikipedia and other tools, collecting both articles and images to prepare
        a rich multi-media markdown response about the destination. Include relevant information related to the user's interests.
        """
    )

def research_events_task(destination, interests, dates):
    return Task.create(
        agent=web_researcher,
        context=f"User's Intended Destination: {destination}\n\nUser's Interests: {interests}\n\nUser's Travel Dates: {dates}\n",
        instruction="""
        Use web tools to research events at the given destination within the specified dates. Include events matching
        the user's interests in addition to general events.
        """
    )

def research_weather_task(destination, dates):
    return Task.create(
        agent=travel_agent,
        context=f"User's Intended Destination: {destination}\n\nUser's Travel Dates: {dates}\n",
        instruction="""
        Research and report weather for the given location and date span. If the dates are more than 10 days ahead, use web tools to
        report average weather for that time of year. Provide a detailed weather summary for the destination.
        """
    )

def research_flights_task(location, destination, dates):
    return Task.create(
        agent=travel_agent,
        context=f"User's Current Location: {location}\n\nUser's Intended Destination: {destination}\n\nUser's Travel Dates: {dates}\n",
        instruction="""
        Use flight research tools to find flight options between the given locations and travel dates. Provide a detailed
        report highlighting the best three options.
        """
    )

def write_final_report_task(location, destination, interests, dates, destination_report, events_report, weather_report, flights_report):
    return Task.create(
        agent=reporter_agent,
        context=f"User is traveling from {location} to {destination} around {dates}. Interests: {interests}. \n\n"
               f"Destination Information: {destination_report}\nEvents Report: {events_report}\n"
               f"Weather: {weather_report}\nFlights: {flights_report}\n",
        instruction="""
        Write a comprehensive travel report in markdown format. Include information about the destination, events, weather,
        and flight options in a cohesive and detailed manner, along with relevant images.
        """
    )





## Give it a try

def main():
    # Get user inputs
    location = input("Where are you flying from?\n").strip()
    destination = input("Where are you going?\n").strip()
    interests = input("What are your interests for this trip?\n").strip()
    dates = input("When are you going to travel?\n").strip()

    # Validate inputs
    if not (location and destination and interests and dates):
        print("All inputs are required. Please try again.")
        return

    # Task executions
    destination_report = research_destination_task(destination, interests)
    print("\n--- Destinatioin Report ---\n")

    events_report = research_events_task(destination, interests, dates)
    print("\n--- Events Report ---\n")

    weather_report = research_weather_task(destination, dates)
    print("\n--- Weather Report ---\n")

    flights_report = research_flights_task(location, destination, dates)
    print("\n--- Fights Report ---\n")


    # Compile the final report
    final_report = write_final_report_task(
        location, destination, interests, dates,
        destination_report, events_report, weather_report, flights_report
    )

    # Print the final report
    print("\n--- Final Trip Report ---\n")
    print(final_report)

if __name__ == "__main__":
    main()
