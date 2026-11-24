import { useState, useEffect } from "react";
import type { EventsCardProps } from "../components/EventsCard";


export function useEventsList() {
    const [events, setEvents] = useState<EventsCardProps[]>([]);
    const [isLoading, setIsLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(()=>{
        const loadEvents = async ()=>{
            setIsLoading(true)
            setError(null)

            try{
                const response = await fetch(import.meta.env.VITE_API_URL + "/events")

                if (!response.ok) {
                    throw new Error(`Unable to load events: ${response.status}`)
                }

                const data: { events: EventsCardProps[] } = await response.json()
                setEvents(data.events)
    
            } catch (err){
    
                setError(err instanceof Error ? err.message : "Oh no, something went wrong!")
    
            } finally {

                setIsLoading(false)
            }
        }

        loadEvents()
    }, [])
    return { events, isLoading, error}
}