print '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h2>Owner Details</h2>'''
import config,cgi
frm=cgi.FieldStorage()
cursor=config.db.cursor()
cursor.execute('SELECT * FROM identity ORDER BY sysdate ASC')
result=cursor.fetchall()
if result:
    print '''<table class="table table-striped table-bordered table-hover" id="dataTables-example">
    <thead>
        <tr>
            <th>Ename</th>
            <th>OName</th>
            <th>Address</th>
            <th>Date</th>
            <th>Mig Stat</th>
        </tr>
    </thead>
    <tbody>'''
    for rec in result:
        print'''<tr>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                </tr>'''.format(rec[0],rec[6],rec[7],rec[10],rec[8])
    print'''</tbody>
    </table>
    '''
else:
    print 'Nothing Found'