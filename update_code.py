print '''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>'''
import cgi, config
frm=cgi.FieldStorage()
cerno=frm.getvalue('id')
systemdate=frm.getvalue('date')

try:
    cursor = config.db.cursor()
    sql = "UPDATE identity SET sysdate='{}' WHERE CerNo='{}'".format(systemdate, cerno)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        print '''<script>
                    window.location='check_date.py?id={}&msg=Updated successfully'
                </script>'''.format(cerno)
except Exception as e:
    print e
print '''</body>
</html>'''