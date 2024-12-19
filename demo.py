import streamlit as st
from taskflowai import Agent, OpenrouterModels, Task, AmadeusTools, OpenaiModels, WikipediaTools, GroqModels, WebTools, set_verbosity
import os

# Must be the first Streamlit command
st.set_page_config(
    page_title="Travel Planning Assistant",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Set verbosity for debugging purposes
set_verbosity(True)

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# API Keys
weather_api_key = os.getenv("WEATHER_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")
amadeus_api_key = os.getenv("AMADEUS_API_KEY")
amadeus_api_secret = os.getenv("AMADEUS_API_SECRET")
groq_api_key = os.getenv("GROQ_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Define agents with reduced output tokens
web_research_agent = Agent(
    role="Web Research Agent",
    goal="Research destinations and find relevant images",
    attributes="diligent, thorough",
    llm=OpenaiModels.gpt_3_5_turbo,
    tools=[WebTools.serper_search, WikipediaTools.search_articles, WikipediaTools.search_images],
    max_tokens=2000  # Limit output tokens
)

travel_agent = Agent(
    role="Travel Agent",
    goal="Assist with travel queries",
    attributes="detailed, efficient",
    llm=OpenaiModels.gpt_3_5_turbo,
    tools=[AmadeusTools.search_flights, WebTools.get_weather_data],
    max_tokens=1000  # Limit output tokens
)

reporter_agent = Agent(
    role="Travel Report Agent",
    goal="Write travel reports",
    attributes="concise, organized",
    llm=OpenaiModels.gpt_3_5_turbo,
    max_tokens=2000  # Limit output tokens
)

def research_destination(destination, interests):
    """Research destination with a focus on including relevant images"""
    instruction = (
        f"Create a concise report about {destination} focusing on {interests}. Include:\n"
        f"1. Brief overview (2-3 sentences)\n"
        f"2. Top 3 attractions related to user interests\n"
        f"3. Key practical information\n"
        "Keep the response under 1000 words."
    )
    
    # First get the basic information
    basic_info = Task.create(
        agent=web_research_agent,
        context=f"User Destination: {destination}\nUser Interests: {interests}",
        instruction=instruction
    )
    
    # Separately fetch images
    image_instruction = f"Find 2 high-quality images of main attractions in {destination}"
    images = Task.create(
        agent=web_research_agent,
        context=f"Destination: {destination}",
        instruction=image_instruction,
        tools=[WikipediaTools.search_images]
    )
    
    # Combine the results
    return f"{basic_info}\n\n{images}"

def research_events(destination, dates, interests):
    instruction = (
        f"Find top 3 relevant events in {destination} during {dates} "
        f"related to: {interests}. Keep response brief and focused."
    )
    return Task.create(
        agent=web_research_agent,
        context=f"Destination: {destination}",
        instruction=instruction
    )

def research_weather(destination, dates):
    instruction = f"Provide a brief weather summary for {destination} during {dates}."
    return Task.create(
        agent=travel_agent,
        context=f"Destination: {destination}",
        instruction=instruction
    )

def search_flights(current_location, destination, dates):
    instruction = (
        f"Find top 3 flight options from {current_location} to {destination} "
        f"during {dates}. Focus on best value options."
    )
    return Task.create(
        agent=travel_agent,
        context=f"Flight search",
        instruction=instruction
    )

def write_travel_report(destination_report, events_report, weather_report, flight_report):
    instruction = (
        "Create a concise travel report combining the key information. "
        "Format with clear headers and keep sections brief."
    )
    return Task.create(
        agent=reporter_agent,
        context="Final report compilation",
        instruction=instruction,
        input_data={
            "destination": destination_report,
            "events": events_report,
            "weather": weather_report,
            "flights": flight_report
        }
    )

def main():
    st.title("✈️ Travel Planning Assistant 🌎")
    st.markdown("---")

    # Input Form Section
    st.markdown("### 📝 Trip Details")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        current_location = st.text_input(
            "Departure City",
            help="Enter city name (e.g., New York, London)",
            placeholder="Enter your starting point"
        )
        
    with col2:
        destination = st.text_input(
            "Destination City",
            help="Enter destination city (e.g., Paris, Tokyo)",
            placeholder="Enter your destination"
        )
        
    with col3:
        dates = st.text_input(
            "Travel Dates",
            help="Format: Dec 20-25, 2024",
            placeholder="Enter your travel dates"
        )

    interests = st.text_input(
        "Your Interests",
        help="e.g., museums, food, hiking, architecture",
        placeholder="Enter your interests (optional)"
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        plan_button = st.button("🚀 Plan My Trip", type="primary", use_container_width=True)

    if plan_button:
        if current_location and destination and dates:
            try:
                st.success("🎈 Starting your travel planning journey!")
                st.balloons()

                # Create expanders instead of tabs for better content management
                with st.expander("📍 Destination Information", expanded=True):
                    with st.spinner("Researching destination..."):
                        destination_report = research_destination(destination, interests)
                    st.markdown(destination_report, unsafe_allow_html=True)

                with st.expander("🎯 Events", expanded=True):
                    with st.spinner("Finding events..."):
                        events_report = research_events(destination, dates, interests)
                    st.markdown(events_report)

                with st.expander("☀️ Weather", expanded=True):
                    with st.spinner("Checking weather..."):
                        weather_report = research_weather(destination, dates)
                    st.markdown(weather_report)

                with st.expander("✈️ Flights", expanded=True):
                    with st.spinner("Searching flights..."):
                        flights_report = search_flights(current_location, destination, dates)
                    st.markdown(flights_report)

                with st.expander("📋 Complete Plan", expanded=True):
                    with st.spinner("Creating final report..."):
                        final_report = write_travel_report(
                            destination_report, events_report, weather_report, flights_report
                        )
                    st.markdown(final_report, unsafe_allow_html=True)
                    
                    st.download_button(
                        label="📥 Download Complete Travel Plan",
                        data=final_report,
                        file_name=f"travel_plan_{destination.lower().replace(' ', '_')}.md",
                        mime="text/markdown",
                        use_container_width=True
                    )

            except Exception as e:
                st.error(f"🚨 An error occurred: {str(e)}")
                print(f"Debug - Error details: {str(e)}")
        else:
            st.warning("🔔 Please fill in all required fields (departure city, destination, and dates)")

    st.markdown("---")
    st.markdown("""
        <p style='text-align: center; color: #666666;'>
            Happy Travels! 🌟 Let us help you plan your perfect trip!
        </p>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()