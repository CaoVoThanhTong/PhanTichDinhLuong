import pandas as pd
import numpy as np
import os
from normalization import standardize_address

def process_data():
    # Đọc dữ liệu từ file JSON
    file_path = '../PhanTichDinhLuong/spiders/phongtro.json'
    try:
        df = pd.read_json(file_path, lines=True)
        print("Dữ liệu đã được tải thành công.")
    except ValueError as e:
        print(f"Lỗi khi đọc file JSON: {e}")
        return

    # Tách và chuẩn hóa địa chỉ
    if 'address' in df.columns:
        df[['Đường', 'Phường', 'Quận/Huyện', 'Thành phố']] = df['address'].str.split(',', n=3, expand=True)
        df = standardize_address(df)

    # Xử lý cột 'public_date' và 'expired_date'
    if 'public_date' in df.columns and 'expired_date' in df.columns:
        df['Ngày đăng'] = pd.to_datetime(df['public_date'].str.replace(r"^Thứ \w+, ", "", regex=True), format="%H:%M %d/%m/%Y", errors='coerce')
        df['Ngày hết hạn'] = pd.to_datetime(df['expired_date'].str.replace(r"^Thứ \w+, ", "", regex=True), format="%H:%M %d/%m/%Y", errors='coerce')
        df['Thời gian đăng (ngày)'] = (df['Ngày hết hạn'] - df['Ngày đăng']).dt.days
        df = df.drop(columns=['public_date', 'expired_date'], errors='ignore')

    # Xử lý cột 'price'
    if 'price' in df.columns:
        df['Giá phòng (triệu/tháng)'] = df['price'].apply(convert_price)
        df = df.dropna(subset=['Giá phòng (triệu/tháng)'])
        df = df.drop(columns=['price'], errors='ignore')

    # Loại bỏ các cột không cần thiết
    df = df.drop(columns=['description', 'phone_number', 'title', 'address', 'link'], errors='ignore')

    # Việt hóa các cột còn lại
    column_mapping = {
        'acreage': 'Diện tích (m²)',
        'hashtag': 'Hashtag',
        'package': 'Gói tin',
        'category': 'Loại phòng',
        'published_hours': 'Thời gian đăng (giờ trước)'
    }
    df.rename(columns=column_mapping, inplace=True)

    # Đẩy các cột địa chỉ lên đầu
    address_columns = ['Đường', 'Phường', 'Quận/Huyện', 'Thành phố']
    other_columns = [col for col in df.columns if col not in address_columns]
    df = df[address_columns + other_columns]

    # Lưu dữ liệu đã xử lý
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "phongtro_processed.csv")
    df.to_csv(output_path, index=False)
    print(f"Dữ liệu đã được xử lý và lưu vào {output_path}.")

def convert_price(value):
    """
    Chuẩn hóa giá trị giá phòng
    """
    if pd.isna(value):
        return np.nan
    elif "triệu/tháng" in value:
        return float(value.replace(" triệu/tháng", ""))
    elif "đồng/tháng" in value:
        return float(value.replace(" đồng/tháng", "").replace(".", "")) / 1_000_000
    elif "Thỏa thuận" in value:
        return np.nan
    return np.nan

if __name__ == "__main__":
    process_data()
