import { Link } from "react-router";

export interface EventCardProps {
    id: number;
    title: string;
    description: string;
    starts_at: string;
    ends_at: string;
    location: string
    address?: string;
    capacity?: string;
    created_at?: string;
    showVenueDetails?: boolean
}

function EventCard({
        id, 
        title, 
        description, 
        starts_at, 
        ends_at, 
        location, 
        address, 
        capacity, 
        created_at, 
        showVenueDetails=false
    }: EventCardProps) {
    const formattedStartsAt = new Date(starts_at).toLocaleString("en-GB", {dateStyle:"full", timeStyle: "medium"})
    const formattedEndsAt = new Date(ends_at).toLocaleString("en-GB", {dateStyle:"full", timeStyle: "medium"})

    const formattedCreatedAt = created_at ? new Date(created_at).toLocaleString("en-GB", {
              dateStyle: "short",
              timeStyle: "long",
          }) : null;

    return (
        <li className="event-card">
            <h2 className="event-title">
                {showVenueDetails ? (`${id}: ${title}`) : (
                    <Link to={`/events/${id}`}>
                        {id}: {title}
                    </Link>
                )}
            </h2>
            <p className="event-description">{description}</p>
            <p className="event-start">Starts: {formattedStartsAt}</p>
            <p className="event-end">Ends: {formattedEndsAt}</p>
            <p className="event-venue">Location: {location}</p>

            {showVenueDetails && (
                <>
                    {address && <p className="event-address">Address: {address}</p>}
                    {capacity !== undefined && (
                        <p className="event-capacity">Capacity: {capacity}</p>
                    )}
                    {formattedCreatedAt && (
                        <p className="event-created">Created: {formattedCreatedAt}</p>
                    )}
                </>
            )}
        </li>
    );
}

export default EventCard;