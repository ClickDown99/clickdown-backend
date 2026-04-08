import httpx
from tasks import views
from http import HTTPStatus
from respx import MockRouter




def test_timeout(client, respx_mock:MockRouter):
    respx_mock.get(
        #"http://127.0.0.1:8000/tasks/delay/10"
    ).mock(
        side_effect=httpx.ReadTimeout("Timeout")
    )

    response = client.get("/tasks/external-request/")

    assert response.status_code == 200
    assert b"Request Timeout" in response.content

def test_example_of_view_with_external_request_server_error(client, respx_mock):
    mocked = respx_mock.get(
        #"http://127.0.0.1:8000/tasks/delay/10"
        ).mock(
        return_value=httpx.Response(
            HTTPStatus.INTERNAL_SERVER_ERROR
        )
    )
    response = client.get("/tasks/external-request/")

    assert mocked.called
    assert response.status_code == 200
    assert b'Exception' in response.content






    


def test_when_a_task_was_created_then_task_needs_to_be_in_tasks_page_content():

    assert True # Precisa garantir que a task esteja no parâmetro tasks

def test_when_parent_id_is_none_then_task_needs_to_be_in_1st_level():
    assert True #Garantir que a task esteja no primeiro nível

def test_when_task_have_parent_id_then_must_be_in_subtasks_of_parent_id():
    assert True

def test_when_tasks_is_called_then_must_return_the_tasks():
    assert True