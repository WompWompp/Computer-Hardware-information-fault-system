# Initialize an empty list to store SQL insert statements
import random

sql_insert_statements_motherboard = []

# Set the range of motherboard IDs
motherboard_ids = list(range(1, 51))

# Mapping of brands to models
brand_models = {
    'ASUS': 'Prime B450',
    'Gigabyte': 'Aorus X570',
    'MSI': 'Tomahawk B550',
}

# Generate SQL insert statements for the Motherboard table
for motherboard_id in motherboard_ids:
    # Choose a brand randomly from the available options
    brand = random.choice(list(brand_models.keys()))
    model = brand_models[brand]

    # Append SQL insert statements for the Motherboard table
    sql_insert_statements_motherboard.append(
        f"INSERT INTO motherboard (MotherboardID, Brand, Model) "
        f"VALUES ({motherboard_id}, '{brand}', '{model}');"
    )

# Print all the SQL insert statements for the Motherboard table
for statement in sql_insert_statements_motherboard:
    print(statement)
