import random
from datetime import datetime, timedelta

# Function to generate a random date between start_date and end_date
def random_date(start_date, end_date):
    return start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )

# Function to generate a random description based on the fault type
def generate_description(fault_type):
    descriptions = {
        'RAM': ['Memory Corruption', 'Bad RAM Modules', 'Incorrect RAM Configuration', 'Overheating', 'Incompatible RAM', 'Driver Issues', 'Memory Leaks', 'Software Bugs', 'File System Corruption', 'Voltage Issues'],
        'CPU': ['Power Supply Issues', 'CPU Socket Problems', 'BIOS/UEFI Incompatibility', 'Driver Issues', 'Hardware Malfunctions', 'Burned or Damaged Circuits', 'Faulty Transistors', 'Soldering Issues', 'Cracked or Bent Pins', 'Manufacturing Defects'],
        'Motherboard': ['BIOS Errors', 'Faulty Capacitors', 'CMOS Battery Failure', 'Connection Issues', 'USB Port Failures', 'Ethernet and Internet Connectivity Problems', 'Physical Damage', 'Burned or Damaged Circuits', 'Short Circuits', 'Faulty Capacitors', 'Broken Traces', 'Damaged Slots or Connectors', 'Manufacturing Defects'],
        'Powersupply': ['Overheating', 'Voltage Fluctuations', 'Power Surges', 'Capacitor Failure', 'Wiring Issues'],
        'Graphicscard': ['Graphic Artifacts', 'Driver Issues', 'Overheating', 'VRAM Failure', 'GPU Fan Failure', 'Connection Problems'],
        'Harddrive': ['Bad Sectors', 'Disk Not Detected', 'Slow Performance', 'Boot Failures', 'Data Corruption', 'Firmware Issues', 'Physical Damage', 'Aging and Wear'],
        'ExternalCPU': ['Overheating', 'Fan Failure', 'Power Supply Issues', 'Connection Problems', 'Slow Performance']
    }
    return random.choice(descriptions[fault_type])

# Set the range of computer IDs
computer_ids = list(range(51, 71))

# Set the range of dates
start_date = datetime(2010, 1, 1)
end_date = datetime(2023, 1, 1)

# Number of records to generate
num_records = 100

# Generate random data and print in SQL insert format
for _ in range(num_records):
    report_date = random_date(start_date, end_date).strftime('%Y-%m-%d')
    year = int(report_date.split('-')[0])

    # Set the status to "solved" if the year is between 2010 and 2020
    status = 'solved' if 2010 <= year <= 2020 else random.choice(['pending', 'waiting','solved'])

    computer_id = random.choice(computer_ids)
    fault_type = random.choice(['RAM', 'CPU', 'Motherboard', 'Powersupply', 'Graphicscard', 'Harddrive', 'ExternalCPU'])
    description = generate_description(fault_type)

    print(f"INSERT INTO faultreport (ReportDate, Status, ComputerID, FaultType, Description) "
          f"VALUES ('{report_date}', '{status}', {computer_id}, '{fault_type}', '{description}');")
