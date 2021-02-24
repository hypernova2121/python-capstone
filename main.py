from customer import Customer
from order import Order
from orderlineitem import OrderLineItem


class Program:

    def main(self):
        #Program starts here
        print('Welcome to the Python order processor!')
        customer = self.get_customer_info()
        order = self.get_order_info()
        summary = order.order_summary(customer)
        print (summary)
         
    def get_customer_info(self):
        print('\nEnter customer information:')

        firstName = input('Enter first name: ')
        while not firstName.isalpha():
            firstName = input('*ERROR* Enter valid first name: ')

        lastName = input('Enter last name: ')
        while not lastName.isalpha():
            lastName = input('*ERROR* Enter valid last name: ')

        emailAddress = input('Enter email address: ')
        while '@' not in emailAddress: #very simple email validation
            emailAddress = input('*ERROR* Enter valid email address: ')
        return Customer(firstName, lastName, emailAddress)

    def get_order_info(self):
        print('\nEnter order information:')
        orderNumber = input('Enter the order number: ')
        while not orderNumber.isnumeric():
            orderNumber = input('*ERROR* Enter valid order number: ')
        itemDescription = input('Enter the item description: ')
        while itemDescription == '':
            itemDescription = input('*ERROR* Enter the item description: ')

        OLIs = []
        OLIcounter = 0
        while OLIcounter < 1:
            try:
                OLIcounter = int(input("How many Order Line Items?: "))
            except ValueError:
                pass
            if OLIcounter < 1:
                print("*ERROR* Must have at least one Order Line Item!")

        for i in range(OLIcounter):
            partNumber = 0
            while partNumber < 1:
                try:
                    partNumber = int(input("What is the part number?: "))
                except ValueError:
                    pass
                if partNumber < 1:
                    print("*ERROR* Enter valid part number!")

            unitCost = 0
            while unitCost < 1:
                try:
                    unitCost = float(input("What is the unit cost?: "))
                except ValueError:
                    pass
                if unitCost <= 0:
                    print("*ERROR* Enter valid unit cost!")

            quantity = 0
            while quantity < 1:
                try:
                    quantity = int(input("What is the quantity?: "))
                except ValueError:
                    pass
                if quantity < 1:
                    print("*ERROR* Enter valid quantity!")

            OLIs.append(OrderLineItem(partNumber, unitCost, quantity))
        return Order(orderNumber, itemDescription, OLIs)
    

if __name__ == '__main__':
    program = Program()
    program.main()