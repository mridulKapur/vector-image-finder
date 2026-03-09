## Backend Architecture

The backend follows a layered architecture:

- **API layer** handles HTTP requests and validation
- **Search layer** performs query embedding and vector retrieval
- **Indexing layer** processes asynchronous image ingestion
- **Embedding layer** generates multimodal vectors using CLIP
- **Storage layer** abstracts vector DB and object storage
- **Jobs layer** manages background task orchestration

This design separates online search paths from offline indexing jobs,
ensuring low-latency queries and scalable ingestion.
