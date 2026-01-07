import { contextBridge, ipcRenderer } from "electron";
import { pathToFileURL } from "url";

contextBridge.exposeInMainWorld("electronAPI", {
    selectFolder: async (): Promise<string | null> => {
        return await ipcRenderer.invoke("select-folder");
    },

    getBackendUrl: async (): Promise<string> => {
        return await ipcRenderer.invoke("get-backend-url");
    },

    indexFolder: async (folder: string): Promise<any> => {
        const backend = await ipcRenderer.invoke("get-backend-url");
        const res = await fetch(
            `${backend}/index?folder=${encodeURIComponent(folder)}`,
            { method: "POST" }
        );
        return res.json();
    },

    search: async (q: string, limit = 20): Promise<any> => {
        const backend = await ipcRenderer.invoke("get-backend-url");
        console.log(backend);
        const res = await fetch(
            `${backend}/search?q=${encodeURIComponent(q)}&limit=${limit}`
        );
        console.log(res);
        return res.json();
    },

    fileUrl: (filePath: string) => {
        return pathToFileURL(filePath).toString();
    },

    openPath: async (p: string): Promise<any> => {
        return await ipcRenderer.invoke("open-path", p);
    },
});
