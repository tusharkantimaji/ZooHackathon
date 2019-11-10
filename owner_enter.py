import cgi
import config
frm=cgi.FieldStorage()
name=frm.getvalue('name')
pas=frm.getvalue('pwd')
cursor=config.db.cursor()
cursor.execute("SELECT * FROM owner WHERE oname='{}' AND opwd='{}'".format(name, pas))
row=cursor.fetchall()
if row:
    import Cookie
    c=Cookie.SimpleCookie()
    for j in row:
        c['info1']=j[0]
    # set the expires time
    c['info1']['expires']=60*60*24 # Expire after 24 hour
    # print the header, starting with the cookie
    print c
    print "Content-type: text/html\n"

    # empty lines so that the browser knows that the header is over
    print ""
    print ""

    # now we can send the page content
    print """
    <html>
        <body>
        <script>
        window.location='official_page.py?msg=Login sucessfully'
        </script>
        </body>
    </html>"""
else:
    print """
    <html>
        <body>
        <script>
        window.location='owner_login.py?msg=Invalid Email or Password'
        </script>
        </body>
    </html>"""
