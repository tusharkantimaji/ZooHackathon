print '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Deceased</title>
</head>
<body>
<h2>Enter the CerNo of the Elephant</h2>
<div class="col-sm-4 col-sm-offset-1">
	<div class="login-form"><!--login form-->
		<form name="frm" method="post" action="deceased_code.py">
			<input type="text" name="cerno" placeholder="Certificate Number" required />
			<br><br>
			<input type="password" name="pwd" placeholder="Ranger Password" required />
			<br><br>
			<input type="submit" name="ok" class="btn btn-primary" value="OK">
		</form>
	</div><!--/login form-->
</div>'''