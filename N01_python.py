import pandas as pd
import matplotlib.pyplot as plt
# Đọc dữ liệu từ các sheet
df_san_pham = pd.read_excel('DuLieuThucHanh2_N01.xlsx', sheet_name='San Pham')
df_nhan_vien = pd.read_excel('DuLieuThucHanh2_N01.xlsx', sheet_name='Nhan Vien')
df_hoa_don = pd.read_excel('DuLieuThucHanh2_N01.xlsx', sheet_name='Hoa Don')
df_thong_tin = pd.read_excel('DuLieuThucHanh2_N01.xlsx', sheet_name='Thong Tin Hoa Don')

# Hiển thị 4 DataFrame
print("DataFrame df_san_pham:")
# Cập nhật các giá trị rỗng thành giá trị mặc định (ở đây là 0)
df_san_pham = df_san_pham.fillna(0)
print(df_san_pham)
print("\nDataFrame df_nhan_vien:")
# Cập nhật các giá trị rỗng thành giá trị mặc định (ở đây là 0)
df_nhan_vien = df_nhan_vien.fillna('')
print(df_nhan_vien)
print("\nDataFrame df_hoa_don:")
# Cập nhật các giá trị rỗng thành giá trị mặc định (ở đây là 0)
df_hoa_don = df_hoa_don.fillna('')
print(df_hoa_don)
print("\nDataFrame df_thong_tin:")
# Cập nhật các giá trị rỗng thành giá trị mặc định (ở đây là 0)
df_thong_tin = df_thong_tin.fillna(0)
print(df_thong_tin)

# Giả sử df_thongtin là DataFrame chứa thông tin sản phẩm và số lượng bán
# Tạo DataFrame mới cho bán hàng
df_san_pham_thay_the = df_san_pham[['ID San Pham', 'Ten']]
df_thong_tin_thay_the = df_thong_tin[['ID San Pham', 'So Luong']]
df_ban_hang = pd.merge(df_san_pham_thay_the, df_thong_tin_thay_the, on='ID San Pham', how='inner')
df_ban_hang = df_ban_hang[['ID San Pham', 'Ten', 'So Luong']]
df_ban_hang = df_ban_hang.groupby('ID San Pham').agg({'Ten': 'first', 'So Luong': 'sum'}).reset_index()
# Bỏ cột 'ID San Pham' ra khỏi DataFrame
df_ban_hang = df_ban_hang.drop(columns=['ID San Pham'])
# In ra DataFrame bán hàng
print("DataFrame Bán Hàng:")
print(df_ban_hang)

# Tìm sản phẩm bán chạy nhất
san_pham_ban_chay_nhat = df_ban_hang.loc[df_ban_hang['So Luong'].idxmax()]

# In ra sản phẩm bán chạy nhất
print("\nSản Phẩm Bán Chạy Nhất:")
print(san_pham_ban_chay_nhat.values)

# Tính tổng doanh thu cửa hàng
print("\n Bang Doanh Thu: ")
df_san_pham_1 = df_san_pham[['ID San Pham', 'Gia']]
df_thong_tin_1 = df_thong_tin[['ID San Pham', 'So Luong']]
df_doanh_thu = pd.merge(df_san_pham_1, df_thong_tin_1, on='ID San Pham', how='inner')
df_doanh_thu['Tong Doanh Thu'] = df_doanh_thu['So Luong'] * df_doanh_thu['Gia']
tong_doanh_thu = df_doanh_thu['Tong Doanh Thu'].sum()
print(df_doanh_thu)
print("\nTổng Doanh Thu Cửa Hàng:", tong_doanh_thu)

# Update lại số lượng sản phẩm ở df_san_pham sau khi trừ hết số lượng đã bán trong cửa hàng
df_san_pham['So Luong'] = df_san_pham['So Luong'] - df_ban_hang['So Luong']
print("\nDataFrame df_san_pham sau khi cập nhật số lượng:")
print(df_san_pham)

# Ý e
# Gộp các hàng trùng lặp ID Hoa Don và ID San PHam trong df_thong_tin và update số lượng
df_thong_tin_gop = df_thong_tin.groupby(['ID Hoa Don', 'ID San Pham'], as_index=False)['So Luong'].sum()

# In ra df_thong_tin sau khi gộp
print("\nDataframe df_thong_tin sau khi gộp:")
print(df_thong_tin_gop)

with pd.ExcelWriter('OutputDuLieuThucHanh_N01.xlsx') as writer:
    df_san_pham.to_excel(writer, sheet_name='San Pham', index=False)
    df_nhan_vien.to_excel(writer, sheet_name='Nhan Vien', index=False)
    df_hoa_don.to_excel(writer, sheet_name='Hoa Don', index=False)
    df_thong_tin.to_excel(writer, sheet_name='Thong Tin Hoa Don', index=False)
    df_ban_hang.to_excel(writer, sheet_name='Ban Hang', index=False)
    df_doanh_thu.to_excel(writer, sheet_name='Doanh Thu', index=False)

#vẽ biểu đồ cho df ở ý b
df_ban_hang.plot(kind="bar", x="Ten", y="So Luong")

# Tùy chỉnh biểu đồ
plt.xlabel("Tên sản phẩm")
plt.ylabel("Số lượng")
plt.title("Biểu đồ số lượng sản phẩm bán")
plt.show()

#trong trường hợp này chúng ta có thể chọn biểu đồ cột (bar chart) 
#để hiển thị số lượng sản phẩm đã bán.
# Biểu đồ cột thường được sử dụng để so sánh giá trị của các mục khác nhau.
# Trong trường hợp này, chúng ta có thể so sánh số lượng sản phẩm bán của từng mục Ten sản phẩm.