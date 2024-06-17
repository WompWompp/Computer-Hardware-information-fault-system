import random

# Initialize an empty list to store SQL insert statements
sql_insert_statements_harddrive = []

# Set the range of HDD IDs
hdd_ids = list(range(704, 1001))

# Available brands, capacities, types, and interfaces
brands = ['Toshiba', 'Seagate', 'Samsung']
capacities = [256, 512, 1000]
types = ['HDD', 'SSD']
interfaces = {'HDD': 'SATA', 'SSD': ['SATA', 'NVMe']}

# Generate SQL insert statements for the HardDrive table
for hdd_id in hdd_ids:
    # Choose random values for brand, capacity, type, and interface
    brand = random.choice(brands)
    capacity = random.choice(capacities)
    hdd_type = random.choice(types)

    # For SSDs, choose only from 'NVMe' and 'SATA' for interfaces
    if hdd_type == 'SSD':
        interface = random.choice(interfaces[hdd_type])
    else:
        interface = interfaces[hdd_type]

    # Append SQL insert statements for the HardDrive table
    sql_insert_statements_harddrive.append(
        f"INSERT INTO harddrive (HDDID, Brand, Capacity, Type, Interface) "
        f"VALUES ({hdd_id}, '{brand}', {capacity}, '{hdd_type}', '{interface}');"
    )

# Print all the SQL insert statements for the HardDrive table
for statement in sql_insert_statements_harddrive:
    print(statement)
