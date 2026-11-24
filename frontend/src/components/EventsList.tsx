import { useEffect, useState } from "react";
import EventCard, { type EventCardProps } from "./EventCard";

function EventsList() {
    const [events, setEvents] = useState<EventCardProps[]>([]);
    const [isLoading, setIsLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        async function fetchEvents() {
            try {
                const response = await fetch('http://127.0.0.1:8000/events/');
                
                if (!response.ok) {
                    throw new Error(`Failed to fetch events (Status: ${response.status})`);
                }

                const data = await response.json();
                console.log("API Response:", data.events);
                
                setEvents(data.events);
            } catch (err) {
                setError(err instanceof Error ? err.message : 'Something went wrong');
            } finally {
                setIsLoading(false);
            }
        }

        fetchEvents();
    }, []);

    if (isLoading) {
        return <p>Loading events...</p>;
    }

    if (error) {
        return <p className="error-message">Unable to load events: {error}</p>;
    }

    if (events.length === 0) {
        return <p>No events found.</p>;
    }

    return (
        <section className="events-section">
            <h2>Upcoming Events</h2>
            <ul className="events-list">
                {events.map((event) => (
                    <EventCard key={event.id} {...event} />
                ))}
            </ul>
        </section>
    );
}

export default EventsList;
