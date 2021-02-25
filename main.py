from customer import Customer
from order import Order
from orderlineitem import OrderLineItem


class Program:

    def main(self):
        #Program starts here
        print('Welcome to the Python order processor!')
        customer = self.get_customer_info()
        order = self.get_order_info()
        summary = self.order_summary(customer, order)
        print (summary)
         
    def get_customer_info(self):

        firstName, lastName, emailAddress = '', '', ''
        
        print('\nEnter customer information:')

        while not firstName.isalpha():
            firstName = input('Enter first name: ').title()
        
        while not lastName.isalpha():
            lastName = input('Enter last name: ').title()

        while '@' not in emailAddress:
            emailAddress = input('Enter email address: ')

        return Customer(firstName, lastName, emailAddress)
    
    def get_order_info(self):

        orderNumber, itemDescription = 0, ''

        print('\nEnter order information:')

        while orderNumber <= 0:
            try:
                orderNumber = int(input('Enter order number: '))
            except ValueError:
                pass
        
        while itemDescription == '':
            itemDescription = input('Enter order description: ')

        OLIs = self.get_orderlineitem_info()
        return Order(orderNumber, itemDescription, OLIs)

    def get_orderlineitem_info(self):
        OLI_list = []
        num_of_OLIs = 0
        while num_of_OLIs < 1:
            try:
                num_of_OLIs = int(input("How many Order Line Items (minimum 1)?: "))
            except ValueError:
                pass
        print()

        for i in range(1, num_of_OLIs+1):
            partNumber, unitCost, quantity = 0, 0, 0

            while partNumber < 1:
                try:
                    partNumber = int(input(f"[Order Line Item {i}] Enter part number: "))
                except ValueError:
                    pass

            while unitCost <= 0:
                try:
                    unitCost = float(input(f"[Order Line Item {i}] Enter unit cost: "))
                except ValueError:
                    pass

            while quantity < 1:
                try:
                    quantity = int(input(f"[Order Line Item {i}] Enter quantity: "))
                except ValueError:
                    pass

            OLI_list.append(OrderLineItem(partNumber, unitCost, quantity))

        return OLI_list

    def order_summary(self, customer, order):
        subtotal, total = 0, 0

        summary = '\n\n*************************************'
        summary += f'\n\nInvoice for Order Number {order.order_number}'
        summary += f'\n{order.description}\n'
        summary += f'\nCustomer Name: {customer.first_name} {customer.last_name}  ({customer.email_address})\n'

        for i in range(len(order.orderlineitems)):
            summary += '\nOrder Line Item ' + str(i+1) + ': '
            summary += f'\n\tPart Number: {order.orderlineitems[i].part_number}'
            summary += f'\n\tUnit Cost: ${order.orderlineitems[i].unit_cost:.2f}'
            summary += f'\n\tItem Quantity: {order.orderlineitems[i].quantity_num}\n'

            subtotal += (order.orderlineitems[i].quantity_num * order.orderlineitems[i].unit_cost)

        #subtotal = round(subtotal, 2)
        tax = subtotal * 0.075
        total = round(subtotal*1.075, 2)
        summary += f'\nSub-total: ${subtotal:,.2f}'
        summary += f'\nTax (7.5%): ${tax:,.2f}'
        summary += f'\n\nTotal: ${total:,.2f}'
        summary += '\n\n*************************************'

        return (summary)
        

if __name__ == '__main__':
    program = Program()
    program.main()