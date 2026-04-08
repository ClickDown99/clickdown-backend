from re import A

from pytest import fixture
from selenium import webdriver
from time import sleep

#from tkinter.tix import DirList


@fixture
def initial_settings():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--incognito')
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(options=options, service=service)

    yield driver

    driver.quit()

@fixture
def open_tasks_page(initial_settings):
    driver = initial_settings
    URL_TASK_PAGE = 'http://127.0.0.1:8000/tasks/'
    driver.get(URL_TASK_PAGE)
    return driver
    #sleep(5)

@fixture
def open_blog_page(initial_settings):
    driver = initial_settings
    URL_BLOG_PAGE = 'http://localhost:3000/blog'
    driver.get(URL_BLOG_PAGE)
    return driver
    #sleep(5)