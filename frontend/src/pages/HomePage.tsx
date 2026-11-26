import NextEvent from "../components/NextEvent";

function HomePage() {

    return(
        <>
            <h1 className="app-header">NC Plus One</h1>
            <p>
                Welcome to NC Plus One. Browse events, 
                and manage your plans.
            </p>
            <section className="next-event">
                <h2 className="next-event-header">Next Event:</h2>
                {/* Making the assumption that the lowest ID will be 
                the next upcoming event as they're sorted by date and 
                once an event passes, the ID's will reshuffle to fill the gap*/}
                <NextEvent id="1"/>
            </section>

        </>
    )
}

export default HomePage;