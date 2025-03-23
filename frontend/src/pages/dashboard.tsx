import { useAuth } from "../context/AuthContext";
import { useRouter } from "next/router";
import { useEffect } from "react";
import { logout } from "../lib/auth";

export default function Dashboard() {
    const { user } = useAuth();
    const router = useRouter();

    useEffect(() => {
        if (!user) router.push("/auth/login");
    }, [user, router]);

    return (
        <div className="p-4">
            <h1 className="text-2xl">Welcome, {user?.displayName}!</h1>
            <button onClick={logout} className="mt-4 bg-red-500 text-white px-4 py-2 rounded">
                Logout
            </button>
        </div>
    );
}
