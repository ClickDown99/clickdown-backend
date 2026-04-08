from pytest import fixture

from django.test import Client

@fixture
def client():
    return Client()

""" import httpx
from httpx_retries import Retry, RetryTransport
import hishel
import hishel.httpx as hishel_httpx """

""" @fixture
def retry_tasport():
    retry = Retry(total=3, backoff_factor=0.5)
    transport=RetryTransport(retry=retry)
    return transport

@fixture
def hishel_transport():#Aparentemente não está funcionando direito
    proxy = httpx.Proxy('http://127.0.0.0:8080/tasks/')
    proxy_transport = httpx.HTTPTransport(proxy=proxy,verify=False)
    transport = hishel_httpx.SyncCacheTransport(
        next_transport=proxy_transport,
        storage=hishel.SyncSqliteStorage()
        )
    return transport

@fixture
def retry_trasport_client(retry_tasport):
    client = httpx.Client(
                transport=retry_tasport,
                timeout=5,
                base_url='http://127.0.0.0:8000/'
                )
    return client """

