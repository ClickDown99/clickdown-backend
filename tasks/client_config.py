import time
import uuid

import httpx
import hishel
import hishel.httpx
from httpx_retries import Retry, RetryTransport
import logging

proxy = httpx.Proxy("http://127.0.0.1:8080")
retry = Retry(total=2, backoff_factor=0.5)
proxy_transport = httpx.HTTPTransport(proxy=proxy, verify=False)
retry_transport = RetryTransport(proxy_transport, retry=retry)
transport = hishel.httpx.SyncCacheTransport(
    next_transport=retry_transport,
    storage=hishel.SyncSqliteStorage(),
)

def before_request(request: httpx.Request):
    request_id = str(uuid.uuid4())
    request.headers['X-Request-ID'] = request_id
    request.extensions['request_id'] = request_id
    request.extensions['start_time'] = time.monotonic()

def prepare_logger(response: httpx.Response):
    logger = logging.getLogger('external_requests_logger')
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("tasks/logs.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

def after_request(response: httpx.Response):
    request = response.request
    start = response.request.extensions.get("start_time", None)
    if start:
        elapsed = time.monotonic() - start
    else:
        elapsed = None
    
    logger = logging.getLogger('external_requests_logger')
    logger.info(
        f'{request.method} {request.url} {response.status_code} '#+
        f'{elapsed} {request.extensions.get("request_id")}'
    )