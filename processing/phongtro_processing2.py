#đọc dữ liệu trong file PhanTichDinhLuong/PhanTichDinhLuong/spider/phongtro.csv

import pandas as pd

file_path = '../PhanTichDinhLuong/spiders/phongtro.csv'

try:
    # Đọc file CSV, bỏ qua các dòng lỗi
    df = pd.read_csv(file_path, delimiter=';', on_bad_lines='skip', encoding='utf-8')

    print("Tên các cột trong dữ liệu:")
    print(df.columns)

    # Hiển thị thông tin dữ liệu
    print("Thông tin dữ liệu:")
    print(df.info())

    # Hiển thị 5 dòng đầu tiên
    print("Dữ liệu mẫu:")
    print(df.head())
    
except Exception as e:
  
    print(f"Lỗi xảy ra: {e}")
