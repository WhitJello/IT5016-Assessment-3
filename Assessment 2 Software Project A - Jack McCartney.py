counter = 10000
staff_dict = {'date': '01/01/1999', 'staff_ID': 'AA00', 'staff_name': 'John Smith', 'req_ID': 0}
total_price = 0
status = 'N/A'
reference_number = 'N/A'

def staff_info():
    staff_dict['date'] = input('Please enter the current date using DD/MM/YYYY: ')
    staff_dict['staff_ID'] = input('Please enter your Staff ID: ')
    staff_dict['staff_name'] = input('Please enter your full name: ')
    global counter
    counter += 1 
    staff_dict['req_ID'] = counter
    print('Date: ' + staff_dict['date'] + '    Staff ID: ' + staff_dict['staff_ID'] + '    Staff Name: ' + staff_dict['staff_name'] + '    Requisiton ID: ' + str(staff_dict['req_ID']))
    return staff_dict


def requisitions_total():
    staff_info()
    i = 'y'
    item_list = []
    item_price = []
    while i == 'y':
        item_list.append(input('Please enter the name of the requisition item: '))
        item_price.append(int(input('Please enter the price of the item. Please only enter whole numbers: ')))
        i = input('Enter "y" to add another item, enter anything else to stop adding items: ')
    
    ticker = 0
    global total_price
    for x in item_list:
        print(item_list[ticker]+ ': $' +str(item_price[ticker]))
        total_price += item_price[ticker]
        ticker += 1
    print('Total Price: $'+ str(total_price))


def requisitions_approval(dict):
    requisitions_total()
    global status
    global reference_number
    status = 'Pending'
    if total_price >= 500:
        status = 'Pending'
    elif total_price < 500:
        status = 'Approved'
    
    reference_number = dict['staff_ID'] + str(dict['req_ID'])[-3:]
    print('Total: $' + str(total_price) + '    Status: ' + status + '    Approval Reference Number: '+ reference_number)

    
    

def display_requisitions(dict, price, approval_status, reference):
    print('Date: ' + dict['date'] + '    Requisiton ID: ' + str(staff_dict['req_ID']) + '    Staff ID: ' + staff_dict['staff_ID'] + '    Staff Name: ' + staff_dict['staff_name'] + '   Price Total: $' + str(price) + '    Status: ' + approval_status + '    Approval Reference Number: ' + reference)

requisitions_approval(staff_dict)

display_requisitions(staff_dict, total_price, status, reference_number)
