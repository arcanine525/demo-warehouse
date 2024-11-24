import json
import random

import unicodedata
import uuid

def remove_vietnamese_signs(text):
    """Removes Vietnamese diacritics (signs) from a given text.

    Args:
        text: The input text containing Vietnamese characters.

    Returns:
        The text with Vietnamese diacritics removed.
    """
    normalized_text = unicodedata.normalize('NFD', text)
    output = ''.join([c for c in normalized_text if not unicodedata.combining(c)])
    return output


def load_json_file(filepath):
    """Loads a JSON file and returns the corresponding Python object.

    Args:
      filepath: The path to the JSON file.

    Returns:
      A Python object representing the data in the JSON file.
    """

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filepath}'.")
        return None

districts = load_json_file("data/disctrict.json")



# Generate data for DimCustomer
def generate_customer_data(cust_id):
    first_names = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Vũ", "Đặng", "Bùi", "Ngô", "Dương"]
    middle_names = ["Văn", "Thị", "Hữu", "Thế", "Kim", "Mỹ", "Xuân", "Thu", "Đông", "Hạ"]
    last_names = ["An", "Bình", "Cường", "Diễm", "Em", "Phương", "Giang", "Hà", "Minh", "Kim",
                  "Nam", "Oanh", "Phong", "Quỳnh", "Sơn", "Thảo", "Trung", "Vân", "Xuân", "Yến",
                  "Bình", "Cúc", "Đức", "Giang", "Hải", "Hoa", "Hưng", "Huyền", "Khánh", "Lan",
                  "Long", "Mai", "Minh", "Ngọc", "Quân", "Dung", "Đức", "Hương", "Linh", "Ly",
                  "Ngân", "Nhi", "Như", "Phúc", "Quang", "Quyên", "Sang", "Thắng", "Thịnh", "Tú",
                  "Uyên", "Vinh", "Vy", "Dũng", "Kiên", "Kiệt", "Khang", "Khôi", "Lâm", "Lộc",
                  "Luân", "Mạnh", "Nghĩa", "Nhân", "Phi", "Phúc", "Phượng", "Quỳnh", "Tân", "Thái",
                  "Thành", "Thiên", "Thủy", "Tiến", "Trang", "Trí", "Tuấn", "Tuyền", "Vũ", "Duy",
                  "Khoa", "Khương", "Liên", "Loan", "Lợi", "Nam", "Nga", "Nghi", "Nhật", "Phương",
                  "Quân", "Tâm", "Thư", "Trâm", "Tuyết", "Vân", "Việt", "Yên"]
    streets = ["Lê Lợi", "Nguyễn Huệ", "Võ Văn Kiệt", "Trần Phú", "Lý Thường Kiệt", "Nguyễn Văn Linh",
               "Hoàng Diệu", "Lê Hồng Phong", "Trần Hưng Đạo", "Nguyễn Trãi", "Pasteur", "Hai Bà Trưng",
               "Nguyễn Đình Chiểu", "CMT8", "Võ Thị Sáu", "Điện Biên Phủ", "Nguyễn Du", "Cách Mạng Tháng 8",
               "Đồng Khởi", "Lê Thánh Tôn", "Nguyễn Thị Minh Khai", "Tôn Đức Thắng", "Hàm Nghi", "Hồ Tùng Mậu",
               "Nam Kỳ Khởi Nghĩa", "Nguyễn Bỉnh Khiêm", "Trần Quang Khải", "Cô Giang", "Cô Bắc", "Đề Thám",
               "Phạm Ngũ Lão", "Yersin", "Bùi Viện", "Thủ Khoa Huân"]


    # Get random district from the provided list
    district = random.choice(districts)
    district_id = district["DistrictID"]
    district_name = district["DistrictName"]  # Get district name for address


    first_name = random.choice(first_names)
    middle_name = random.choice(middle_names)
    last_name = random.choice(last_names)

    email_name  = remove_vietnamese_signs(f"{first_name.lower()}.{last_name.lower()}")
    rand = random.randint(1, 12)
    if rand < 6:
        email_name = f"{email_name}.{str(uuid.uuid1())[0:rand]}"

    email_providers = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
    email = f"{email_name}@{random.choice(email_providers)}"

    address = f"{random.randint(1, 1000)} {random.choice(streets)}, {district_name}"
    gender = random.choice(["M", "F", "O"])
    dob = f"{random.randint(1970, 2006)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    bio = random.choice(["Thích đọc sách", "Thích nấu ăn", "Yêu âm nhạc", "Thích du lịch", "Mê thể thao",
                         "Yêu nghệ thuật", "Mê lịch sử", "Thích ăn uống", "Thích chơi game", "Thích xem phim"])

    if middle_name == "Thị":
        gender = "F"


    return {
        "CustID": cust_id,
        "DistrictID": district_id,
        "CustName": f"{first_name} {middle_name} {last_name}",
        "CustEmail": email,
        "CustAddress": address,
        "CustGender": gender,
        "CustDOB": dob,
        "CustBio": bio
    }

# Create a list of customers
customers = []
for i in range(1, 567):
    customers.append(generate_customer_data(i))  # DistrictID 1 is Quận 1

# Save data as JSON
with open("dim_customer_quan1.json", "w", encoding="utf-8") as f:
    json.dump(customers, f, ensure_ascii=False, indent=4)
