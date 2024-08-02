import mysql.connector

em=mysql.connector.connect(
    host="localhost",
    user="gayathrijayadevan", 
    password="gayu2024@synfo",  
    database="new1"  
)

cursor=em.cursor()
try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dtls (
            emp_id INT PRIMARY KEY,    
            position VARCHAR(100),
            address VARCHAR(100)       
        )
    ''')
except:
    pass

l= int (input("Enter no of employee : "))
for i in range(l):
            id = int(input('enter employee id: '))
            pos = str(input('Enter ur position:'))
            address=input("Enter address:")
 
            cursor.execute('INSERT INTO dtls (emp_id, position,address) VALUES (%s,%s,%s)',
                        (id,pos,address))
            em.commit()

# cursor.execute('DROP TABLE dtls')