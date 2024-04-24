from tokenize import String
import mysql.connector as connector


class MyDBHelper:
    def __init__(self):
        self.conn = connector.connect(
            host='localhost', port=3306, username='root', password='sanketpatil', database='my_schema')

        # date = yyyy-mm-dd
        query = "create table if not exists my_schema.grocery(productName varchar(50), price float, mfg date, exp date, limitingQuantity int, quantity int)"
        cur = self.conn.cursor()
        cur.execute(query)
        # print("Created")

    def insertData(self, productName, price, mfg, exp, limitingQuantity, quantity):
        query = "insert into my_schema.grocery(productName, price, mfg, exp, limitingQuantity, quantity)values('{}',{},'{}','{}',{},{})".format(
            productName, price, mfg, exp, limitingQuantity, quantity)
        query2 = "select productName from my_schema.grocery"
        print(query)
        cur = self.conn.cursor()
        cur2 = self.conn.cursor()

        cur2.execute(query2)

        lst = cur2.fetchall()

        if(productName,) in lst:
            cur3 = self.conn.cursor()
            print("Item already exists")
            query3 = "select quantity from my_schema.grocery where productName = '{}'".format(
                productName)
            cur3.execute(query3)
            lst = cur3.fetchall()
            final_quantity = lst[0][0]+quantity
            cur3.execute(
                "update my_schema.grocery set quantity={}, mfg='{}', exp='{}',limitingQuantity={}, price={} where productName='{}'".format(final_quantity, mfg, exp, limitingQuantity, price, productName))
            self.conn.commit()
            print("Entity Updated!")

        else:
            cur.execute(query)
            self.conn.commit()
            print("Entity Saved!")

    def fetchAll(self):
        query = "select * from my_schema.grocery"
        cur = self.conn.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
            # print("Name: ", row[0])
            # print("Price: ", row[1])
            # print("MGD Date: ", row[2])
            # print("EXP Date: ", row[3])
            # print("Available Quantity: ", row[5])
            # print('#'*30)

    def deleteEntity(self, productName):
        query = "delete from my_schema.grocery where productName = '{}'".format(
            productName)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("Deleted")

    def updateEntity(self, price, mfg, exp, limitingQuantity, quantity, productName):
        query = "update my_schema.grocery set price={}, mfg='{}', exp='{}',limitingQuantity={}, quantity={} where productName='{}'".format(
            price, mfg, exp, limitingQuantity, quantity, productName)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()

    def billingChanges(self, productName, new_quantity):
        query = "select price, quantity from my_schema.grocery where productName='{}'".format(
            productName)
        cur = self.conn.cursor()
        cur2 = self.conn.cursor()
        cur.execute(query)
        lst = cur.fetchall()
        print(lst)
        print("Total bill price: ", lst[0][0] * new_quantity)
        print("Remaining quantities are: ", lst[0][1]-new_quantity)
        query2 = "update my_schema.grocery set quantity={} where productName='{}'".format(
            lst[0][1]-new_quantity, productName)
        cur2.execute(query2)
        self.conn.commit()

    def generalQuery(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()


if __name__ == "__main__":

    helper = MyDBHelper()
    # helper.insertData('Rin', 10, '1999-4-20', '3050-4-11', 33, 100)
    # helper.insertData('Eclairs', 1, '2019-11-20', '2025-5-1', 100, 1500)

    # helper.insertData('Noodles', 20, '2021-4-20', '2023-4-11', 11, 70)
    # helper.insertData('Item1', 50, '2022-5-23', '2023-4-11', 15, 45)
    # helper.insertData('Item2', 60, '2019-1-1', '2023-4-11', 3, 12)
    # helper.insertData('Item2', 65, '2021-3-21', '2023-4-11', 20, 98)

    # helper.fetchAll()
    # helper.updateEntity(22, '1999-4-20', '3050-4-11', 100, 5000, 'Rin')
    # helper.fetchAll()

    # helper.updateEntity("Rin")
    # helper.deleteEntity('Item1')

# helper.billingChanges('Rin', 15)
