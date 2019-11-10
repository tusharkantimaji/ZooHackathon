print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Me</title>'
print '</head>'
print '<body>'
import cgi, cgitb, config
frm=cgi.FieldStorage()
ename=frm.getvalue('ename')
cerno=frm.getvalue('cerno')
mno=frm.getvalue('mno')
mrno=frm.getvalue('mrno')
oname=frm.getvalue('oname')
age=frm.getvalue('age')
gen=frm.getvalue('gender')
add=frm.getvalue('address')
mstat=frm.getvalue('mstat')
obs=frm.getvalue('obs')
date=frm.getvalue('date')

try:
    cursor=config.db.cursor()
    sql="INSERT INTO identity (Ename,Cerno,Mno,MRno,Age,Sex,Oname,Address,Migstat,Observation,sysdate)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(ename,cerno,mno,mrno,age,gen,oname,add,mstat,obs,date)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        print """
                        <html>
                            <body>
                            <script>
                            window.location='dataentry1.py?msg=Inserted'
                            </script>
                            </body>
                        </html>"""
except Exception as e:
    print e
print '</body>'
print '</html>'