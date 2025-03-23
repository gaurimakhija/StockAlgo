import { signInWithGoogle } from "../../lib/auth";
import { useAuth } from "../../context/AuthContext";
import { useRouter } from "next/router";
import { useEffect } from "react";

export default function Login() {
    const { user } = useAuth();
    const router = useRouter();

    useEffect(() => {
        if (user) router.push("/dashboard");
    }, [user, router]);

    return (
        <div className="flex flex-col items-center justify-center h-screen">
            <h1 className="text-2xl mb-4">Login</h1>
            <button onClick={signInWithGoogle} className="bg-blue-500 text-white px-4 py-2 rounded">
                Sign in with Google
            </button>
        </div>
    );
}
