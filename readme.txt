Build an order processor in Python:
Create a class in Python for Customer that includes properties for first name, last name, and e-mail address
Create a class in Python for OrderLineItem that includes properties for part number, unit cost, and quantity
Create a class in Python for Order that includes properties for order number, description, a Customer reference, a collection of OrderLineItems, a subtotal, and a total
In the console, prompt the user for customer information
Prompt the user for order number and description
Prompt the user for the number of order line items to include on the order
In a loop, prompt the user for detail for the specified number of order line items (part number, unit cost, and quantity for each)
Use the inputs to create new instances of the necessary objects
Calculate order subtotal as the sum of quantity * unit cost for all order line items
Calculate order total to include subtotal plus 7.5% sales tax
Display an invoice in the console including all order details, order line item information, order subtotal, and order total; format totals as currency ($X.XX)
OPTIONAL (for an added challenge): Enforce input validation, continuing to prompt the user for a given input until valid data is provided

test