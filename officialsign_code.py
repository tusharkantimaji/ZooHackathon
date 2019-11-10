print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Me</title>'
print '</head>'
print '<body>'
import cgi, cgitb, config
frm=cgi.FieldStorage()
name=frm.getvalue('name')
pwd=frm.getvalue('pwd')

try:
    cursor=config.db.cursor()
    sql="INSERT INTO officials (username,pass)VALUES('%s','%s')"%(name,pwd)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        print """
                        <html>
                            <body>
                            <script>
                            window.location='official_page.py?msg=Welcome'
                            </script>
                            </body>
                        </html>"""
except Exception as e:
    print e
print '</body>'
print '</html>'