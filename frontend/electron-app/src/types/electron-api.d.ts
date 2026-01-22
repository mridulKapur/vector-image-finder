export {};

declare global {
    interface Window {
        electronAPI: {
            selectFolder(): Promise<string | null>;
            getBackendUrl(): Promise<string>;
            indexFolder(folder: string): Promise<any>;
            search(q: string, limit?: number): Promise<any>;
            fileUrl(path: string, size?: number): string;
            openPath(p: string): Promise<any>;
        };
    }
}
