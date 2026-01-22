// electron-app/src/electron/main.ts
import { app, BrowserWindow, ipcMain, dialog, shell } from "electron";
import path from "path";
import isDev from "electron-is-dev";
import dotenv from "dotenv";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

dotenv.config({ path: path.join(__dirname, "..", "..", ".env") });
const BACKEND_URL = process.env.BACKEND_URL || "http://localhost:8000";
console.log("BACKEND_URL:", BACKEND_URL);

let mainWindow: BrowserWindow | null = null;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 1100,
        height: 800,
        webPreferences: {
            preload: path.join(__dirname, "../preload/preload.ts"),
            contextIsolation: true,
            nodeIntegration: false,
            sandbox: false,
            webSecurity: false,
        },
    });

    if (isDev) {
        mainWindow.loadURL("http://localhost:5173");
    } else {
        mainWindow.loadFile(
            path.join(__dirname, "../../react-dist/index.html")
        );
    }

    mainWindow.on("closed", () => {
        mainWindow = null;
    });
}

app.whenReady().then(createWindow);

app.on("window-all-closed", () => {
    if (process.platform !== "darwin") app.quit();
});
app.on("activate", () => {
    if (mainWindow === null) createWindow();
});

// IPC handlers

ipcMain.handle("select-folder", async () => {
    const res = await dialog.showOpenDialog({ properties: ["openDirectory"] });
    if (res.canceled) return null;
    return res.filePaths[0];
});

ipcMain.handle("get-backend-url", () => {
    return "http://localhost:8000";
});

ipcMain.handle("open-path", async (_event, filePath: string) => {
    // uses the OS default app to open the file
    return await shell.openPath(filePath);
});
