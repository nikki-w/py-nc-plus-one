import { useParams } from "react-router";
import { useEvent } from "../hooks/useEvent";
import EventCard from "./EventCard";


function EventDetails() {
    const { id } = useParams()
    const {event, isLoading, error} = useEvent(id)

    if (isLoading) 
        return(<p>Loading Events...</p>);

    if (error) 
        return (<p role="alert">Error: {error} </p>);

    if (!event) 
        return(<p>No events found</p>)

    return(
        <section className="event-section">
            <EventCard {...event} showVenueDetails/>

        </section>
    )
}

export default EventDetails;