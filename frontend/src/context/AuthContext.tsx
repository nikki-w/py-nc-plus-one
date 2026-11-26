import { createContext, useState, type ReactNode } from "react";


interface AuthContextType {
  token: string | null;
  isAuthenticated: boolean;
  saveToken: (newToken: string) => void;
  logout: () => void;
}

export const AuthContext = createContext<AuthContextType | null>(null);

function AuthProvider({ children }: { children: ReactNode }) {
    const [token, setToken] = useState<string | null>(() => 
    localStorage.getItem("access_token")
    );

    const saveToken = (newToken: string) => {
        localStorage.setItem("access_token", newToken);
        setToken(newToken);
    };

    const logout = () => {
        localStorage.removeItem("access_token")
        setToken(null);
    };

    return(
        <AuthContext.Provider
            value={{
                token,
                isAuthenticated: Boolean(token),
                saveToken,
                logout
            }}
        >
            { children }
        </AuthContext.Provider>
    );
}

export default AuthProvider;