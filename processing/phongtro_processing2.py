import pandas as pd

def clean_column(dataframe, column_name, patterns, replacement=""):
    
    if column_name in dataframe.columns:
        for pattern in patterns:
            dataframe[column_name] = dataframe[column_name].str.replace(pattern, replacement, regex=True).str.strip()
    return dataframe

def remove_rows_with_value(dataframe, column_name, value_to_remove):
    
    if column_name in dataframe.columns:
        dataframe = dataframe[dataframe[column_name] != value_to_remove]
    return dataframe

def process_data(file_path, output_path):

    # Đọc file CSV
    df = pd.read_csv(file_path)

    # Làm sạch cột "Đường"
    df = clean_column(df, 'Đường', ["Địa chỉ: ", r"\bĐường\b"])

    # Làm sạch cột "Phường"
    df = clean_column(df, 'Phường', [r"\bPhường\b", r"Quận|Huyện"])

    # Làm sạch cột "Quận/Huyện"
    df = clean_column(df, 'Quận/Huyện', [r"\bQuận\b"])

    # Làm sạch cột "Thành phố"
    df = clean_column(df, 'Thành phố', ["Thành phố"])

    # Xóa các dòng có giá trị "Không rõ" ở cột "Thành phố"
    df = remove_rows_with_value(df, 'Thành phố', "Không rõ")

    # Lưu kết quả vào file CSV mới
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"Dữ liệu đã được xử lý và lưu vào: {output_path}")

# Gọi hàm xử lý dữ liệu
if __name__ == "__main__":
    input_file = "output/phongtro_processed.csv"  # Đường dẫn file đầu vào
    output_file = "output/output_cleaned.csv"    # Đường dẫn file đầu ra
    process_data(input_file, output_file)
