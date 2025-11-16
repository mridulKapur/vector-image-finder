// electron-app/src/ui/App.tsx
import React, { useState } from 'react';
import { useApi } from '@/ui/hooks/useApi';

type Result = { path: string; score?: number };

export default function App() {
  const { loading, selectFolder, indexFolder, search, thumbnailUrl, openPath } = useApi();
  const [folder, setFolder] = useState<string | null>(null);
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<Result[]>([]);

  const onChooseFolder = async () => {
    const f = await selectFolder();
    if (f) setFolder(f);
  };

  const onIndex = async () => {
    if (!folder) return alert('Choose folder first');
    await indexFolder(folder);
    alert('Indexing started / completed (depending on dataset)');
  };

  const onSearch = async () => {
    if (!query) return;
    const res = await search(query);
    setResults(res);
  };

  return (
    <div style={{ padding: 18 }}>
      <h2>Local Photo Search</h2>

      <div style={{ marginBottom: 10 }}>
        <button onClick={onChooseFolder}>Choose folder</button>
        <span style={{ marginLeft: 10 }}>{folder ?? 'No folder chosen'}</span>
      </div>

      <div style={{ marginBottom: 10 }}>
        <button onClick={onIndex} disabled={!folder || loading}>
          {loading ? 'Working...' : 'Index folder'}
        </button>
      </div>

      <div style={{ marginBottom: 10 }}>
        <input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Search text..." style={{ width: 400 }} />
        <button onClick={onSearch} style={{ marginLeft: 8 }}>Search</button>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(220px, 1fr))', gap: 12 }}>
        {results.map((r, i) => (
          <ImageCard key={i} result={r} thumbnailUrl={thumbnailUrl} openPath={openPath} />
        ))}
      </div>
    </div>
  );
}

function ImageCard({ result, thumbnailUrl, openPath }: { result: Result; thumbnailUrl: (p: string) => Promise<string>; openPath: (p: string) => void }) {
  const [thumb, setThumb] = useState<string | null>(null);

  React.useEffect(() => {
    let mounted = true;
    thumbnailUrl(result.path).then((url) => {
      if (mounted) setThumb(url);
    }).catch(() => {
      // ignore
    });
    return () => { mounted = false; };
  }, [result.path, thumbnailUrl]);

  return (
    <div style={{ border: '1px solid #ddd', padding: 8 }}>
      <img src={thumb ?? ''} alt={result.path} style={{ width: '100%', height: 160, objectFit: 'cover' }} />
      <div style={{ marginTop: 6 }}>
        <div style={{ fontSize: 12, color: '#333' }}>{result.path}</div>
        <div style={{ fontSize: 12, color: '#666' }}>{result.score ? result.score.toFixed(3) : ''}</div>
        <button onClick={() => openPath(result.path)} style={{ marginTop: 6 }}>Open</button>
      </div>
    </div>
  );
}
