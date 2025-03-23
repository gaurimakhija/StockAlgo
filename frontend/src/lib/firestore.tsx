import { collection, addDoc, getDocs } from "firebase/firestore";
import { db } from "./firebaseConfig";

// Add trade
export const addTrade = async (trade: { userId: string; stock: string; price: number; timestamp: Date }) => {
    await addDoc(collection(db, "trades"), trade);
};

// Fetch trades
export const getTrades = async () => {
    const snapshot = await getDocs(collection(db, "trades"));
    return snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
};
