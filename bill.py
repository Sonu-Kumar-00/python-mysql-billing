import time as t
import mysql.connector


def bill():
    con = mysql.connector.connect(
    host="localhost",
    user="root", #enter your database name
    password="WJ28@krhps",
    database="managers"

    )
    cur = con.cursor()
    order_id=int(input("enter the order id: "))
    product_name=input("enter the product name: ")
    price=float(input("enter the P_Price: "))
    quantity=int(input("enter the Quantity: "))
    amount=price*quantity
    sql = """INSERT INTO results (Order_id,product_name,price,quantity,amount) VALUES (%s,%s,%s,%s,%s)"""
    values = (order_id,product_name,price,quantity,amount)
    cur.execute(sql,values)
    con.commit()
    print("✅ Data successfully inserted into results table!")

    amount=price*quantity
    name=str(order_id)
    time=t.ctime()
    f = open(name + ".txt", "w")
    data=f.write(f'''
    Time: {time}
    --------------------
    order id: {order_id}
    product name: {product_name}
    Quantity: {quantity}
    ---------------------Z
    final amount: {amount}''')
    f.close()
    cur.close()
    con.close()
    
bill()