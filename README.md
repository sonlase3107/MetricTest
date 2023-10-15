# SonLA Metric Test
1. Yêu Cầu
    Thực hiện Crawl data các sản phẩm theo các danh mục và transform thành file CSV
2. Tổng Quan Kết Quả
    Thực hiện crawl dữ liệu từ Shopee bằng thư viện Selenium của Python, code luồng để trình duyệt driver chạy qua các trang có sản phẩm và truy xuất data thông qua thẻ HTML của trình duyệt
    a. Cấu trúc thư mục
        Do hiện tại thời gian ngắn nên mình để cấu trúc như sau:
        - crawl.py
            File chứa code để Crawl data về dưới local và lưu thành dạng txt
        - transform.py
            File chứa code để thực hiện đọc dữ liệu từ các file txt được chia theo mỗi category được tạo riêng thành các Folder, sau đó thực hiện transform và ghi thành csv file (cùng thư mục category)
        - loggingconfig.py
            File khởi tạo config cho logging, phục vụ lưu log của luồng
    b. Hướng dẫn chạy
        1. Cài đặt các thư viện của Selenium thủ công
        2. Chạy File crawl.py
        3. Chạy File transform.py
3. Báo cáo yêu cầu
    a. Test 1
        Số lượng sản phẩm lấy được: Lần nhiều nhất lấy được là khoảng 20.000 sản phẩm nếu chạy hết tất cả các danh mục, tốn khoảng 1 tiếng rưỡi nếu tốc độ mạng ổn định với máy 32GB
        Số lượng sản phẩm lấy được trong 1 phút: từ 7 - 10 sản phẩm / phút nên sẽ khoảng 400 đến 600 sản phẩm
    b. Test 2
        Số sản phẩm transform được trong phút: Hiện tại dữ liệu raw lưu ở Local nên việc đọc ghi file nhanh
            Thực hiện test thử với khoảng 7000 sản phẩm sẽ mất tầm 2 đến 3
            