from collections import deque
import threading
from app.domain.indexing.service import IndexingService

class Job:
    def __init__(self, job_type, payload):
        self.job_type = job_type
        self.payload = payload

# In-memory queue
queue = deque()
lock = threading.Lock()
worker_thread = None

def enqueue(job: Job):
    with lock:
        queue.append(job)

def worker(indexing_service: IndexingService):
    while True:
        job = None
        with lock:
            if queue:
                job = queue.popleft()
        
        if job:
            if job.job_type == "index_folder":
                indexing_service.index_folder(job.payload["folder_path"])

def start_worker(indexing_service: IndexingService):
    global worker_thread
    worker_thread = threading.Thread(target=worker, args=(indexing_service,))
    worker_thread.daemon = True
    worker_thread.start()
