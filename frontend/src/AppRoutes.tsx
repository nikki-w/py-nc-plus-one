import { Route, Routes } from "react-router";
import NavigationBar from "./components/NavigationBar";
import HomePage from "./pages/HomePage";
import EventsPage from "./pages/EventsPage";
import SingleEventPage from "./pages/SingleEventPage";
import LoginPage from "./pages/LoginPage";



function AppRoutes() {
    return(
        <>
            <NavigationBar/>
            <Routes>
                <Route path="/" element={<HomePage/>}/>
                <Route path="/events" element={<EventsPage/>}/>
                <Route path="/events/:id" element={<SingleEventPage/>}/>
                <Route path="/auth/login" element={<LoginPage/>}/>
                {/* <Route path="/events/:id/rsvp" element={<RsvpPage/>} */}
            </Routes>
        </>

    )
}

export default AppRoutes;