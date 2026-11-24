import { Route, Routes } from "react-router";
import NavigationBar from "./components/NavigationBar";
import HomePage from "./pages/HomePage";
import EventsPage from "./pages/EventsPage";
import SingleEventPage from "./pages/SingleEventPage";



function AppRoutes() {
    return(
        <>
            <NavigationBar/>
            <Routes>
                <Route path="/" element={<HomePage/>}/>
                <Route path="/events" element={<EventsPage/>}/>
                <Route path="/events/:id" element={<SingleEventPage/>}/>
            </Routes>
        </>

    )
}

export default AppRoutes;