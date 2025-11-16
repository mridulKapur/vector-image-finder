import { contextBridge, ipcRenderer } from 'electron';

contextBridge.exposeInMainWorld('electronAPI', {
  selectFolder: async (): Promise<string | null> => {
    return await ipcRenderer.invoke('select-folder');
  },

  getBackendUrl: async (): Promise<string> => {
    return await ipcRenderer.invoke('get-backend-url');
  },

  indexFolder: async (folder: string): Promise<any> => {
    const backend = await ipcRenderer.invoke('get-backend-url');
    const res = await fetch(`${backend}/index?folder=${encodeURIComponent(folder)}`, { method: 'POST' });
    return res.json();
  },

  search: async (q: string, limit = 20): Promise<any> => {
    const backend = await ipcRenderer.invoke('get-backend-url');
    const res = await fetch(`${backend}/search?q=${encodeURIComponent(q)}&limit=${limit}`);
    return res.json();
  },

  thumbnailUrl: async (path: string, size = 256): Promise<string> => {
    const backend = await ipcRenderer.invoke('get-backend-url');
    // The renderer can directly use this URL as an <img src=... />
    return `${backend}/thumbnail?path=${encodeURIComponent(path)}&size=${size}`;
  },

  openPath: async (p: string): Promise<any> => {
    return await ipcRenderer.invoke('open-path', p);
  }
});
