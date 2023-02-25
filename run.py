import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figures input from the user
    """
    while True:
        print('\nPlease enter sales data from the last market.\n')
        print('Data should be six numbers, separated by commas.\n')
        print('Example: 10,20,30,40,50,60\n')

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(',')
        if validate_data(sales_data):
            print('data valid')
            break
    return sales_data

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f'Exactly 6 values required, you provided {len(values)}'
            )
    except ValueError as e:
        print(f'\nInvalid data: {e}, please try again.\n')
        return False
    
    return True

def calculate_surplus_data(sales_row):
    """
    Compare Sales with stock and calculate the surplus for each item type

    The surplus is defined as the sales figure subtracted from the stock
    - positive surplus indicates waste
    - negative surplus indicates extra made when stock was sold out.
    """
    print('calulating surplus data...\n 2342352352352jdi2o3id2o3ind2\n fwoin4o3i498yr89wy9hd')
    stock = SHEET.worksheet('stock').get_all_values()
    stock_row = stock[-1]
    
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data





def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    update the relevant worksheet with the data provided
    """
    print(f'Updating {worksheet} worksheet...\n')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f'{worksheet} updated successfully...\n')

def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, 'sales')
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, 'surplus')




print('\nHEllo and welcome you to this automation')

main()












"""
def update_sales_worksheet(data):
    print('updating sales...\n')
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print('sales worksheet updated succesfully.\n')


def update_surplus_worksheet(data):
    print('updating surplus data...\n...\n...\n...')
    surplus_worksheet = SHEET.worksheet('surplus')
    surplus_worksheet.append_row(data)
    print('updated surplus worksheet successfully')
"""