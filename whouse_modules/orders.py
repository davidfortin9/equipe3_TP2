import sqlite3

def get_orders():

    #Connect to DB
    conn = sqlite3.connect('whouseDB.db')
    c = conn.cursor()

    #Get arcs from DB
    c.execute("SELECT * FROM Orders")
    order_list = c.fetchall()
    return order_list
    
