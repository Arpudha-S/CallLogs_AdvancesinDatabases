import csv
import random
from faker import Faker

# Initialize Faker instance
fake = Faker('en_IN')

# Create customers.csv
with open('customers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'location', 'age', 'gender'])
    
    for _ in range(200):  # Generate 200 customer records
        name = fake.name()
        location = fake.city()
        age = fake.random_int(min=18, max=80)
        gender = random.choice(['Male', 'Female'])
        writer.writerow([name, location, age, gender])

# Create plans.csv
with open('plans.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['plan_name', 'price'])
    
    plans = ['Basic Plan', 'Standard Plan', 'Premium Plan', 'Family Plan', 'Corporate Plan']
    for plan in plans:
        price = fake.random_int(min=10, max=100) + fake.random.random()
        writer.writerow([plan, round(price, 2)])

# Create date.csv
with open('date.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['date', 'month','year'])
    
    for _ in range(100):  # Generate 100 date records
        day = fake.random_int(min=1, max=30)
        month = fake.random_int(min=1, max=12)
        year = fake.random_int(min=2000, max=2024)
        formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
        writer.writerow([formatted_date, month, year])

# Create callid.csv
with open('call.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([ 'customer_id','plan_id','date_id','duration','cost'])
    
    for _ in range(500):  # Generate 500 date records
        custid = fake.random_int(min=1, max=200)
        planid = fake.random_int(min=1, max=5)
        dateid = fake.random_int(min=1, max=100)
        duration = fake.random_int(min=1, max=50)
        cost = fake.random_int(min=1, max=5)*duration
        writer.writerow([custid, planid, dateid,duration,cost])
