import csv

# Function to read the data from the CSV file
def read_inventory(file_path):
    inventory = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            inventory.append(row)
    return inventory

# Function to write the data to the CSV file
def write_inventory(file_path, inventory):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(inventory)

# Function to add a new product to the inventory
def add_product(inventory, product):
    inventory.append(product)

# Function to update the available quantity of a product
def update_quantity(inventory, product_name, new_quantity):
    for product in inventory:
        if product[0] == product_name:
            product[2] = new_quantity
            break

# Function to search for products by name
def search_product(inventory, product_name):
    for product in inventory:
        if product[0] == product_name:
            return product
    return None

# Main program
if __name__ == '__main__':
    file_path = '/c:/Users/sebas/OneDrive/Escritorio/fundamentos test/inventory.csv'
    inventory = read_inventory(file_path)

    # Your code to interact with the inventory goes here

    write_inventory(file_path, inventory)