import pandas as pd
import numpy as np
import os

def main():
    # Đọc dữ liệu từ file JSON
    try:
        df = pd.read_json('../PhanTichDinhLuong/spiders/phongtro.json', lines=True)
        print("Các cột hiện có trong DataFrame:", df.columns)
    except ValueError as e:
        print(f"Error reading JSON file: {e}")
        df = pd.DataFrame()

    # Xóa các cột không cần thiết
    df = df.drop(columns=['description', 'phone_number', 'title'], errors='ignore')

    # Loại bỏ từ "Địa chỉ: " trong cột 'address'
    df['address'] = df['address'].str.replace("Địa chỉ: ", "", regex=False)

    # Tách cột 'address' thành bốn cột
    df[['Đường', 'Phường', 'Quận/Huyện', 'Thành phố']] = df['address'].str.split(',', n=3, expand=True)
    df = df.drop(columns=['address'], errors='ignore')

    # Xử lý 'public_date' và 'expired_date'
    df['public_date'] = pd.to_datetime(df['public_date'].str.replace(r"^Thứ \w+, ", "", regex=True), format="%H:%M %d/%m/%Y", errors='coerce')
    df['expired_date'] = pd.to_datetime(df['expired_date'].str.replace(r"^Thứ \w+, ", "", regex=True), format="%H:%M %d/%m/%Y", errors='coerce')
    df['duration_days'] = (df['expired_date'] - df['public_date']).dt.days

    # Sắp xếp thứ tự cột
    columns_order = ['Đường', 'Phường', 'Quận/Huyện', 'Thành phố', 'duration_days'] + [col for col in df.columns if col not in ['Đường', 'Phường', 'Quận/Huyện', 'Thành phố', 'duration_days']]
    df = df[columns_order]

    # Đảm bảo thư mục lưu file tồn tại
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Lưu file CSV
    df.to_csv(os.path.join(output_dir, "phongtro_processed_with_duration.csv"), index=False)
    print("Dữ liệu đã xử lý và lưu vào 'output/phongtro_processed_with_duration.csv'.")

    # Kiểm tra sự tồn tại của cột 'ad_type'
    if 'ad_type' in df.columns:
        df['ad_type'] = df['ad_type'].str.replace(", nhà trọ", "", regex=False).str.strip()
        df.to_csv(os.path.join(output_dir, "phongtro_processed_only_phongtro.csv"), index=False)
        print("File 'output/phongtro_processed_only_phongtro.csv' đã được lưu sau khi xử lý 'ad_type'.")
    else:
        print("Cột 'ad_type' không tồn tại. Bỏ qua bước xử lý này.")

    # Xử lý cột 'price'
    df['price'] = df['price'].apply(convert_price) if 'price' in df.columns else np.nan
    df_cleaned = df.dropna(subset=['price'])
    df_cleaned.to_csv(os.path.join(output_dir, "phongtro_price_statistics.csv"), index=False)
    print("Dữ liệu giá đã chuẩn hóa và lưu vào 'output/phongtro_price_statistics.csv'.")

def convert_price(value):
    if pd.isna(value):
        return np.nan
    elif "triệu/tháng" in value:
        return float(value.replace(" triệu/tháng", ""))
    elif "đồng/tháng" in value:
        return float(value.replace(" đồng/tháng", "").replace(".", "")) / 1_000_000
    elif "Thỏa thuận" in value:
        return np.nan
    else:
        return np.nan

if __name__ == "__main__":
    main()
