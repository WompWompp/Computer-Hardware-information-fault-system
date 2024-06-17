import random

# Initialize an empty list to store SQL insert statements
sql_insert_statements_cpu = []

# Set the range of CPU IDs
cpu_ids = list(range(1, 51))

# Available brands, models, clockspeeds, and core configurations
brands = ['Intel', 'AMD']
intel_models = ['Core i3', 'Core i5', 'Core i7', 'Core i9']
amd_models = ['Ryzen 3', 'Ryzen 5', 'Ryzen 7', 'Ryzen 9']
clockspeeds = {
    'Core i3': '3.4GHz',
    'Core i5': '2.4GHz',
    'Core i7': '2.9GHz',
    'Core i9': '3.0GHz',
    'Ryzen 3': '2.4GHz',
    'Ryzen 5': '3.9 GHz',
    'Ryzen 7': '3.7 GHz',
    'Ryzen 9': '3.4 GHz',
}
cores = {
    'Core i3': 2,
    'Core i5': 4,
    'Core i7': 4,
    'Core i9': 8,
    'Ryzen 3': 4,
    'Ryzen 5': 6,
    'Ryzen 7': 8,
    'Ryzen 9': 16,
}

# Generate SQL insert statements for the CPU table
for cpu_id in cpu_ids:
    # Choose random brand
    brand = random.choice(brands)

    # Get model, clockspeed, and cores based on the selected brand
    if brand == 'Intel':
        model = random.choice(intel_models)
    else:
        model = random.choice(amd_models)

    clockspeed = clockspeeds[model]
    core_count = cores[model]

    # Append SQL insert statements for the CPU table
    sql_insert_statements_cpu.append(
        f"INSERT INTO cpu (CPUID, Brand, Model, ClockSpeed, Cores) "
        f"VALUES ({cpu_id}, '{brand}', '{model}', '{clockspeed}', {core_count});"
    )

# Print all the SQL insert statements for the CPU table
for statement in sql_insert_statements_cpu:
    print(statement)
