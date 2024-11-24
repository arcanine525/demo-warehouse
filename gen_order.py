import json
import random

from datetime import date, timedelta


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



products = load_json_file("data/unit_price.json")
customers = load_json_file("data/customer.json")
payments = load_json_file("data/payment.json")
stores = load_json_file("data/store.json")

# --- Generate data for FactTransactionHeader ---
def generate_transaction_header(trans_header_id):
    store = random.choice(stores)
    customer = random.choice(customers)
    payment = random.choice(payments)

    # Generate random date within a year
    start_date = date(2023, 1, 1)
    end_date = date(2023, 11, 20)
    random_days = random.randrange((end_date - start_date).days)
    trans_date = start_date + timedelta(days=random_days)

    return {
        "TransHeaderID": trans_header_id,
        "StoreID": store["StoreID"],
        "CustID": customer["CustID"],
        "PaymentID": payment["PaymentID"],
        "TransDate": trans_date.strftime("%Y-%m-%d"),
        "TotalCost": 0  # Placeholder, will be calculated later
    }


# --- Generate data for FactTransactionItem ---
def generate_transaction_item(trans_record_id, trans_header_id, trans_date):
    product = random.choice(products)
    quantity = random.randint(1, 5)

    # Get unit price from DimProductUnitPrice
    unit_price = product["UnitPrice"]
    cost = quantity * unit_price

    return {
        "TransRecordID": trans_record_id,
        "TransHeaderID": trans_header_id,
        "ProductID": product["ProductID"],
        "Quantity": quantity,
        "Cost": cost,
        "TransDate": trans_date
    }

# --- Main execution ---
fact_transaction_header = []
fact_transaction_item = []
trans_header_id = 1
trans_record_id = 1

transaction_numbers = 10000
for i in range(transaction_numbers):  # Generate transactions
    header = generate_transaction_header(trans_header_id)
    fact_transaction_header.append(header)

    # Generate 1-3 items per transaction
    num_items = random.randint(1, 4)
    for _ in range(num_items):
        item = generate_transaction_item(trans_record_id, trans_header_id, header["TransDate"])
        fact_transaction_item.append(item)
        header["TotalCost"] += item["Cost"]  # Update total cost in header
        trans_record_id += 1

    trans_header_id += 1

# Save data as JSON
with open("fact_transaction_header.json", "w", encoding="utf-8") as f:
    json.dump(fact_transaction_header, f, ensure_ascii=False, indent=4)

with open("fact_transaction_item.json", "w", encoding="utf-8") as f:
    json.dump(fact_transaction_item, f, ensure_ascii=False, indent=4)


# import json
# import csv

# def json_to_csv(json_data, csv_filename):
#     """Converts a JSON array to a CSV file.

#     Args:
#         json_data: The JSON array containing the data.
#         csv_filename: The name of the CSV file to be created.
#     """

#     try:
#         # Get the header row from the keys of the first JSON object
#         header = json_data[0].keys()

#         with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
#             writer = csv.DictWriter(csvfile, fieldnames=header)

#             # Write  the header row
#             writer.writeheader()

#             # Write the data rows
#             for row in json_data:
#                 writer.writerow(row)

#         print(f"CSV file '{csv_filename}' created successfully.")

#     except (IndexError, ValueError) as e:
#         print(f"Error creating CSV: {e}")


# json_to_csv(fact_transaction_header, "fact_transaction_header.csv")
# json_to_csv(fact_transaction_item, "fact_transaction_item.csv")
