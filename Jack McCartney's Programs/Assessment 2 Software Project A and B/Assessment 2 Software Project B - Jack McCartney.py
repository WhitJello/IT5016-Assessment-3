# Post Analysis Note: This is the second part of the assessment, and it reuses code from the previous part with some changes to include classes and some additional functions
# Post Analysis Note: The addition of comments makes this code significantly easier to understand than the previous part

# Post Analysis Note: Much like Part A, the names for the classes, functions, and variables are all appropriately named and easy to understand what they are for

# Global Variables
counter = 10000
staff_dict = {'date': '01/01/1999', 'staff_ID': 'AA00', 'staff_name': 'John Smith', 'req_ID': 0}
total_price = 0
status = 'N/A'
reference_number = 'N/A'
submitted_reqs = 0
approved_reqs = 0
pending_reqs = 0
not_approved_reqs = 0

# The RequisitionSystem Class storing all of the functions related to it
class RequisitionSystem:

    # The staff_info Function asks the user to input their information, stores it for later, then prints it out for the user to see
    def staff_info():
        staff_dict['date'] = input('Please enter the current date using DD/MM/YYYY: ')
        staff_dict['staff_ID'] = input('Please enter your Staff ID: ')
        staff_dict['staff_name'] = input('Please enter your full name: ')
        global counter
        counter += 1 
        staff_dict['req_ID'] = counter
        print('Date: ' + staff_dict['date'] + '    Staff ID: ' + staff_dict['staff_ID'] + '    Staff Name: ' + staff_dict['staff_name'] + '    Requisiton ID: ' + str(staff_dict['req_ID']))
        return staff_dict

    # requisition_details Function asks the user to input an item, then a price, adds the price to a total, then allows the user to enter another item repeatedly if they wish. 
    # It then prints the items, prices and their total
    def requisitions_details():
        global total_price
        total_price = 0
        i = 'y'
        item_list = []
        item_price = []
        while i == 'y':
            item_list.append(input('Please enter the name of the requisition item: '))
            item_price.append(int(input('Please enter the price of the item. Please only enter whole numbers: ')))
            i = input('Enter "y" to add another item, enter anything else to stop adding items: ')

        ticker = 0
        for x in item_list:
            print(item_list[ticker]+ ': $' +str(item_price[ticker]))
            total_price += item_price[ticker]
            ticker += 1
        print('Total Price: $'+ str(total_price))



    # requisitions_approval Function checks if the total item price from the Requisition Details Function is over 500
    # If it is, sets the status to pending and runs the respond_requisition Function
    # If not, sets status to approved
    # It also adds counters to the requisition variables depending on what status the requisition was assigned
    # Then prints out the completed requisition form
    def requisitions_approval(dict):
        global status
        global reference_number
        global pending_reqs
        global approved_reqs
        global submitted_reqs
        status = 'Pending'
        submitted_reqs += 1
        if total_price >= 500:
            status = 'Pending'
            pending_reqs += 1
            RequisitionSystem.respond_requisition()
        elif total_price < 500:
            status = 'Approved'
            approved_reqs += 1
        
        reference_number = dict['staff_ID'] + str(dict['req_ID'])[-3:]
        print('Total: $' + str(total_price) + '    Status: ' + status + '    Approval Reference Number: '+ reference_number)

    # respond_requisition only runs within requisitions_approval if the total cost is 500 or over
    # It asks for a manager for input to change a pending requisition to something else
    # Entering 'y' sets the status to 'approved', 'n' sets it to 'not approved', any other input keeps the status at 'pending'
    # It also changes the requisition statistics accordingly if the status is changed
    def respond_requisition():
        global status
        global pending_reqs
        global approved_reqs
        global not_approved_reqs
        approval_input = input("This requisition needs to be approved by a manager. If you are the manager, enter 'y' to approve, 'n' to not approve, or anything else if you are not the manager to leave the requisition pending: ")
        if approval_input == 'y':
            status = 'Approved'
            pending_reqs -= 1
            approved_reqs += 1
        elif approval_input == 'n':
            status = 'Not approved'
            pending_reqs -= 1
            not_approved_reqs += 1
    
    # Displays the Requisition Statistics
    def requisition_statistics():
        global submitted_reqs
        global pending_reqs
        global approved_reqs
        global not_approved_reqs
        print('Requisition Statistics\nRequisitions Submitted: '+str(submitted_reqs)+ '\nRequisitions Pending: '+str(pending_reqs)+ '\nRequisitions Approved: '+str(approved_reqs)+ '\nRequisitions Not Approved: '+str(not_approved_reqs))
        


    
    # Displays the user data and the requisition information
    def display_requisitions(dict, price, approval_status, reference):
        print('Date: ' + dict['date'] + '\nRequisiton ID: ' + str(staff_dict['req_ID']) + '\nStaff ID: ' + staff_dict['staff_ID'] + '\nStaff Name: ' + staff_dict['staff_name'] + '\nPrice Total: $' + str(price) + '\nStatus: ' + approval_status + '\nApproval Reference Number: ' + reference)



# This runs through all the functions in order, except for respond_requisition, and requisition_statistics
# It then asks for input if the user wishes to repeat the functions again
j = 'y'
while j == 'y':
    RequisitionSystem.staff_info()
    RequisitionSystem.requisitions_details()
    RequisitionSystem.requisitions_approval(staff_dict)
    RequisitionSystem.display_requisitions(staff_dict, total_price, status, reference_number)
    j = input("Do you or another staff member wish to enter another requisition order? enter 'y' to repeat the requisition process: ")

# Runs requisition_statistics
RequisitionSystem.requisition_statistics()

# Post Analysis Note: Similar to the previous part, there is no unnecessary code and it is kept as simple as possible (D.R.Y. and K.I.S.S.)
# Post Analysis Note: There is also plenty of line breaks, making the code easy to read

# Post Analysis Note: The functions in this code have little to no coupling, meaning they can be run and modified independantly without causing errors.
# Post Analysis Note: This shows good avoidance of the bad practice of Strong coupling in S.T.U.P.I.D.
