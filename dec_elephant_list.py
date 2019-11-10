print '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h2>Deceased Elephant List</h2>'''
import config,cgi
frm=cgi.FieldStorage()
cursor=config.db.cursor()
cursor.execute('SELECT * FROM dece')
result=cursor.fetchall()
if result:
    print '''<table class="table table-striped table-bordered table-hover" id="dataTables-example">
    <thead>
        <tr>
            <th>Certificate Number</th>
        </tr>
    </thead>
    <tbody>'''
    for rec in result:
        print'''<tr>
                    <td>{}</td>
                </tr>'''.format(rec[0])
    print'''</tbody>
    </table>
    '''
else:
    print 'Nothing Found'