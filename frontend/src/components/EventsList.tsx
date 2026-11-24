import EventCard from "./EventCard";
import { useEventsList } from "../hooks/useEventsList";


function EventsList() {
    const {events, isLoading, error} = useEventsList()

    if (isLoading) 
        return(<p>Loading Events...</p>);

    if (error) 
        return (<p>Error: {error} </p>);

    if (events.length === 0) 
        return(<p>No events found</p>)

    return(
        <section className="events-section">
            <h2>Upcoming Events</h2>
            <p>Click event title to view more details.</p>
            <ul className="events-list">
                {events.map((event) => (
                    <EventCard
                     key={event.id} {...event} />
                ))}
            </ul>
        </section>
    )
}

export default EventsList
