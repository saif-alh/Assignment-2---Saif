# classes.py

class EBook:
    def __init__(self, title, author, publication_date, genre, price):
        self._title = title
        self._author = author
        self._publication_date = publication_date
        self._genre = genre
        self._price = price

    # Getters and Setters
    def get_title(self):
        return self._title
    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author
    def set_author(self, author):
        self._author = author

    def get_publication_date(self):
        return self._publication_date
    def set_publication_date(self, publication_date):
        self._publication_date = publication_date

    def get_genre(self):
        return self._genre
    def set_genre(self, genre):
        self._genre = genre

    def get_price(self):
        return self._price
    def set_price(self, price):
        self._price = price

    def __str__(self):
        return f"EBook({self._title}, {self._author}, {self._publication_date}, {self._genre}, ${self._price})"


class ShoppingCart:
    def __init__(self):
        self._items = []
        self._total_price = 0.0

    def add_item(self, ebook):
        self._items.append(ebook)
        self._total_price += ebook.get_price()

    def remove_item(self, ebook):
        if ebook in self._items:
            self._items.remove(ebook)
            self._total_price -= ebook.get_price()

    def get_total_price(self):
        return self._total_price

    def list_items(self):
        return [str(item) for item in self._items]

    def __str__(self):
        items_str = ', '.join([item.get_title() for item in self._items])
        return f"ShoppingCart(Items: [{items_str}], Total Price: ${self._total_price:.2f})"


class Customer:
    def __init__(self, name, email, phone, membership_status):
        self._name = name
        self._email = email
        self._phone = phone
        self._membership_status = membership_status
        self._shopping_cart = ShoppingCart()

    # Getters and Setters
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_email(self):
        return self._email
    def set_email(self, email):
        self._email = email

    def get_phone(self):
        return self._phone
    def set_phone(self, phone):
        self._phone = phone

    def get_membership_status(self):
        return self._membership_status
    def set_membership_status(self, membership_status):
        self._membership_status = membership_status

    def get_shopping_cart(self):
        return self._shopping_cart

    def __str__(self):
        return f"Customer({self._name}, {self._email}, {self._membership_status})"


class PremiumCustomer(Customer):
    def __init__(self, name, email, phone, membership_status, discount_rate, loyalty_points):
        super().__init__(name, email, phone, membership_status)
        self._discount_rate = discount_rate
        self._loyalty_points = loyalty_points

    # Additional getters and setters
    def get_discount_rate(self):
        return self._discount_rate
    def set_discount_rate(self, discount_rate):
        self._discount_rate = discount_rate

    def get_loyalty_points(self):
        return self._loyalty_points
    def set_loyalty_points(self, loyalty_points):
        self._loyalty_points = loyalty_points

    def __str__(self):
        return f"PremiumCustomer({self._name}, {self._email}, {self._membership_status}, Discount Rate: {self._discount_rate}, Loyalty Points: {self._loyalty_points})"


class Order:
    def __init__(self, order_id, items, discount=0.0):
        self._order_id = order_id
        self._items = items
        self._discount = discount
        self._final_price = sum(item.get_price() for item in items) * (1 - discount)

    def get_final_price(self):
        return self._final_price

    def __str__(self):
        items_str = ', '.join([item.get_title() for item in self._items])
        return f"Order(ID: {self._order_id}, Items: [{items_str}], Final Price: ${self._final_price:.2f})"


class Invoice:
    def __init__(self, invoice_id, order, vat_rate=0.08):
        self._invoice_id = invoice_id
        self._order = order
        self._vat = self._order.get_final_price() * vat_rate
        self._total = self._order.get_final_price() + self._vat

    def get_total(self):
        return self._total

    def __str__(self):
        return f"Invoice(ID: {self._invoice_id}, Total (with VAT): ${self._total:.2f})"


class EbookStore:
    def __init__(self, category, publisher, language, year):
        self._category = category
        self._publisher = publisher
        self._language = language
        self._year = year
        self._e_books = []

    # Getters and Setters
    def get_category(self):
        return self._category
    def set_category(self, category):
        self._category = category

    def get_publisher(self):
        return self._publisher
    def set_publisher(self, publisher):
        self._publisher = publisher

    def get_language(self):
        return self._language
    def set_language(self, language):
        self._language = language

    def get_year(self):
        return self._year
    def set_year(self, year):
        self._year = year

    def get_ebooks(self):
        return self._e_books

    # Method to add an e-book to the store's catalog
    def add_ebook(self, ebook):
        self._e_books.append(ebook)
        print(f"EBook '{ebook.get_title()}' added to the store.")

    # Method to remove an e-book from the store's catalog
    def remove_ebook(self, ebook):
        if ebook in self._e_books:
            self._e_books.remove(ebook)
            print(f"EBook '{ebook.get_title()}' removed from the store.")
        else:
            print(f"EBook '{ebook.get_title()}' not found in the store.")

    # Method to list all e-books in the store's catalog
    def list_ebooks(self):
        return [str(ebook) for ebook in self._e_books]

    def __str__(self):
        return f"EbookStore(Category: {self._category}, Publisher: {self._publisher}, Language: {self._language}, Year: {self._year}, Total EBooks: {len(self._e_books)})"