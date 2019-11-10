print '''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
<body>'''

import config,cgi
frm=cgi.FieldStorage()
id=frm.getvalue('CerNo')
cursor=config.db.cursor()
cursor.execute('SELECT * FROM identity WHERE CerNo="{}"'.format(id))
result=cursor.fetchall()
rec=result[0]

print'''
<form name="frm" method="post" action="update_code.py">
<div class="from-group">
    <label for="pname">Change Certificate Validity</label>
    <input type="date" name="date" value="{}" class="form-control">
    <input type="hidden" name="id" value="{}">
</div>'''.format(rec[10],id)
print'''
<br>
<input type="submit" name="ok" value="Update Date"/>
</form>
</body>
</html>
'''