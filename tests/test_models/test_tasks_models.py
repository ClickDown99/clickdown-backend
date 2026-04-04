from tasks import models
from pytest import mark



# @mark.parametrize('task_name, progress_id, priority_id, order', (
#                                                             ('fazer os testes',1,1,1),
#                                                             ('Fritar um empanado',2,2,2),
#                                                             ('Dormir',3,3,3)
#                                                             ),
#                                                             indirect=True)
@mark.django_db                                                           
def test_when_taks_is_created_then_needs_to_be_within_db(create_task):
    task_objects = [models.Task.objects.filter(id=i) for i in range(3)]
    assert len(task_objects) == 3

def test_when_subtaks_is_created_then_must_be_associated_with_task():
    assert True

def test_when_task_dont_have_parent_task_then_parent_task_id_must_be_none():
    assert True