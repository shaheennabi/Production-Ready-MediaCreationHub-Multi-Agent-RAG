# Must be the first Streamlit command
import streamlit as st

st.set_page_config(
    page_title="Travel Planning Assistant",
    layout="wide",
    initial_sidebar_state="collapsed"
)



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