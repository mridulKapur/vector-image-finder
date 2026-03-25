import { useCallback, useState } from "react";

export type SearchResult = { path: string; score?: number };

export function useApi() {
    const [loading, setLoading] = useState(false);

    const selectFolder = useCallback(async () => {
        if (window.electronAPI) {
            return await window.electronAPI.selectFolder();
        } else {
            console.error("window.electronAPI is undefined!");
        }
    }, []);

    const indexFolder = useCallback(async (folder: string) => {
        setLoading(true);
        try {
            const res = await window.electronAPI.indexFolder(folder);
            return res;
        } finally {
            setLoading(false);
        }
    }, []);

    const search = useCallback(async (q: string): Promise<SearchResult[]> => {
        setLoading(true);
        try {
            const res = await fetch("http://localhost:8000/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ query: q })
            });
            if (!res.ok) {
                console.error("Search failed", await res.text());
                return [];
            }
            const data = await res.json();
            
            // Map the backend's PointStruct response to the local SearchResult required format
            return data.map((point: any) => ({
                path: point.payload?.url || point.payload?.id || String(point.id),
                score: point.score
            }));
        } catch (e) {
            console.error("Error calling search API", e);
            return [];
        } finally {
            setLoading(false);
        }
    }, []);

    const fileUrl = useCallback((path: string): string => {
        return window.electronAPI.fileUrl(path);
    }, []);

    const openPath = useCallback(async (p: string) => {
        return await window.electronAPI.openPath(p);
    }, []);

    return {
        loading,
        selectFolder,
        indexFolder,
        search,
        fileUrl,
        openPath,
    };
}
