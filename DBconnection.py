import MySQLdb
#myDB = MySQLdb.connect(host="192.168.1.108",port=3306,user="username",passwd="password",db="")
def connection():
    myDB = MySQLdb.connect(host="192.168.1.115",port=3306,user="username",passwd="password",db="")
    return myDB


"""
conn= connection()

cursore = conn.cursor()
cursore.execute("SELECT cig, importo FROM gare.gare where data_scadenza>NOW()")
bandi = cursore.fetchall()
for uno in bandi:
    print uno

"""
