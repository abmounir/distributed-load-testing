from locust import HttpUser, task, between

books_data = [{'title': 'the lord of the rings', 'author': 'J. R. R. Tolkien', 'price': 10.99},{'title':'A Game of Thrones','author':'George R. R. Martin','price':9.99},{'title':'The Name of the Wind','author':'Patrick Rothfuss','price':8.99},{'title':'The Way of Kings','author':'Brandon Sanderson','price':7.99},{'title':'The Lies of Locke Lamora','author':'Scott Lynch','price':6.99},{'title':'The Final Empire','author':'Brandon Sanderson','price':5.99},{'title':'The Eye of the World','author':'Robert Jordan','price':4.99},{'title':'The Blade Itself','author':'Joe Abercrombie','price':3.99},{'title':'The Fellowship of the Ring','author':'J. R. R. Tolkien','price':2.99},{'title':'The Black Prism','author':'Brent Weeks','price':1.99}]
class User(HttpUser):
    wait_time = between(1, 2)
    @task(4)
    def get_books(self):
        self.client.get("/v1/books")
        
    @task(2)
    def purchase(self):
        for book in books_data:
            self.client.post("/v1/pay", json=book)
    @task(1)
    def add_to_cart(self):
        
        for book in books_data:
            self.client.post("/v1/cart", json=book)