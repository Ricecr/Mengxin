from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

#问卷星一般都是一些简单的选择或者多选题，每一题随机生成一个或多个选项这个不难，而且问卷星的网站不会封ip，但是刷的多了会出现验证码，验证码验证是个难点。
def wenjuanxing(请勿作商业用途):
    driver = webdriver.Chrome('请输入下载浏览器驱动driver的文件目录地址.exe')
    wait = WebDriverWait(driver, 1)  # 设置隐式等待时间
    driver.get(url)  # 打开url中填写的地址
#单选题
    xpath1 = '//*[@id="divquestion1"]/ul/li[%s]' % str(random.randint(1,4)) #请在源代码中找出选项的Xpath位置
    answer_1 = driver.find_elements_by_xpath(xpath1)[0]
    answer_1.click()

    xpath2 = '//*[@id="divquestion2"]/ul/li[%s]' % str(random.randint(1,2))
    answer_2 = driver.find_elements_by_xpath(xpath2)[0]
    answer_2.click()

    xpath3 = '//*[@id="divquestion3"]/ul/li[%s]' % str(random.randint(1,2))
    answer_3 = driver.find_elements_by_xpath(xpath3)[0]
    answer_3.click()
    if xpath3=='//*[@id="divquestion3"]/ul/li[1]':
#多选题(题中有题)
        qList_4 = [str(x) for x in range(1, 5)]
        num = random.randint(2, 3)
        aList_4 = random.sample(qList_4, num)  # 从1，4中随机的选出 2 -> 3项
        for i in aList_4:
            xpath4 = '//*[@id="divquestion4"]/ul/li[%s]' % i
            answer_4 = driver.find_elements_by_xpath(xpath4)[0]
            answer_4.click()

        qList_5 = [str(x) for x in range(1, 5)]
        num = random.randint(2, 3)
        aList_5 = random.sample(qList_5, num)  # 从1，4中随机的选出 2 -> 3项
        for i in aList_5:
            xpath5 = '//*[@id="divquestion5"]/ul/li[%s]' % i
            answer_5 = driver.find_elements_by_xpath(xpath5)[0]
            answer_5.click()

# 填空题
#    name_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="divquestion7"])))  # 使用xpath查找相应的文本框的定位
#    name_input.clear()  # 清楚可能存在的文本框（比如提示的框框）
#    name_input.send_keys('填写自己需要的文字，不可随机')

# 提交
        submit = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="submit_button"]')))  # 定位提交的所在的位置
        submit.click()
        # time.sleep(0)#遇到验证码请把0调成5秒以上以便手动填写验证码
#退出，清除浏览器缓存
        driver.quit()

if __name__ == '__main__':
    url = '请输入网站'
    for i in range(50000):
        wenjuanxing(i)
        print('成功' + str(i) + '次')

