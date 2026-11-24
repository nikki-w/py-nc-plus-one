export interface EventCardProps {
    id: number;
    title: string;
    description: string;
    starts_at: string;
    ends_at: string;
    location: string;
    address: string;
    capacity: string;
    created_at: string;
}

function EventCard({id, title, description, starts_at, ends_at, location, address, capacity, created_at}: EventCardProps) {
    const formattedStartsAt = new Date(starts_at).toLocaleString("en-GB", {dateStyle:"full", timeStyle: "medium"})
    const formattedEndsAt = new Date(ends_at).toLocaleString("en-GB", {dateStyle:"full", timeStyle: "medium"})
    const formattedCreatedsAt = new Date(created_at).toLocaleString("en-GB", {dateStyle:"short", timeStyle: "long"})

    return(
        <li className="event-card">
            <h2 className="event-title">{ id }: { title }</h2>
            <p className="event-description"> { description }</p>
            <p className="event-start">Starts: { formattedStartsAt }</p>
            <p className="event-end">Ends: { formattedEndsAt }</p>
            <p className="event-venue">Location: { location }</p>
            <p className="event-address">Address: { address }</p>
            <p className="event-capacity">Capacity: { capacity }</p>
            <p className="event-created">Created at: { formattedCreatedsAt }</p>
        </li>
    )
}

export default EventCard