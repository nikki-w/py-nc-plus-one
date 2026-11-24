import { useState, useEffect } from "react";
import type { EventCardProps } from "../components/EventCard";

export function useEvent(id: string | undefined) {
    const [event, setEvent] = useState<EventCardProps | null>(null);
    const [isLoading, setIsLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(()=>{
        if (!id) return;

        const loadEvent = async () => {
            setIsLoading(true)
            setError(null)

            try{
                const response = await fetch(`${ import.meta.env.VITE_API_URL }/events/${ id }`)

                if (!response.ok) {
                    throw new Error(`Unable to load event: ${response.status}`)
                }

                const data: { event: EventCardProps } = await response.json()
                setEvent(data.event)
    
            } catch (err){
    
                setError(err instanceof Error ? err.message : "Oh no, something went wrong!")
    
            } finally {

                setIsLoading(false)
            }
        }

        loadEvent()
    }, [id])
    return { event, isLoading, error};
}
