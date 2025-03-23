import { getAuth, GoogleAuthProvider, signInWithPopup, signOut } from "firebase/auth";
import { app } from "./firebaseConfig";

const auth = getAuth(app);
const provider = new GoogleAuthProvider();

// Google Sign-In
export const signInWithGoogle = async () => {
    try {
        const result = await signInWithPopup(auth, provider);
        return result.user;
    } catch (error) {
        console.error("Login failed:", error);
    }
};

// Logout
export const logout = async () => {
    try {
        await signOut(auth);
    } catch (error) {
        console.error("Logout failed:", error);
    }
};
