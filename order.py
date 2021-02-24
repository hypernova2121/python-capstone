class Order:
    def __init__(self, order_number, description, orderlineitems):
        self.order_number = order_number
        self.description = description
        self.orderlineitems = orderlineitems
    
    def order_summary(self, customer):
        subtotal = 0
        total = 0
        summary = f'\n\nInvoice for Order Number {self.order_number}:\n'
        summary += f'\n\nCustomer Name: {customer.first_name} {customer.last_name}'

        if self.orderlineitems != None:
            for i in range(len(self.orderlineitems)):
                summary += '\nOrder Line Item ' + str(i+1) + ': '
                summary += f'\nPart Number: {self.orderlineitems[i].part_number}'
                summary += f'\nUnit Cost: {self.orderlineitems[i].unit_cost}'
                summary += f'\nItem Quantity: {self.orderlineitems[i].quantity_num}\n'

                subtotal += (self.orderlineitems[i].quantity_num * self.orderlineitems[i].unit_cost)

            subtotal = round(subtotal, 2)
            total = round((subtotal * 1.075),2)
            summary += f'\nSub-total: {subtotal}'
            summary += f'\nTotal: {total}'

            return (summary)

        else:
            return ('NOTHING ORDERED, ABORTING')
