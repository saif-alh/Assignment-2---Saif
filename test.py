# test.py

from classes import EBook, ShoppingCart, Customer, PremiumCustomer, Order, Invoice, EbookStore

def test_ebook_creation():
    # Creating some eBooks related to self-improvement and habit-building
    ebook1 = EBook("Atomic Habits", "James Clear", "2018", "Self-Help", 18.99)
    ebook2 = EBook("The Power of Habit", "Charles Duhigg", "2012", "Psychology", 15.99)
    ebook3 = EBook("Tiny Habits", "BJ Fogg", "2020", "Self-Help", 20.99)
    print(ebook1)
    print(ebook2)
    print(ebook3)
    return [ebook1, ebook2, ebook3]

def test_shopping_cart_operations():
    # Creating a shopping cart and adding/removing eBooks
    cart = ShoppingCart()
    ebooks = test_ebook_creation()

    # Adding items to the cart
    cart.add_item(ebooks[0])  # Adding "Atomic Habits"
    cart.add_item(ebooks[1])  # Adding "The Power of Habit"
    print("Shopping Cart after adding items:", cart)

    # Removing an item
    cart.remove_item(ebooks[0])  # Removing "Atomic Habits"
    print("Shopping Cart after removing an item:", cart)
    return cart

def test_customer_creation():
    # Creating a standard and a premium customer
    customer = Customer("Saif", "20222074@zu.ac.ae", "555-1234", "Standard")
    premium_customer = PremiumCustomer("Ahmed", "202221113@zu.ac.ae", "555-5678", "Premium", discount_rate=0.1, loyalty_points=150)

    print(customer)
    print(premium_customer)
    return customer, premium_customer

def test_order_and_invoice():
    # Creating an order and generating an invoice for a customer’s shopping cart
    ebooks = test_ebook_creation()
    cart = ShoppingCart()
    
    # Adding items to the cart
    cart.add_item(ebooks[0])  # Adding "Atomic Habits"
    cart.add_item(ebooks[1])  # Adding "The Power of Habit"
    
    # Creating an order with a discount (e.g., premium customer discount)
    order = Order(order_id=1, items=cart._items, discount=0.1)  # 10% discount
    print(order)

    # Generating an invoice for the order
    invoice = Invoice(invoice_id=1001, order=order)
    print(invoice)

def test_ebookstore_operations():
    # Testing EbookStore functionality
    store = EbookStore("Self-Help", "Penguin", "English", 2023)
    ebooks = test_ebook_creation()

    # Adding e-books to the store
    store.add_ebook(ebooks[0])
    store.add_ebook(ebooks[1])
    store.add_ebook(ebooks[2])

    print("EbookStore after adding e-books:", store)
    print("List of e-books in store:", store.list_ebooks())

    # Removing an e-book
    store.remove_ebook(ebooks[1])
    print("EbookStore after removing an e-book:", store)
    print("Updated list of e-books in store:", store.list_ebooks())

# Running the tests
print("EBook Creation:")
test_ebook_creation()

print("\nShopping Cart Operations:")
test_shopping_cart_operations()

print("\nCustomer Creation:")
test_customer_creation()

print("\nOrder and Invoice Generation:")
test_order_and_invoice()

print("\nEbookStore Operations:")
test_ebookstore_operations()