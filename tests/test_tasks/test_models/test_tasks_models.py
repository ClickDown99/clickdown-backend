from tasks import models
from pytest import mark



@mark.django_db                                                           
def test_when_taks_is_created_then_needs_to_be_within_db(create_task):
    qtd_tasks = models.Task.objects.count()
    assert qtd_tasks == 1

@mark.django_db  
def test_when_subtaks_is_created_then_must_be_associeted_to_parent_task(create_subtask):
    parent_subtask = create_subtask.parent_id
    assert parent_subtask

@mark.django_db  
def test_when_task_dont_have_parent_task_then_parent_task_id_must_be_none(create_task):
    task = create_task
    assert task.parent_id is None