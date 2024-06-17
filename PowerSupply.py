import random

# Initialize an empty list to store SQL insert statements
sql_insert_statements_powersupply = []

# Set the range of PowerSupply IDs
powersupply_ids = list(range(1, 51))

# Available brands, models, and voltage ranges
brands = ['Corsair', 'EVGA', 'Thermaltake']
models = {
    'Corsair': 'CX550M',
    'EVGA': 'SuperNOVA750',
    'Thermaltake': 'Smart500W'
}
voltage_ranges = {
    'Corsair': '110-240V',
    'EVGA': '100-240V',
    'Thermaltake': '90-240V'
}

# Generate SQL insert statements for the PowerSupply table
for powersupply_id in powersupply_ids:
    # Choose random brand
    brand = random.choice(brands)

    # Get model and voltage based on the selected brand
    model = models[brand]
    voltage = voltage_ranges[brand]

    # Append SQL insert statements for the PowerSupply table
    sql_insert_statements_powersupply.append(
        f"INSERT INTO powersupply (PowerSupplyID, Brand, Model, Voltage) "
        f"VALUES ({powersupply_id}, '{brand}', '{model}', '{voltage}');"
    )

# Print all the SQL insert statements for the PowerSupply table
for statement in sql_insert_statements_powersupply:
    print(statement)
