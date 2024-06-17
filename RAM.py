import random


# Initialize an empty list to store SQL insert statements
sql_insert_statements_ram = []

# Set the range of RAM IDs
ram_ids = list(range(51, 1001))

# Available brands, CL values, capacities, and speeds
ram_brands = ['Corsair', 'Kingston', 'Crucial']
cl_values = [16, 18, 14]
capacities = [16, 32, 64]
speeds = [2400, 3000, 3200, 3600, 4000]

# Generate SQL insert statements for the RAM table
for ram_id in ram_ids:
    # Choose random brand, CL value, capacity, and speed
    brand = random.choice(ram_brands)
    cl_value = random.choice(cl_values)
    capacity = random.choice(capacities)
    speed = random.choice(speeds)

    # Append SQL insert statements for the RAM table
    sql_insert_statements_ram.append(
        f"INSERT INTO ram (RAMID, Brand, CLValue, Capacity, Speed) "
        f"VALUES ({ram_id}, '{brand}', {cl_value}, {capacity}, {speed});"
    )

# Print all the SQL insert statements for the RAM table
for statement in sql_insert_statements_ram:
    print(statement)
