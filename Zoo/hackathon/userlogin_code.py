import cgi,cgitb
import config
frm=cgi.FieldStorage()
ename=frm.getvalue('Elephantname')
cno=frm.getvalue('CNumber')
mno=frm.getvalue('MNumber')
mcno=frm.getvalue('CertificateNumber')
gen=frm.getvalue('g1')
age=frm.getvalue('age')
name=frm.getvalue('owner')
add=frm.getvalue('address')
mstat=frm.getvalue('r1')
try:
    cursor=config.db.cursor()
    sql="INSERT INTO identity (Ename,Cerno,Mno,MRno,Owstatus,Age,Sex,Oname,Address)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(ename,cno,mno,mcno,mstat,age,gen,name,add)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        print ("""
                        <html>
                            <body>
                            <script>
                            window.location='Zoo1.html?msg=Welcome'
                            </script>
                            </body>
                        </html>""")
except Exception as e:
    print (e)
print ("</body>")
print ("</html>")