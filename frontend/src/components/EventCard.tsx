export interface EventCardProps {
    id: number;
    title: string;
    description: string;
    starts_at: string;
    ends_at: string;
    organiser_id: number;
    venue_id: number;
}

function EventCard({id, title, description, starts_at, ends_at, organiser_id, venue_id}: EventCardProps) {
    const formattedStartsAt = new Date(starts_at).toLocaleString("en-GB", {dateStyle:"full", timeStyle: "medium"})
    const formattedEndsAt = new Date(ends_at).toLocaleString("en-GB", {dateStyle:"full", timeStyle: "medium"})
    return(
        <li className="event-card">
            <h2 className="event-title">{ id }: { title }</h2>
            <p className="event-description"> { description }</p>
            <p className="event-start">Starts: { formattedStartsAt }</p>
            <p className="event-end">Ends: { formattedEndsAt }</p>
            <p className="event-venue">Location: { venue_id }</p>
        </li>
    )
}

export default EventCard