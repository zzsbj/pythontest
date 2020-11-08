import time
def login_page(username,password,driver):  #输入账号密码
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()
def open_url(url,driver):  #打开网页
    driver.get(url)
    driver.maximize_window()
def search_key(url, driver, username, password,s_key):
    open_url(url, driver)
    login_page(username, password, driver)
    driver.find_element_by_xpath("//span [text()='零售出库']").click()
    p_id=driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
    f_id = p_id + "-frame"
    driver.switch_to.frame(1)
    driver.find_element_by_id ("searchNumber") .send_keys (s_key)
    driver.find_element_by_id("searchBtn").click()
    time.sleep(1)   #隐式等待不生效时， 加强制等待
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num