import { NavLink } from "react-router"

function NavigationBar() {
    return(
        <nav>
            <NavLink
            to="/" end
            className={({ isActive }) => (isActive ? "nav-link active" : "nav-link")}>
                Home
            </NavLink>

            <NavLink 
            to="/events" end
            className={({ isActive }) => (isActive ? "nav-link active" : "nav-link")}>
                Events    
            </NavLink>
        </nav>
    );
}

export default NavigationBar;