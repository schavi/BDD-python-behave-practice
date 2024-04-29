
import behave

from time import sleep

from POM.page_model import Ecosia

@given("Opening ecosia.org")
def open_ecosia(context):
    context.page = Ecosia(chosen_browser="firefox")
    context.page.open()

@when("Entering '{query}' into the search bar")
def enter_search_query(context, query):
    context.page.main_search_input().send_keys(query)

@when("Clicking the search button")
def click_search_button(context):
    context.page.main_search_button().click()

@then("The behave documentation shows up in the results")
def check_behave_docs_in_results(context):
    assert "https://behave.readthedocs.io/en/stable/" in [link.get_attribute("href") for link in context.page.result_all_links()]
    context.page.close()

@when("Clicking the images tab")
def clicking_the_images_tab(context):
    context.page.result_images_tab_button().click()

@then("Images of '{query}'s are shown")
def relevant_images_are_shown(context, query):
    image_result_labels = [element.get_attribute("aria-label") for element in context.page.result_images_articles()]
    assert any(query in label for label in image_result_labels)
    context.page.close()