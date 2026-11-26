import { useNavigate } from "react-router";
import LoginForm, { type LoginDetails } from "../components/LoginForm";
import useLogin from "../hooks/useLogin";

function LoginPage() {
    const { login, isLoading } = useLogin();
    const navigate = useNavigate();

    const handleLogin = async (details: LoginDetails) => {
        const success = await login(details)
        if (success) {
            navigate("/events")
        }
    };

    return (
        <main className="login-page">
            <h1>Log In</h1>
            <LoginForm onSubmit={handleLogin} isLoading={isLoading} />
        </main>
    );
}

export default LoginPage;