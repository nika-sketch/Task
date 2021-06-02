import null
from constants import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def check_home_page(driver):
    page_title = driver.title
    assert page_title == EXPECTED_PAGE_TITLE

    phone_number = driver.find_element_by_class_name("shop-phone").text.split(": ")[1]
    assert phone_number == EXPECTED_PHONE_NUMBER

    contact_us_link = driver.find_element_by_xpath('//*[@title="Contact us"]')
    assert contact_us_link != null

    sign_in_link = driver.find_element_by_xpath('//*[@class="login"]')
    assert sign_in_link != null

    women_link = driver.find_element_by_xpath('//*[@title="Women"]')
    assert women_link != null

    dresses_link = driver.find_element_by_xpath('//*[@title="Dresses"]')
    assert dresses_link != null

    t_shirts_link = driver.find_element_by_xpath('//*[@title="T-shirts"]')
    assert t_shirts_link != null

    slider = driver.find_element_by_id("homepage-slider")
    assert slider != null

    for i in range(1, 3):
        banner = driver.find_element_by_class_name("htmlcontent-item-" + str(i))
        assert banner != null and banner.screenshot_as_png != null


def check_popular_products_section(driver):
    popular_link = driver.find_element_by_xpath('//*[@class="homefeatured"]')
    assert popular_link != null

    best_sellers_link = driver.find_element_by_xpath('//*[@class="blockbestsellers"]')
    assert best_sellers_link != null

    product_categories = driver.find_element_by_id("homefeatured").text.split("\n")
    for i in range(len(product_categories)):
        assert product_categories[i] != null


def check_third_product_from_view_button(driver):
    main_product_image = driver.find_element_by_xpath('//*[@title="Printed Dress"]')
    assert main_product_image != null and main_product_image.screenshot_as_png != null

    thumbnail_image = driver.find_element_by_class_name("last")
    assert thumbnail_image != null and thumbnail_image.screenshot_as_png != null


def check_more_for_third_product(driver):
    driver.set_window_size(WINDOW_WIDTH, WIDOW_HEIGHT)
    driver.get(MORE_INFO_ON_THIRD_PRODUCT_URL)

    assert driver.find_element_by_class_name("navigation-pipe").text == ">"

    main_product_image = driver.find_element_by_xpath('//*[@title="Printed Dress"]')
    assert main_product_image != null and main_product_image.screenshot_as_png != null

    for i in range(8, 9):
        thumbnail_pictures = driver.find_element_by_id("thumb_" + str(i))
        assert thumbnail_pictures != null and thumbnail_pictures.screenshot_as_png != null

    page_title = driver.title
    assert page_title == EXPECTED_PAGE_DRESS_TITLE

    condition = driver.find_element_by_id("product_condition").text
    assert condition == EXPECTED_CONDITION

    description = driver.find_element_by_id("short_description_content").text
    assert description == EXPECTED_DESCRIPTION

    twitter_link = driver.find_element_by_xpath('//*[@class="icon-twitter"]')
    assert twitter_link != null

    facebook_link = driver.find_element_by_xpath('//*[@class="icon-facebook"]')
    assert facebook_link != null

    google_plus_link = driver.find_element_by_xpath('//*[@class="icon-google-plus"]')
    assert google_plus_link != null

    pinterest_link = driver.find_element_by_xpath('//*[@class="icon-pinterest"]')
    assert pinterest_link != null

    price_display = driver.find_element_by_id("our_price_display").text
    assert price_display == EXPECTED_PRICE

    quantity_selector = driver.find_element_by_id("quantity_wanted").tag_name
    assert quantity_selector == EXPECTED_INPUT

    minus_button = driver.find_element_by_xpath('//*[@class="icon-minus"]')
    minus_button != null

    plus_button = driver.find_element_by_xpath('//*[@class="icon-plus"]')
    plus_button != null

    size_selector = driver.find_element_by_id("group_1").text.split("\n")
    for size in size_selector:
        assert size != null

    color_selector = driver.find_element_by_xpath('//*[@id="color_13"]')
    assert color_selector != null

    add_to_cart_button = driver.find_element_by_xpath('//*[@id="add_to_cart"]/button/span')
    assert add_to_cart_button != null

    add_to_wish_list_button = driver.find_element_by_xpath('//*[@id="wishlist_button"]')
    assert add_to_wish_list_button != null

    send_to_a_friend = driver.find_element_by_id("send_friend_button").text
    assert send_to_a_friend == EXPECTED_SEND_TO_A_FRIEND_TEXT

    print_button = driver.find_element_by_class_name("print").text
    assert print_button == EXPECTED_PRINT_BUTTON_TEXT

    add_to_cart_button.click()


def check_add_to_cart_button(driver):
    driver.set_window_size(WINDOW_WIDTH, WIDOW_HEIGHT)
    driver.get(MORE_INFO_ON_THIRD_PRODUCT_URL)

    icon_ok = driver.find_element_by_class_name("icon-ok").tag_name
    assert icon_ok == "i"

    main_product_image = driver.find_element_by_xpath('//*[@title="Printed Dress"]')
    assert main_product_image != null and main_product_image.screenshot_as_png != null

    product_title = driver.title
    assert product_title == EXPECTED_PRODUCT_TITLE

    product_price = driver.find_element_by_xpath('//*[@id="layer_cart_product_price"]')
    assert product_price != null

    total_product_price = driver.find_element_by_xpath('//*[@class="ajax_block_products_total"]')
    assert total_product_price != null

    total_product_shipping = driver.find_element_by_xpath('//*[@class="ajax_cart_shipping_cost"]')
    assert total_product_shipping != null

    total = driver.find_element_by_xpath('//*[@class="ajax_block_cart_total"]')
    assert total != null

    continue_shopping_button = driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span')
    assert continue_shopping_button != null

    proceed_to_checkout_button = driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')
    assert proceed_to_checkout_button != null

    close_button = driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[1]/span')
    assert close_button != null


def check_click_proceed_to_check_out_button(driver):
    driver.set_window_size(WINDOW_WIDTH, WIDOW_HEIGHT)
    driver.get(CHECKOUT_URL)

    summary = driver.find_element_by_xpath('//*[@id="order_step"]/li[1]/span').text
    assert summary == EXPECTED_SUMMARY

    sign_in = driver.find_element_by_xpath('//*[@id="order_step"]/li[2]/span').text
    assert sign_in == EXPECETED_SIGN_IN

    address = driver.find_element_by_xpath('//*[@id="order_step"]/li[3]/span').text
    assert address == EXPECTED_ADDRESS

    order_step = driver.find_element_by_id("order_step").text.split("\n")
    for i in range(len(order_step)):
        assert order_step[i] != null

    proceed_checkout_button = driver.find_element_by_xpath('//*[@id="center_column"]/p[2]/a[1]/span')
    assert proceed_checkout_button != null


def check_proceed_to_chek_out(driver):
    driver.set_window_size(WINDOW_WIDTH, WIDOW_HEIGHT)
    driver.get(PROCEED_URL)

    create_account_form = driver.find_element_by_id("create-account_form").text.split("\n")
    for item in create_account_form:
        assert item != null

    login_form = driver.find_element_by_id("login_form").text.split("\n")
    for item in login_form:
        assert item != null

    #An account using this email address has already been registered. Please enter a valid password or request a new one.
    enter_email = driver.find_element_by_id("email_create")
    enter_email.send_keys("JohnDoeRandomEmailForTask.net")

    submit_create = driver.find_element_by_id("SubmitCreate")
    submit_create.click()
    time.sleep(10)

    customer_first_name = driver.find_element_by_xpath('//*[@id="customer_firstname"]')
    customer_first_name.send_keys("John")

    customer_last_name = driver.find_element_by_xpath('//*[@id="customer_lastname"]')
    customer_last_name.send_keys("Doe")

    first_name = driver.find_element_by_xpath('//*[@id="firstname"]')
    first_name.send_keys("John")

    last_name = driver.find_element_by_xpath('//*[@id="lastname"]')
    last_name.send_keys("Doe")

    customer_password = driver.find_element_by_xpath('//*[@id="passwd"]')
    customer_password.send_keys("paroli")

    customer_day_of_birth = driver.find_element_by_xpath('//*[@id="days"]')
    customer_day_of_birth.send_keys("3")

    customer_month_of_birth = driver.find_element_by_xpath('//*[@id="months"]')
    customer_month_of_birth.send_keys("May")

    customer_year_of_birth = driver.find_element_by_xpath('//*[@id="years"]')
    customer_year_of_birth.send_keys("1973")

    city = driver.find_element_by_xpath('//*[@id="city"]')
    city.send_keys("Jersey")

    state = driver.find_element_by_xpath('//*[@id="id_state"]')
    state.send_keys("Georgia")

    zip_code = driver.find_element_by_xpath('//*[@id="postcode"]')
    zip_code.send_keys("30014")

    home_phone = driver.find_element_by_xpath('//*[@id="phone"]')
    home_phone.send_keys("+17706091425")

    additional_info = driver.find_element_by_xpath('//*[@id="other"]')
    additional_info.send_keys("My name is Joe")

    address = driver.find_element_by_xpath('//*[@id="address1"]')
    address.send_keys("115 lower Jersey RD")

    register_button = driver.find_element_by_xpath('//*[@id="submitAccount"]/span')
    register_button.click()
    time.sleep(10)

    check_out_button = driver.find_element_by_xpath('//*[@id="center_column"]/form/p/button/span')
    check_out_button.click()

    check_fee = driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[1]/div/div/table/tbody/tr/td[4]/div').text
    assert check_fee == "$2.00"

    check_box = driver.find_element_by_xpath('//*[@id="cgv"]')
    check_box.click()
    time.sleep(5)

    check_proceed_button_again = driver.find_element_by_xpath('//*[@id="form"]/p/button/span')
    check_proceed_button_again.click()

    check_cart_summary = driver.find_element_by_xpath('//*[@id="cart_summary"]').text.split("\n")
    for item in check_cart_summary:
        assert item != null

    pay_by_bank = driver.find_element_by_xpath('//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a')
    pay_by_bank.click()

    confirm_order_button = driver.find_element_by_xpath('//*[@id="cart_navigation"]/button/span')
    confirm_order_button.click()

    check_result = driver.find_element_by_xpath('//*[@id="center_column"]/div/p/strong').text
    assert check_result == EXPECTED_RESULT


if __name__ == '__main__':
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.set_window_size(WINDOW_WIDTH, WIDOW_HEIGHT)
    driver.get(SITE_URL)

    check_home_page(driver)
    check_popular_products_section(driver)
    check_third_product_from_view_button(driver)
    check_more_for_third_product(driver)
    check_add_to_cart_button(driver)
    check_click_proceed_to_check_out_button(driver)
    check_proceed_to_chek_out(driver)

