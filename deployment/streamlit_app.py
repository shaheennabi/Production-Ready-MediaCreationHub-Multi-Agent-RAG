# Streamlit UI
def main():
    st.title("TripPlanner Multi-AI Agent")

    with st.form("trip_form"):
        location = st.text_input("Where are you flying from?")
        destination = st.text_input("Where are you going?")
        interests = st.text_area("What are your interests for this trip?")
        dates = st.text_input("When are you traveling?")
        submit = st.form_submit_button("Generate Travel Plan")

    if submit:
        st.info("Generating reports, please wait...")

        # Execute tasks
        destination_report = research_destination_task(destination, interests).run()
        events_report = research_events_task(destination, interests, dates).run()
        weather_report = research_weather_task(destination, dates).run()
        flights_report = research_flights_task(location, destination, dates).run()
        final_report = write_final_report_task(location, destination, interests, dates, destination_report, events_report, weather_report, flights_report).run()

        # Display results
        st.markdown("### Final Travel Report")
        st.markdown(final_report)

if __name__ == "__main__":
    main()