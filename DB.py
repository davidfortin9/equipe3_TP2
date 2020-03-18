import sqlite3

conn = sqlite3.connect('SQLiteDB.db')

c = conn.cursor()

# Creation de la table arcs
# c.execute("""CREATE TABLE ARCS (
#     id int,
#     travel_node real,
#     head_node_id int,
#     tail_node_id int
#     )""") 

#Creation de la table SKU
# Pour la colone class j'ai du utiliser text (ENUM pas un data type SQLite)
# c.execute("""CREATE TABLE SKU (
#      id int,
#      name text,
#      description text,
#      Class text,
#      x_size real,
#      y_size real,
#      z_size real,
#      weight real
#     )""")

#Création de la table orders
#Pour order_dtg, target_dtg, pick_dtg j'ai du utiliser text au lieu de datetime format=(“YYYY-MM-DD HH:MM:SS.SSS”)
#Pour order_status j'ai du utiliser text au lieu de enum
# c.execute("""CREATE TABLE ORDERS (
#      id int,
#      order_dtg text,
#      target_pick_dtg text,
#      customer text,
#      order_number text,
#      order_status text,
#      pick_dtg text
#  )""")

#Création table LINE_ITEM
#pour status j'ai du utiliser text au lieu de enum
# c.execute("""CREATE TABLE LINE_ITEM (
#      id int,
#      quantity int,
#      order_id int,
#      sku_id int,
#      status text)""")


#J'ai du utiliser text au lieu de enum pour type
# c.execute("""CREATE TABLE NODE(
#      id int,
#      name text,
#      x real,
#      y real,
#      z real,
#      type text
#      )""")

# c.execute("""CREATE TABLE SLOT(
#      id int,
#      node_id int,
#      sku_id int,
#      quantity int
#      )""")





#c.execute("INSERT INTO arcs VALUES (1,1,1,2) ")

#c.execute("SELECT * FROM arcs WHERE id=1")

#print(c.fetchone())

#conn.commit()   

#conn.close()