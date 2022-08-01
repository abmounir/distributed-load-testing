from fastapi import FastAPI, HTTPException, Response, status
from fastapi.middleware.cors import CORSMiddleware
# from prometheus_client import start_http_server, Counter, Info, Gauge,Histogram, MetricsHandler, make_asgi_app
from aioprometheus import Counter, Gauge, Histogram, Summary, MetricsMiddleware
from aioprometheus.asgi.starlette import metrics
import time
# app_metrics = make_asgi_app()
# start_http_server(port=8000)
# function execution time , type Histogram
h=Histogram('execution_time','execution time')
app = FastAPI()
app.state.users_events_counter = Counter("events", "Number of events.")
app.state.books_counter = Counter("books", "Number of books.")
app.add_middleware(MetricsMiddleware)
app.add_route("/metrics", metrics)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
import logging, datetime

logging.basicConfig(level=logging.INFO)

# book data including title, author, price 
books_data = [{'title': 'the lord of the rings', 'author': 'J. R. R. Tolkien', 'price': 10.99},{'title':'A Game of Thrones','author':'George R. R. Martin','price':9.99},{'title':'The Name of the Wind','author':'Patrick Rothfuss','price':8.99},{'title':'The Way of Kings','author':'Brandon Sanderson','price':7.99},{'title':'The Lies of Locke Lamora','author':'Scott Lynch','price':6.99},{'title':'The Final Empire','author':'Brandon Sanderson','price':5.99},{'title':'The Eye of the World','author':'Robert Jordan','price':4.99},{'title':'The Blade Itself','author':'Joe Abercrombie','price':3.99},{'title':'The Fellowship of the Ring','author':'J. R. R. Tolkien','price':2.99},{'title':'The Black Prism','author':'Brent Weeks','price':1.99}]

@app.post("/v1/pay", status_code=201)
async def payment(d: dict):
    logging.info(datetime.datetime.now())
    logging.info(d)
    app.state.books_counter.inc({"book": d["title"], "author": d["author"], "price": d["price"]})
    return {"message": "Purchase completed successfully."}

@app.get("/v1/books")
async def books():
    logging.info(datetime.datetime.now())
    app.state.users_events_counter.inc({"path": "/v1/books", })
    return books_data
# add to cart
@app.post("/v1/cart", status_code=201)
async def cart(d: dict):
    logging.info(datetime.datetime.now())
    logging.info(d)
    app.state.users_events_counter.inc({"path": "/v1/cart", })
    return {"message": "Book added to cart successfully."}

# stripe api endpoint

@app.post("/v1/charge", status_code=201)
async def charge(d: dict):
    logging.info(datetime.datetime.now())
    logging.info(d)
    app.state.users_events_counter.inc({"path": "/v1/charge", })
    return {"message": "Payment completed successfully."}
