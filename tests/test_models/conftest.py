from pytest import fixture, mark
from tasks import models as task_models
from authentication import models as authentication_models
from datetime import datetime

@fixture
def create_progress():
    todo = task_models.Progress.objects.create(id=1, description='to_do')
    in_progress = task_models.Progress.objects.create(id=2, description='in_progress')
    done = task_models.Progress.objects.create(id=3, description='done')
    return (todo, in_progress, done)

@fixture
def create_priority():
    medium_priority = task_models.Priority.objects.create(id=1, description='low_priority')
    medium_priority = task_models.Priority.objects.create(id=2, description='medium_priority')
    high_priority = task_models.Priority.objects.create(id=3, description='high_priority')
    return (medium_priority, medium_priority, high_priority)

@fixture(params=(('fazer os testes',1,1,1),('Fritar um empanado',2,2,2),('Dormir',3,3,3)))
def create_task(request, create_priority, create_progress):
    #print(request.param)
    task_name=request.param[0]
    progress_id=request.param[1]
    priority_id=request.param[2]
    order=request.param[3]
    #user = authentication_models.User.objects.get(None)
    progress = task_models.Progress.objects.get(id=progress_id)
    priority = task_models.Priority.objects.get(id=priority_id)
    
    print(progress)
    task = task_models.Task.objects.create(id=1,
                                    name=task_name,
                                    description='pipipipopopo', 
                                    parent_id=None, 
                                    progress=progress, 
                                    priority=priority,
                                    date_limit=datetime.now(), 
                                    #assignees=None, 
                                    trash=False, 
                                    trash_date_limit=datetime.now(), 
                                    #team=None, 
                                    order=order) 
    return task


def test_define_parameters():
    assert True