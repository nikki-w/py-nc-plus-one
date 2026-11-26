import { useState } from "react";
import useAuth from "./useAuth";
import type { LoginDetails } from "../components/LoginForm";

interface LoginResponse {
  access_token: string;
  token_type: string;
}

function useLogin() {
  const [isLoading, setIsLoading] = useState(false);
  const { saveToken } = useAuth();

  const login = async (details: LoginDetails): Promise<boolean> => {
    setIsLoading(true);

    try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}/auth/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(details),
    });

    if (!response.ok) {
        return false;
    }

    const data: LoginResponse = await response.json();
    saveToken(data.access_token)
    return true;
    } catch {
        return false;
    } finally {
        setIsLoading(false);
    }
  };

  return { login, isLoading }

}

export default useLogin;