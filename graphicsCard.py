import random

# Initialize an empty list to store SQL insert statements
sql_insert_statements_graphicscard = []

# Set the range of GraphicsCard IDs
graphicscard_ids = list(range(1, 51))

# Available brands and models
nvidia_models = ['Nvidia RTX 4090', 'Nvidia RTX 4080', 'Nvidia RTX 3090 Ti', 'Nvidia RTX 3090',
                 'Nvidia RTX 4070 Ti', 'Nvidia RTX 3080 Ti', 'Nvidia RTX 4070', 'Nvidia RTX 3080',
                 'Nvidia RTX 3070', 'Nvidia RTX 4060', 'Nvidia RTX 3060', 'Nvidia RTX 2080 SUPER',
                 'Nvidia GTX 1080 Ti', 'Nvidia RTX 2060', 'Nvidia GTX 1660 Ti', 'Nvidia GTX 1650']

amd_models = ['AMD Radeon RX 6950 XT', 'AMD Radeon RX 6900 XT', 'AMD Radeon RX 5500 XT',
              'AMD Radeon RX 580', 'AMD Radeon RX 570', 'AMD Radeon RX 560']

# Generate SQL insert statements for the GraphicsCard table
for graphicscard_id in graphicscard_ids:
    # Choose random brand
    brand = random.choice(['NVIDIA', 'AMD'])

    # Get model based on the selected brand
    if brand == 'NVIDIA':
        model = random.choice(nvidia_models)
    else:
        model = random.choice(amd_models)

    # Append SQL insert statements for the GraphicsCard table
    sql_insert_statements_graphicscard.append(
        f"INSERT INTO graphicscard (GraphicsCardID, Brand, Model) "
        f"VALUES ({graphicscard_id}, '{brand}', '{model}');"
    )

# Print all the SQL insert statements for the GraphicsCard table
for statement in sql_insert_statements_graphicscard:
    print(statement)
