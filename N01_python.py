import pandas as pd
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

print("\nDataFrame df_hoadon:")
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

# Ý e
# Gộp các hàng trùng lặp ID Hoa Don và ID San PHam trong df_thong_tin và update số lượng
df_thong_tin_gop = df_thong_tin.groupby(['ID Hoa Don', 'ID San Pham'], as_index=False)['So Luong'].sum()

# In ra df_thong_tin sau khi gộp
print("\nDataframe df_thong_tin sau khi gộp:")
print(df_thong_tin_gop)