from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pathlib import Path
import os
from loggingconfig import logging_ins


# scroll from start to the end of website for completely loading data 
def scroll_all_page(dr,second):
    dr.execute_script("window.scrollTo(0, 1500);")
    time.sleep(second)
    dr.execute_script("window.scrollTo(0, 2500);")
    time.sleep(second)
    dr.execute_script("window.scrollTo(0, 4000);")
    time.sleep(second)

#conduct crawl data by seeking element in html text
def crawl_data(driver_crawl,nop):
    scroll_all_page(driver_crawl,1)
    idx = 1
    try:
        while True:
            print(f"Page {idx}")
            # f.write(f"\nPage {idx}")
            idxpage = 1
            print(f'Page Index: {idxpage}')
            element = driver_crawl.find_elements(By.CLASS_NAME,'col-xs-2-4')
            for i in range(0,len(element)):
                try:
                    #search element contain value for crawlng
                    child = element[i].find_element(By.CLASS_NAME,'gHKRq2')
                    card_element = child.find_element(By.CLASS_NAME,'J1Dw2W')
                    name_element = card_element.find_element(By.CLASS_NAME,'OspxFR')
                    only_element_name = name_element.find_element(By.CLASS_NAME,'v5rrDh')
                    url_product = element[i].find_element(By.TAG_NAME,"a").get_attribute("href")
                    price_product = card_element.find_element(By.CLASS_NAME,"COjcOU")
                    rating = card_element.find_element(By.CLASS_NAME,'MpNuVJ')
                    print(f'\n{nop}||{idxpage}||{only_element_name.text}||{url_product}||{price_product.text}||{rating.text}')
                    f.write(f'\n{nop}||{idxpage}||{only_element_name.text}||{url_product}||{price_product.text}||{rating.text}')
                    idxpage+=1
                    nop+=1
                except Exception as e:
                    log.critical(f'Crawl Fail At {idx} PAge')
                    idxpage+=1
                    nop+=1
                    continue
            pag_btn_element = driver_crawl.find_element(By.XPATH,f"//div[@class='shopee-page-controller']/button[text()='{idx}']")
            pag_btn_element.click()
            time.sleep(1)
            scroll_all_page(driver,1)
            idx+=1

    except Exception as e:
        print(f'Error: Idx: {idx}')
    finally:
        return nop

# seeking paging button element by class name then click every for naviagating to next page
def next_category(dr,numop):
    more_option_btn = dr.find_element(By.CLASS_NAME,'shopee-category-list__toggle-btn')
    more_option_btn.click()
    time.sleep(0.5)
    category_elements = dr.find_elements(By.CLASS_NAME,'shopee-category-list__sub-category')
    for category_ele in category_elements:
        log.info(f'Start Crawling data of {category_ele}')
        category_ele.click()
        time.sleep(1)
        numop = crawl_data(dr,numop)
        print(numop)
        if numop > 3000:
            break
        


if __name__ == '__main__':
    
    shopee_site = "https://shopee.vn"
    category_url = [
        "Thời-Trang-Nam-cat.11035567",
        "Điện-Thoại-Phụ-Kiện-cat.11036030",
        "Thiết-Bị-Điện-Tử-cat.11036132",
        "Máy-Tính-Laptop-cat.11035954",
        "Máy-Ảnh-Máy-Quay-Phim-cat.11036101",
        "Đồng-Hồ-cat.11035788",
        "Giày-Dép-Nam-cat.11035801",
        "Thiết-Bị-Điện-Gia-Dụng-cat.11036971",
        "Thể-Thao-Du-Lịch-cat.11035478",
        "Ô-Tô-Xe-Máy-Xe-Đạp-cat.11036793",
        "Thời-Trang-Nữ-cat.11035639",
        "Mẹ-Bé-cat.11036194",
        "Nhà-Cửa-Đời-Sống-cat.11036670",
        "Sắc-Đẹp-cat.11036279",
        "Sức-Khỏe-cat.11036345",
        "Giày-Dép-Nữ-cat.11035825",
        "Túi-Ví-Nữ-cat.11035761",
        "Phụ-Kiện-Trang-Sức-Nữ-cat.11035853",
        "Bách-Hóa-Online-cat.11036525",
        "Nhà-Sách-Online-cat.11036863",
        "Balo-Túi-Ví-Nam-cat.11035741",
        "Thời-Trang-Trẻ-Em-cat.11036382",
        "Đồ-Chơi-cat.11036932",
        "Giặt-Giũ-Chăm-Sóc-Nhà-Cửa-cat.11036624",
        "Chăm-Sóc-Thú-Cưng-cat.11036478",
        "Voucher-Dịch-Vụ-cat.11035898",
        "Dụng-cụ-và-thiết-bị-tiện-ích-cat.11116484"
    ]

    driver = webdriver.Chrome()
    start_time = time.time()
    current_directory = Path.cwd()
    log = logging_ins(pathfile=f"{current_directory}/logs/crawl.log")
     # process sequently by category
    for i in category_url:
        dir_name = i.split(".")[0]
        directory_path = Path(f"{current_directory}/{dir_name}")
        directory_path.mkdir(parents=True, exist_ok=True)
        f = open(f"{directory_path}/{i}.txt", "a")
        driver.get(f"{shopee_site}/{i}")
        noproduct = 0
        time.sleep(2)
        next_category(driver,noproduct)
        f.close()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time} seconds")