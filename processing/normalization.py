import pandas as pd
import numpy as np

# Từ điển để chuẩn hóa
DICTIONARY = {
    'Quận/Huyện': ['Quận', 'Huyện', 'Thành phố'],
    'Thành phố': ['Thành phố', 'Tỉnh'],
    'Phường': ['P.', 'Phường', 'Thị trấn', 'Xã'],
    'Đường': ['Đường', 'Phố', 'Số']
}

def normalize_value(value, valid_keywords):
    """
    Chuẩn hóa giá trị bằng cách kiểm tra từ khóa hợp lệ
    """
    if pd.isna(value) or value.strip() == "":
        return np.nan
    for keyword in valid_keywords:
        if keyword in value:
            return value.strip()  # Xóa khoảng trắng thừa
    return np.nan  # Loại bỏ giá trị không hợp lệ

def assign_city(row):
    """
    Gán giá trị 'Thành phố' nếu thông tin bị thiếu
    """
    if pd.isna(row['Thành phố']) or row['Thành phố'].strip() == "":
        if "Quận" in str(row['Quận/Huyện']) or "Huyện" in str(row['Quận/Huyện']):
            return "Thành phố Hồ Chí Minh"  # Ví dụ gán mặc định
        return "Không rõ"  # Gán giá trị mặc định nếu không có thông tin
    return row['Thành phố']

def standardize_address(df):
    """
    Chuẩn hóa từng cột địa chỉ trong DataFrame
    """
    # Chuẩn hóa các cột địa chỉ
    df['Đường'] = df['Đường'].apply(lambda x: normalize_value(x, DICTIONARY['Đường']))
    df['Phường'] = df['Phường'].apply(lambda x: normalize_value(x, DICTIONARY['Phường']))
    df['Quận/Huyện'] = df['Quận/Huyện'].apply(lambda x: normalize_value(x, DICTIONARY['Quận/Huyện']))
    df['Thành phố'] = df['Thành phố'].apply(lambda x: normalize_value(x, DICTIONARY['Thành phố']))

    # Chỉ gán giá trị mặc định cho 'Thành phố' khi thông tin bị thiếu
    df['Thành phố'] = df.apply(assign_city, axis=1)
    return df

def main():
    # Đường dẫn tới file JSON
    file_path = '../PhanTichDinhLuong/spiders/phongtro.json'
    try:
        # Đọc dữ liệu từ file JSON
        df = pd.read_json(file_path, lines=True)
    except Exception as e:
        print(f"Lỗi khi đọc file JSON: {e}")
        return

    # Tách cột 'address' thành các cột riêng biệt
    if 'address' in df.columns:
        df[['Đường', 'Phường', 'Quận/Huyện', 'Thành phố']] = df['address'].str.split(',', n=3, expand=True)
        df[['Đường', 'Phường', 'Quận/Huyện', 'Thành phố']] = df[['Đường', 'Phường', 'Quận/Huyện', 'Thành phố']].apply(lambda x: x.str.strip())

    # Chuẩn hóa dữ liệu địa chỉ
    df_cleaned = standardize_address(df)

    # Lưu dữ liệu đã chuẩn hóa
    output_path = "output/phongtro_cleaned.csv"
    df_cleaned.to_csv(output_path, index=False)
    print(f"Dữ liệu đã được chuẩn hóa và lưu vào {output_path}.")

if __name__ == "__main__":
    main()
