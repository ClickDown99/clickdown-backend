from time import sleep

from pytest import mark


def xpto():
    assert True

#@mark.usefixtures
def test_when_task_is_created_then_needs_to_be_within_tasks_page():
    assert True

#@mark.selenium_test
@mark.skip(reason='Servidor do Front está desligado')
def test_open_blog_page(open_blog_page):#Apenas esboço
    driver = open_blog_page
    assert driver


