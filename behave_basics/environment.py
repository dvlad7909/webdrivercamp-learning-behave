from selenium import webdriver


def before_feature(context, feature):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()


def after_feature(context, feature):
    context.browser.close()
