print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Me</title>'
print '</head>'
print '<body>'
import cgi, cgitb, config
frm=cgi.FieldStorage()
name=frm.getvalue('name')
address=frm.getvalue('address')
contact=frm.getvalue('contact')
eleno=frm.getvalue('eleno')
pwd=frm.getvalue('pwd')

try:
    cursor=config.db.cursor()
    sql="INSERT INTO owner (oname,opwd,oaddress,ophone,ele_no)VALUES('%s','%s','%s','%s','%s')"%(name,pwd,address,contact,eleno)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        print """
                        <html>
                            <body>
                            <script>
                            window.location='owner_login.py?msg=Welcome'
                            </script>
                            </body>
                        </html>"""
except Exception as e:
    print e
print '</body>'
print '</html>'