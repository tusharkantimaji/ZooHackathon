print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Me</title>'
print '</head>'
print '<body>'
import cgi, cgitb, config
frm=cgi.FieldStorage()
cerno=frm.getvalue('cerno')
color=frm.getvalue('color')
ecolor=frm.getvalue('ecolor')
hei=frm.getvalue('height')
len=frm.getvalue('length')
ngirth=frm.getvalue('ngirth')
cgirth=frm.getvalue('cgirth')
weight=frm.getvalue('weight')
frnail=frm.getvalue('frnail')
hrnail=frm.getvalue('hrnail')
flnail=frm.getvalue('flnail')
hlnail=frm.getvalue('hlnail')
molset=frm.getvalue('molset')

try:
    cursor=config.db.cursor()
    sql="INSERT INTO physique (CerNo,color,Ecolor,Height,Length_tt,Ngirth,Cgirth,Weight,FRnail,HRnail,FLnail,HLnail,MolSet)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(cerno,color,ecolor,hei,len,ngirth,cgirth,weight,frnail,hrnail,flnail,hlnail,molset)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        print """
                        <html>
                            <body>
                            <script>
                            window.location='dataentry2.py?msg=Inserted'
                            </script>
                            </body>
                        </html>"""
except Exception as e:
    print e
print '</body>'
print '</html>'