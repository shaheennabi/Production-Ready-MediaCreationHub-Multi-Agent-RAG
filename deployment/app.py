import streamlit as st
from taskflowai import  Task, set_verbosity
import os
import re
from src.agentic.agents.reporter_agent import TravelReportAgent
from src.agentic.agents.travel_agent import TravelAgent
from src.agentic.agents.web_research_agent  import WebResearchAgent
from src.agentic.logger import logging
from src.agentic.exception import CustomException

# Must be the first Streamlit command
st.set_page_config(
    page_title="Travel Planning Assistant",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Set verbosity for debugging purposes
set_verbosity(True)

# Load environment variables

# First, simplify the CSS by removing the white backgrounds and fixing contrast
st.markdown("""
    <style>
    /* Container styling */
    .block-container {
        padding: 1rem;
        max-width: 960px;
        margin: 0 auto;
    }
    
    /* Section styling */
    .section-header {
        margin: 1.5rem 0 1rem;
        padding: 0.5rem;
        background-color: #1e3a8a;
        color: white;
        border-radius: 0.3rem;
    }
    
    /* Content sections */
    .content-section {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid #e5e7eb;
        background-color: #1e293b;
        color: white;
    }
    
    /* Form styling */
    .stTextInput {
        margin-bottom: 0.5rem;
    }
    
    /* Button styling */
    .stButton button {
        margin: 1rem 0;
    }
    
    /* Message styling */
    .stSuccess, .stError, .stWarning {
        padding: 0.75rem;
        border-radius: 0.3rem;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)


# Define agents
reporter_agent = TravelReportAgent.initialize_travel_report_agent()
travel_agent= TravelAgent.initialize_travel_agent()
web_research_agent  = WebResearchAgent.initialize_web_research_agent()

# Then, simplify the image formatting function to preserve markdown
def format_markdown_images(markdown_text):
    """
    Keep markdown image syntax intact and just ensure URLs are properly formatted
    """
    import re
    
    # Only process markdown images without converting to HTML
    img_pattern = r'!\[(.*?)\]\((.*?)\)'
    
    def fix_url(match):
        alt_text, url = match.groups()
        url = url.strip()
        if not url.startswith(('http://', 'https://')):
            url = f"https:{url}" if url.startswith('//') else f"https://{url}"
        return f'![{alt_text}]({url})'
    
    return re.sub(img_pattern, fix_url, markdown_text)
 


def research_destination(destination, interests):
    """Research destination with enhanced image handling"""
    instruction = (
        f"Create a comprehensive report about {destination} with the following:\n"
        f"1. Use Wikipedia tools to find and include 2-3 high-quality images of key attractions\n"
        f"2. Ensure images are full URLs starting with http:// or https://\n"
        f"3. Format images as: ![Description](https://full-image-url)\n"
        f"4. Include a brief caption for each image\n"
        f"5. Research attractions and activities related to: {interests}\n"
        f"6. Organize the report with proper headings and sections\n"
        f"7. Place images naturally throughout the content where relevant\n"
        f"8. Include practical visitor information\n"
        f"Format the entire response in clean markdown"
    )
    try:
        task = Task.create(
            agent=web_research_agent,
            context=f"User Destination: {destination}\nUser Interests: {interests}",
            instruction=instruction
        )
        logging.info("Successfully created destination research task.")
        return task
    except Exception as e:
        logging.info(f"Failed to create destination research task: {str(e)}")
        raise CustomException(f"Error creating destination research task: {str(e)}")


def research_events(destination, dates, interests):
    """Research events with enhanced image handling"""
    instruction = (
        f"Research events in {destination} during {dates} that match these interests: {interests}.\n\n"
        f"For each event, include:\n"
        f"- Event name\n"
        f"- Date and time\n"
        f"- Venue/location\n"
        f"- Ticket information (if applicable)\n"
        f"- A short description of the event\n"
        f"- Format event images as: ![Event Name](https://full-image-url)\n"
        f"- Format images as: ![Description](https://full-image-url)\n"
        f"- Ensure images are full URLs starting with http:// or https://\n"
        f"- Information is accurate and up-to-date\n"
        f"- Place images naturally throughout the content where relevant\n"
        f"- Format the entire response in clean markdown"
    )
    try:
        task = Task.create(
            agent=web_research_agent,
            context=f"Destination: {destination}\nDates: {dates}\nInterests: {interests}",
            instruction=instruction
        )
        logging.info("Successfully created events research task.")
        return task
    except Exception as e:
        logging.info(f"Failed to create events research task: {str(e)}")
        raise CustomException(f"Error creating events research task: {str(e)}")


def research_weather(destination, dates):
    """Research weather information"""
    try:
        task = Task.create(
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
        logging.info("Successfully created weather research task.")
        return task
    except Exception as e:
        logging.info(f"Failed to create weather research task: {str(e)}")
        raise CustomException(f"Error creating weather research task: {str(e)}")


def search_flights(current_location, destination, dates):
    """Search flight options"""
    try:
        task = Task.create(
            agent=travel_agent,
            context=f"Flights from {current_location} to {destination} on {dates}",
            instruction="Find top 3 affordable and convenient flight options and provide concise bullet-point information"
        )
        logging.info("Successfully created flight search task.")
        return task
    except Exception as e:
        logging.info(f"Failed to create flight search task: {str(e)}")
        raise CustomException(f"Error creating flight search task: {str(e)}")


def write_travel_report(destination_report, events_report, weather_report, flight_report):
    """Create final travel report"""
    try:
        task = Task.create(
            agent=reporter_agent,
            context=f"Destination Report: {destination_report}\n\n"
                    f"Events Report: {events_report}\n\n"
                    f"Weather Report: {weather_report}\n\n"
                    f"Flight Report: {flight_report}",
            instruction=(
                "Create a comprehensive travel report that:\n"
                "1. Maintains all images from the destination and events reports\n"
                "2. Organizes information in a clear, logical structure\n"
                "3. Keeps all markdown formatting intact\n"
                "4. Ensures images are properly displayed with captions\n"
                "5. Includes all key information from each section"
            )
        )
        logging.info("Successfully created travel report.")
        return task
    except Exception as e:
        logging.info(f"Failed to create travel report: {str(e)}")
        raise CustomException(f"Error creating travel report: {str(e)}")

def main():
    st.title("✈️ Travel Planning Assistant")
    
    with st.container():
        st.subheader("📝 Trip Details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            current_location = st.text_input(
                "Departure City",
                placeholder="Enter your starting point"
            )
            destination = st.text_input(
                "Destination City",
                placeholder="Enter your destination"
            )
            
        with col2:
            dates = st.text_input(
                "Travel Dates",
                placeholder="Dec 20-25, 2024"
            )
            interests = st.text_input(
                "Your Interests",
                placeholder="museums, food, hiking..."
            )

    plan_button = st.button("🚀 Plan My Trip", type="primary", use_container_width=True)

    if plan_button:
        if current_location and destination and dates:
            try:
                st.success("🎈 Starting your travel planning journey!")
                st.balloons()

                sections = {
                    "destination": ("📍 Destination Information", research_destination),
                    "events": ("🎯 Events & Activities", research_events),
                    "weather": ("☀️ Weather Forecast", research_weather),
                    "flights": ("✈️ Flight Options", search_flights)
                }

                reports = {}

                for key, (title, func) in sections.items():
                    with st.container():
                        st.markdown(f"<div class='section-header'><h3>{title}</h3></div>", 
                                  unsafe_allow_html=True)
                        with st.spinner(f"Loading {title.lower()}..."):
                            if key == "destination":
                                reports[key] = func(destination, interests)
                            elif key == "events":
                                reports[key] = func(destination, dates, interests)
                            elif key == "weather":
                                reports[key] = func(destination, dates)
                            else:  # flights
                                reports[key] = func(current_location, destination, dates)
                            
                            try:
                                formatted_content = format_markdown_images(reports[key])
                                st.markdown(formatted_content)  # Just use regular markdown
                            except Exception as e:
                                st.error(f"Error displaying content: {str(e)}")
                                st.markdown(reports[key])

                st.markdown("<div class='section-header'><h3>📋 Complete Travel Plan</h3></div>", 
                          unsafe_allow_html=True)
                with st.spinner("Creating final report..."):
                    final_report = write_travel_report(
                        reports["destination"],
                        reports["events"],
                        reports["weather"],
                        reports["flights"]
                    )
                    # And for the final report:
                    try:
                        formatted_final_report = format_markdown_images(final_report)
                        st.markdown(formatted_final_report)  # Just use regular markdown
                    except Exception as e:
                        st.error(f"Error displaying final report: {str(e)}")
                        st.markdown(final_report)
                
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
            st.warning("🔔 Please fill in all required fields")

    st.markdown("""
        <p style='text-align: center; color: #666666; margin-top: 2rem;'>
            Happy Travels! 🌟
        </p>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()