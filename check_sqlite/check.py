import sqlite3

# Kết nối với cơ sở dữ liệu SQLite
conn = sqlite3.connect("database.sqlite3")

# Tạo đối tượng cursor để thực thi các câu lệnh SQL
cursor = conn.cursor()

# Thực thi câu lệnh SELECT để lấy tất cả các dòng từ bảng 'user' (thay bằng tên bảng của bạn)
cursor.execute("SELECT * FROM user")

# Lấy tất cả kết quả trả về
rows = cursor.fetchall()

# In ra các kết quả
for row in rows:
    print(row)



# Đóng kết nối
conn.close()
