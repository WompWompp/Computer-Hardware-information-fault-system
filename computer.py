import random
from datetime import datetime, timedelta

# Function to generate a random date between start_date and end_date
def random_date(start_date, end_date):
    return start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )

# Set the range of computer IDs
computer_ids = list(range(804, 1001))

# Set the range of dates
start_date = datetime(2007, 1, 1)
end_date = datetime(2010, 12, 31)

# Number of records to generate
num_records = 200

# Generate random data and print in SQL insert format
for computer_id in computer_ids:
    serial_number = f'SN{random.randint(100000, 999999)}'
    model = random.choice(['Laptop', 'Desktop'])
    purchase_date = random_date(start_date, end_date).strftime('%Y-%m-%d')

    print(f"INSERT INTO computer (ComputerID, SerialNumber, Model, PurchaseDate) "
          f"VALUES ({computer_id}, '{serial_number}', '{model}', '{purchase_date}');")
