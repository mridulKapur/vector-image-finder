"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const electron_1 = require("electron");
electron_1.contextBridge.exposeInMainWorld('electronAPI', {
    selectFolder: async () => {
        return await electron_1.ipcRenderer.invoke('select-folder');
    },
    getBackendUrl: async () => {
        return await electron_1.ipcRenderer.invoke('get-backend-url');
    },
    indexFolder: async (folder) => {
        const backend = await electron_1.ipcRenderer.invoke('get-backend-url');
        const res = await fetch(`${backend}/index?folder=${encodeURIComponent(folder)}`, { method: 'POST' });
        return res.json();
    },
    search: async (q, limit = 20) => {
        const backend = await electron_1.ipcRenderer.invoke('get-backend-url');
        const res = await fetch(`${backend}/search?q=${encodeURIComponent(q)}&limit=${limit}`);
        return res.json();
    },
    thumbnailUrl: async (path, size = 256) => {
        const backend = await electron_1.ipcRenderer.invoke('get-backend-url');
        // The renderer can directly use this URL as an <img src=... />
        return `${backend}/thumbnail?path=${encodeURIComponent(path)}&size=${size}`;
    },
    openPath: async (p) => {
        return await electron_1.ipcRenderer.invoke('open-path', p);
    }
});
