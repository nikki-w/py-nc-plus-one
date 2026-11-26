import { useState } from "react";


export interface LoginDetails {
    email: string;
    password: string;
}

interface LoginFormProps {
    onSubmit: (details: LoginDetails) => void;
    // error: string | null;
    isLoading: boolean
}

function LoginForm({ onSubmit, isLoading }: LoginFormProps) {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    return(
        <form 
            className="login-form" 
            onSubmit={(event) => {
                event.preventDefault();
                onSubmit({ email, password })
            }}>
            <div>
                <label htmlFor="email">Email:</label>
                    <input
                        id="email"
                        type="email"
                        value={ email }
                        onChange={(event)=>setEmail(event.target.value)}
                        required/>
            </div>

            <div>
                <label htmlFor="password">Password:</label>
                    <input
                        id="password"
                        type="password"
                        value={ password }
                        onChange={(event)=>setPassword(event.target.value)}
                        required/>
            </div>
            <button 
                type="submit"
                disabled={isLoading}>
                {isLoading ? "Logging in..." : "Log In"}
            </button>
        </form>
    )
}

export default LoginForm;