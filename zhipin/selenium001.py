#coding:utf-8
from selenium import webdriver
import time
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Remote(command_executor='http://192.168.33.133:4444/wd/hub',
desired_capabilities = chrome_options.to_capabilities())
try:
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)
    driver.get('https://sell.paipai.com/auction-list/')
    # driver.find_element_by_id("kw").send_keys("docker selenium test")
    # driver.find_element_by_id("su").click()
    # driver.get_screenshot_as_file("/tmp/pycharm_project_641/zhipin/img1.png")
    source = driver.page_source
    open("888888888.html", 'wb').write(source.encode("utf-8"))

    nows = driver.find_elements_by_css_selector("[class='gl-i-wrap']")
    for now in nows[:]:
        # 价格
        t = now.text
        x = now.find_element_by_css_selector('[class="p-price"]').text
        source = now.find_element_by_xpath(".//div[@class='p-label']/span").text
        print "[[[[[[[[[[[[[[[[[[[[[" + source + "]]]]]]]]]]]]]]]]]]]]]]]]"
        name = now.find_element_by_xpath(".//div[@class='p-name']").text
        print "[[[[[[[[[[[[[[[[[[[[[" + name + "]]]]]]]]]]]]]]]]]]]]]]]]"
        href = now.find_element_by_xpath(".//div[@class='p-img']/a").get_attribute("href")
        print "[[[[[[[[[[[[[[[[[[[[[" + href + "]]]]]]]]]]]]]]]]]]]]]]]]"
        time = now.find_element_by_xpath(".//span[@class='time']").text
        print "[[[[[[[[[[[[[[[[[[[[[" + time + "]]]]]]]]]]]]]]]]]]]]]]]]"

    # driver.find_elements_by_class_name("number")[2].click();
    # time.sleep(5)
    # source1 = driver.page_source
    # open("999999999.html", 'wb').write(source1.encode("utf-8"))
finally:
    driver.quit()

# driver = webdriver.Remote(command_executor='http://192.168.33.133:4444/wd/hub',
# desired_capabilities = chrome_options.to_capabilities())
# driver.page_source = source
# driver.find_elements_by_class_name("el-pager number")[2].click();
# driver_page_source = driver.page_source
# open("111111.html", 'wb').write(driver_page_source)

