import random


# Initialize an empty list to store SQL insert statements
sql_insert_statements_externalcpu = []

# Set the range of ExternalCPU IDs
externalcpu_ids = list(range(1, 51))

# Available brands and models
intel_models = ['i9', 'i7']
amd_models = ['Ryzen 9', 'Ryzen 7']

# Generate SQL insert statements for the ExternalCPU table
for externalcpu_id in externalcpu_ids:
    # Choose random brand
    brand = random.choice(['Intel', 'AMD'])

    # Get model based on the selected brand
    if brand == 'Intel':
        model = random.choice(intel_models)
    else:
        model = random.choice(amd_models)

    # Append SQL insert statements for the ExternalCPU table
    sql_insert_statements_externalcpu.append(
        f"INSERT INTO externalcpu (ExternalCPUID, Brand, Model) "
        f"VALUES ({externalcpu_id}, '{brand}', '{model}');"
    )

# Print all the SQL insert statements for the ExternalCPU table
for statement in sql_insert_statements_externalcpu:
    print(statement)
