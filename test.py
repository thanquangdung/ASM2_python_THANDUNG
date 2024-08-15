import pandas as pd
file_path = 'CustomerTable.csv'  # Đường dẫn đến tệp CSV của bạn
customer_df = pd.read_csv(file_path)  # Đọc tệp CSV vào DataFrame
import matplotlib.pyplot as plt
import pandas as pd

# Giả sử chúng ta đã làm sạch và tải lại file CSV
file_path = 'CustomerTable.csv'
customer_df = pd.read_csv(file_path)


# Đọc dữ liệu từ tệp CSV 1
df = pd.read_csv('CustomerTable.csv')

# Kiểm tra các hàng trùng lặp
duplicate_rows = customer_df[customer_df.duplicated()]

# Hiển thị các hàng trùng lặp nếu có
if not duplicate_rows.empty:
    print("Các hàng trùng lặp được tìm thấy:")
    print(duplicate_rows)
else:
    print("Không có hàng trùng lặp.")


import re

# Các mẫu regex đơn giản để xác thực
email_pattern = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_pattern = r'^\+?\d[\d -]{7,}\d$'  # Định dạng quốc tế và địa phương
postal_pattern = r'^\d{4,10}$'  # Giả sử mã bưu điện là số và có độ dài từ 4 đến 10 chữ số

# Áp dụng xác thực
invalid_emails = customer_df[~customer_df['Email'].apply(lambda x: bool(re.match(email_pattern, x)))]
invalid_phone_numbers = customer_df[~customer_df['PhoneNumber'].apply(lambda x: bool(re.match(phone_pattern, x)))]
invalid_postal_codes = customer_df[~customer_df['PostalCode'].apply(lambda x: bool(re.match(postal_pattern, str(x))))]

# Hiển thị kết quả
print("Email không hợp lệ:\n", invalid_emails)
print("\nSố điện thoại không hợp lệ:\n", invalid_phone_numbers)
print("\nMã bưu điện không hợp lệ:\n", invalid_postal_codes)


# Remove invalid phone numbers
customer_df_cleaned = customer_df[customer_df['PhoneNumber'].apply(lambda x: bool(re.match(phone_pattern, x)))]

# Display the cleaned DataFrame
customer_df_cleaned.head()


# Remove the record with the invalid postal code
customer_df_cleaned = customer_df_cleaned[customer_df_cleaned['PostalCode'].apply(lambda x: bool(re.match(postal_pattern, str(x))))]

# Display the cleaned DataFrame
customer_df_cleaned.head()


# Save the cleaned data to a new CSV file
cleaned_file_path = '/mnt/data/Cleaned_CustomerTable.csv'
customer_df_cleaned.to_csv(cleaned_file_path, index=False)

cleaned_file_path



























