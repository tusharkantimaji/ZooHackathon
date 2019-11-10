print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>DEC</title>'
print '</head>'
print '<body>'
import cgi, cgitb, config
frm=cgi.FieldStorage()
cerno=frm.getvalue('cerno')
pas=frm.getvalue('pwd')
cursor=config.db.cursor()
cursor.execute("SELECT * FROM officials WHERE pass='{}'".format(pas))
row=cursor.fetchall()
if row:
    try:
        cur = config.db.cursor()
        sql = "INSERT INTO dece (cerno)VALUES('%s')" % (cerno)
        if cur.execute(sql):
            config.db.commit()
            config.db.close()
            print """
                                <html>
                                    <body>
                                        <script>
                                            window.location='official_page.py?msg=Inserted'
                                        </script>
                                    </body>
                                </html>"""
    except Exception as e:
        print e
print '</body>'
print '</html>'