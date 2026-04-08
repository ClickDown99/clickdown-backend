from pytest import fixture
from tasks import models as task_models
#from authentication import models as authentication_models
#from datetime import datetime

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

@fixture(params=(
    {'task_name':'fazer os testes', 'progress_id':1, "priority_id":1, "order":1},
    {'task_name':'fritar um empanado', 'progress_id':2, "priority_id":2, "order":2},
    {'task_name':'dormir', 'progress_id':3, "priority_id":3, "order":3}
    ))
def create_task(request, create_priority, create_progress):
    valores=request.param.copy()
    task_name=valores['task_name']
    progress_id=valores["progress_id"]
    priority_id=valores["priority_id"]
    order=valores["order"]
    progress = task_models.Progress.objects.get(id=progress_id)
    priority = task_models.Priority.objects.get(id=priority_id)

    task = task_models.Task.objects.create(#id=1,
                                    name=task_name,
                                    description='pipipipopopo', 
                                    parent_id=None, 
                                    progress=progress, 
                                    priority=priority,
                                    date_limit=None, 
                                    trash=False, 
                                    trash_date_limit=None, 
                                    order=order) 
    return task

@fixture(params=(
    {'task_name':'Essa é uma subtask', 'progress_id':1, "priority_id":1, "order":1},
    ))

def create_subtask(request, create_task):   
    valores=request.param.copy()

    parent_id=task_models.Task.objects.get(id=1)
    task_name=valores['task_name']
    progress_id=valores["progress_id"]
    priority_id=valores["priority_id"]
    order=valores["order"]
    progress = task_models.Progress.objects.get(id=progress_id)
    priority = task_models.Priority.objects.get(id=priority_id)


    task = task_models.Task.objects.create(#id=1,
                                    name=task_name,
                                    description='pipipipopopo', 
                                    parent_id=parent_id, 
                                    progress=progress, 
                                    priority=priority,
                                    date_limit=None, 
                                    trash=False, 
                                    trash_date_limit=None, 
                                    order=order)
    return task