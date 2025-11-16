export {};

declare global {
  interface Window {
    electronAPI: {
      selectFolder(): Promise<string | null>;
      getBackendUrl(): Promise<string>;
      indexFolder(folder: string): Promise<any>;
      search(q: string, limit?: number): Promise<any>;
      thumbnailUrl(path: string, size?: number): Promise<string>;
      openPath(p: string): Promise<any>;
    };
  }
}
