
import time
from pathlib import Path
import os
import csv
from loggingconfig import logging_ins


# this function use for serialize data after split from text
def serialize_data(strs:[]):
    if " - " in str(strs[3]):
        # In here I only use the first price as the sample measure
        prices = str(strs[3]).split(" - ")
        prices[0] = prices[0][1:].replace(".","")
        strs[3] = int(prices[0])
    else:
        price = str(strs[3])
        price = price[1:].replace(".","")
        strs[3] = int(price)
    total_sell = 0
    # calculate revenue
    if ',' in str(strs[4]):
        total_sell = int(str(strs[4]).split(" ")[2].replace(",","").replace("k","00")) * strs[3]
    else:
        total_sell = int(str(strs[4]).split(" ")[2].replace(",","").replace("k","000")) * strs[3]
    strs[4] = total_sell
    
    return strs


# extract each line of txt data file as a specific row
def split_line(line:str):
    extract_line = line.split("||")[1:]
    return extract_line



if __name__ == '__main__':
    # I decide use basic python logging for management and tracing after finish flow
    
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
    header = ['STT', 'product_name', 'product_url', 'product_price','product_revenue']
    start_time = time.time()
    current_directory = Path.cwd()
    log = logging_ins(pathfile=f"{current_directory}/logs/transform.log")
    # process sequently by category
    for i in category_url:
        dir_name = i.split(".")[0]
        directory_path = Path(f"{current_directory}/{dir_name}")
        directory_path.mkdir(parents=True, exist_ok=True)
        # read data from specific folder which contain accurately the signal of product
        fr = open(f"{directory_path}\{i}.txt", "r")
        with open(f"{directory_path}\{i}.csv", "w",encoding='utf-8') as fw:
            writer = csv.writer(fw)
            writer.writerow(header)
            for line in fr.readlines():
                print("Line: ",line)
                try:
                    data_ele = split_line(line)
                    if data_ele==[]:
                        continue
                    transformed_data = serialize_data(data_ele)
                    writer.writerow(transformed_data)
                    log.info(f'Transform Successfully {fw.name}')
                except Exception as e:
                    log.critical(f'Error when tranforming data at {fw.name}|{e}')
                    print("ErrorParent: ",e)
                    continue
            log.info(f'Transform {fw.name} Successfully')
        log.info(f'Transform Category {i} Successfully')
        fw.close()
        fr.close()
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time} seconds")