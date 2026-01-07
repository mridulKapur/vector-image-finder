import { useState } from "react";
import { Search, Folder, RefreshCw } from "lucide-react";
import { useApi, type SearchResult } from "@/ui/hooks/useApi";
import { PhotoCard } from "./components/PhotoCard";
import { appStyles } from "@/ui/styles/appStyles";

export default function App() {
    const { selectFolder, indexFolder, search, fileUrl, openPath, loading } =
        useApi();
    const [folder, setFolder] = useState<string | null>(null);
    const [query, setQuery] = useState("");
    const [results, setResults] = useState<SearchResult[]>([]);
    const [isIndexing, setIsIndexing] = useState(false);
    const [searchFocused, setSearchFocused] = useState(false);
    const [hoveredBtn, setHoveredBtn] = useState<string | null>(null);

    async function chooseFolder() {
        const f = await selectFolder();
        if (f) setFolder(f);
    }

    async function index() {
        if (!folder) return;
        setIsIndexing(true);
        await indexFolder(folder);
        setIsIndexing(false);
    }

    async function doSearch() {
        if (!query) return;
        const x = await search(query);
        setResults(x);
    }

    return (
        <div style={appStyles.app}>
            <div style={appStyles.container}>
                <header style={appStyles.header}>
                    <h1 style={appStyles.title}>Photos</h1>
                    <p style={appStyles.subtitle}>AI-powered photo search</p>
                </header>

                <div style={appStyles.searchContainer}>
                    <div style={appStyles.searchIcon}>
                        <Search size={20} />
                    </div>
                    <input
                        style={{
                            ...appStyles.searchInput,
                            ...(searchFocused && {
                                boxShadow:
                                    "0 4px 16px rgba(102, 126, 234, 0.15), 0 0 0 2px rgba(102, 126, 234, 0.3)",
                            }),
                        }}
                        placeholder="Search your photos..."
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                        onKeyDown={(e) => e.key === "Enter" && doSearch()}
                        onFocus={() => setSearchFocused(true)}
                        onBlur={() => setSearchFocused(false)}
                    />
                </div>

                <div style={appStyles.actions}>
                    <button
                        style={{
                            ...appStyles.btn,
                            ...appStyles.btnPrimary,
                            ...(hoveredBtn === "primary" && {
                                transform: "translateY(-2px)",
                                boxShadow:
                                    "0 6px 16px rgba(102, 126, 234, 0.4)",
                            }),
                        }}
                        onClick={chooseFolder}
                        onMouseEnter={() => setHoveredBtn("primary")}
                        onMouseLeave={() => setHoveredBtn(null)}
                    >
                        <Folder size={18} />
                        <span>Choose Folder</span>
                    </button>

                    <button
                        style={{
                            ...appStyles.btn,
                            ...appStyles.btnSecondary,
                            ...(!folder || isIndexing
                                ? appStyles.btnDisabled
                                : {}),
                            ...(hoveredBtn === "secondary" &&
                                !(!folder || isIndexing) && {
                                    background: "#f8f9fa",
                                    transform: "translateY(-2px)",
                                    boxShadow: "0 4px 12px rgba(0, 0, 0, 0.08)",
                                }),
                        }}
                        disabled={!folder || isIndexing}
                        onClick={index}
                        onMouseEnter={() => setHoveredBtn("secondary")}
                        onMouseLeave={() => setHoveredBtn(null)}
                    >
                        <RefreshCw
                            size={18}
                            style={
                                isIndexing
                                    ? { animation: "spin 1s linear infinite" }
                                    : {}
                            }
                        />
                        <span>
                            {isIndexing ? "Indexing..." : "Index Photos"}
                        </span>
                    </button>
                </div>

                {folder && (
                    <div style={appStyles.folderInfo}>
                        <Folder size={16} />
                        <span>{folder}</span>
                    </div>
                )}

                {results.length > 0 && (
                    <div style={appStyles.resultsSection}>
                        <h2 style={appStyles.resultsTitle}>
                            Results ({results.length})
                        </h2>
                        <div style={appStyles.grid}>
                            {results.map((r, i) => (
                                <PhotoCard
                                    key={i}
                                    path={r.path}
                                    score={r.score ?? 0}
                                    fileUrl={fileUrl}
                                    openPath={openPath}
                                />
                            ))}
                        </div>
                    </div>
                )}

                {results.length === 0 && query && (
                    <div style={appStyles.emptyState}>
                        <Search size={48} />
                        <p style={appStyles.emptyStateText}>No photos found</p>
                        <span style={appStyles.emptyStateSubtext}>
                            Try a different search term
                        </span>
                    </div>
                )}
            </div>

            <style>{`
        @keyframes spin {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }

        * {
          margin: 0;
          padding: 0;
          box-sizing: border-box;
        }

        @media (max-width: 768px) {
          /* Mobile responsive adjustments handled via inline styles */
        }
      `}</style>
        </div>
    );
}
