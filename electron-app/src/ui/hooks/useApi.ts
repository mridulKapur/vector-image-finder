import { useCallback, useState } from "react";

type SearchResult = { path: string; score?: number };

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
            const res = await window.electronAPI.search(q);
            // backend returns { results: [{path, score}] }
            return res?.results || [];
        } finally {
            setLoading(false);
        }
    }, []);

    const thumbnailUrl = useCallback(async (path: string, size = 256) => {
        return await window.electronAPI.thumbnailUrl(path, size);
    }, []);

    const openPath = useCallback(async (p: string) => {
        return await window.electronAPI.openPath(p);
    }, []);

    return {
        loading,
        selectFolder,
        indexFolder,
        search,
        thumbnailUrl,
        openPath,
    };
}
