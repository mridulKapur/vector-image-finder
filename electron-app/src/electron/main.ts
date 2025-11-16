import { app, BrowserWindow,ipcMain,dialog } from "electron";
import path from "path";
import isDev from 'electron-is-dev'

app.on("ready", () => {
  const mainWindow = new BrowserWindow({});
  const finalPath = path.join(app.getAppPath() + "/dist-react/index.html");
  mainWindow.loadFile(finalPath);
});

let mainWindow: BrowserWindow | null = null;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1100,
    height: 800,
    webPreferences: {
      preload: path.join(__dirname, "../src-electron/preload.js"),
      contextIsolation: true,
      nodeIntegration: false,
    },
  });

  if (isDev) {
    mainWindow.loadURL("http://localhost:5173");
  } else {
    mainWindow.loadFile(path.join(__dirname, "../dist/index.html"));
  }

  mainWindow.on("closed", () => (mainWindow = null));
}

app.on("ready", createWindow);

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});

app.on("activate", () => {
  if (mainWindow === null) createWindow();
});

// IPC handler for folder selection
ipcMain.handle("select-folder", async () => {
  const res = await dialog.showOpenDialog({ properties: ["openDirectory"] });
  if (res.canceled) return null;
  return res.filePaths[0];
});
