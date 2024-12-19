import streamlit as st
from taskflowai import Agent, OpenrouterModels, Task, AmadeusTools, OpenaiModels, WikipediaTools, WebTools, set_verbosity
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

# Custom CSS for better full-width display
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 0rem;
    }
    .element-container {
        width: 100%;
    }
    .stMarkdown {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Validate required API keys
required_keys = [
    "WEATHER_API_KEY",
    "SERPER_API_KEY",
    "AMADEUS_API_KEY",
    "AMADEUS_API_SECRET",
    "GROQ_API_KEY",
    "GEMINI_API_KEY"
]

# Check for missing keys
missing_keys = [key for key in required_keys if not os.getenv(key)]
if missing_keys:
    raise ValueError(f"Missing required API keys: {', '.join(missing_keys)}")

# Define agents
web_research_agent = Agent(
    role="Web Research Agent",
    goal="Research destinations and find relevant images",
    attributes="diligent, thorough, comprehensive, visual-focused",
    llm=OpenaiModels.gpt_3_5_turbo,
    tools=[WebTools.serper_search, WikipediaTools.search_articles, WikipediaTools.search_images]
)

travel_agent = Agent(
    role="Travel Agent",
    goal="Assist travelers with their queries",
    attributes="friendly, hardworking, and detailed in reporting back to users",
    llm=OpenaiModels.gpt_3_5_turbo,
    tools=[AmadeusTools.search_flights, WebTools.get_weather_data]
)

reporter_agent = Agent(
    role="Travel Report Agent",
    goal="Write comprehensive travel reports with visual elements",
    attributes="friendly, hardworking, visual-oriented, and detailed in reporting",
    llm=OpenaiModels.gpt_3_5_turbo
)

def research_destination(destination, interests):
    """Research destination with a focus on including relevant images"""
    instruction = (
        f"Create a comprehensive report about {destination} with the following:\n"
        f"1. Use Wikipedia tools to find and include 2-3 high-quality images of key attractions\n"
        f"2. Each image should be properly formatted in markdown with ![description](image_url)\n"
        f"3. Include a brief caption below each image\n"
        f"4. Research attractions and activities related to: {interests}\n"
        f"5. Organize the report with proper headings and sections\n"
        f"6. Place images naturally throughout the content where relevant\n"
        f"7. Include practical visitor information\n"
        f"Format the entire response in clean markdown"
    )
    return Task.create(
        agent=web_research_agent,
        context=f"User Destination: {destination}\nUser Interests: {interests}",
        instruction=instruction
    )

def research_events(destination, dates, interests):
    instruction = (
        f"Research events in {destination} during {dates} with these requirements:\n"
        f"1. Focus on events matching these interests: {interests}\n"
        f"2. Include images of venues or past events where available\n"
        f"3. Provide practical details like timing, location, and tickets\n"
        f"4. Format all content in clean markdown\n"
        f"5. Include images with proper markdown formatting"
    )
    return Task.create(
        agent=web_research_agent,
        context=f"Destination: {destination}\nDates: {dates}\nInterests: {interests}",
        instruction=instruction
    )

def research_weather(destination, dates):
    return Task.create(
        agent=travel_agent,
        context=f"Destination: {destination}\nDates: {dates}",
        instruction=(
            "Provide detailed weather information including:\n"
            "1. Temperature ranges\n"
            "2. Precipitation chances\n"
            "3. General weather patterns\n"
            "4. Recommended clothing/gear"
        )
    )

def search_flights(current_location, destination, dates):
    return Task.create(
        agent=travel_agent,
        context=f"From: {current_location}\nTo: {destination}\nDates: {dates}",
        instruction="Search for best flight options considering price and convenience"
    )

def write_travel_report(destination_report, events_report, weather_report, flight_report):
    instruction = (
        "Create a comprehensive travel report that:\n"
        "1. Maintains all images from the destination and events reports\n"
        "2. Organizes information in a clear, logical structure\n"
        "3. Keeps all markdown formatting intact\n"
        "4. Ensures images are properly displayed with captions\n"
        "5. Includes all key information from each section"
    )
    return Task.create(
        agent=reporter_agent,
        context=f"Destination Report: {destination_report}\n\n"
               f"Events Report: {events_report}\n\n"
               f"Weather Report: {weather_report}\n\n"
               f"Flight Report: {flight_report}",
        instruction=instruction
    )

def main():
    st.title("✈️ Travel Planning Assistant 🌎")
    st.markdown("---")

    # Input Form Section
    st.markdown("### 📝 Trip Details")
    
    # Create three columns for input fields
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

    # Interests field in full width
    interests = st.text_input(
        "Your Interests",
        help="e.g., museums, food, hiking, architecture",
        placeholder="Enter your interests (optional)"
    )

    # Center the Plan button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        plan_button = st.button("🚀 Plan My Trip", type="primary", use_container_width=True)

    if plan_button:
        if current_location and destination and dates:
            try:
                st.success("🎈 Starting your travel planning journey!")
                st.balloons()

                # Use tabs for different sections of the report
                tab1, tab2, tab3, tab4, tab5 = st.tabs([
                    "📍 Destination",
                    "🎯 Events",
                    "☀️ Weather",
                    "✈️ Flights",
                    "📋 Complete Plan"
                ])

                with tab1:
                    with st.spinner("Researching destination..."):
                        destination_report = research_destination(destination, interests)
                    st.markdown(destination_report)

                with tab2:
                    with st.spinner("Finding events..."):
                        events_report = research_events(destination, dates, interests)
                    st.markdown(events_report)

                with tab3:
                    with st.spinner("Checking weather..."):
                        weather_report = research_weather(destination, dates)
                    st.markdown(weather_report)

                with tab4:
                    with st.spinner("Searching flights..."):
                        flights_report = search_flights(current_location, destination, dates)
                    st.markdown(flights_report)

                with tab5:
                    with st.spinner("Creating final report..."):
                        final_report = write_travel_report(
                            destination_report, events_report, weather_report, flights_report
                        )
                    st.markdown(final_report)
                    
                    # Download button in the complete plan tab
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

    # Footer
    st.markdown("---")
    st.markdown("""
        <p style='text-align: center; color: #666666;'>
            Happy Travels! 🌟 Let us help you plan your perfect trip!
        </p>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()