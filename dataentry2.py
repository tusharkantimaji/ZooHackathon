print '''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Entry</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <link href="css/prettyPhoto.css" rel="stylesheet">
    <link href="css/price-range.css" rel="stylesheet">
    <link href="css/animate.css" rel="stylesheet">
	<link href="css/main.css" rel="stylesheet">
	<link href="css/responsive.css" rel="stylesheet">
    <!--[if lt IE 9]>
    <script src="js/html5shiv.js"></script>
    <script src="js/respond.min.js"></script>
    <![endif]-->       
    <link rel="shortcut icon" href="images/ico/favicon.ico">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="images/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="images/ico/apple-touch-icon-114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="images/ico/apple-touch-icon-72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="images/ico/apple-touch-icon-57-precomposed.png">
</head>
<body>
    <div class="col-sm-4" align="center">
					<div class="signup-form">
						<h2>Elephant Details</h2>
						<form name="frm" method="post" action="usersign_code_2.py">
						    <input type="text" name="cerno" placeholder="Certificate Numer" required/>
							<input type="text" name="color" placeholder="Body Color" required/>
							<input type="text" name="ecolor" placeholder="Eye Color" required/>
							<input type="text" name="height" placeholder="Height" required/>
							<input type="text" name="length" placeholder="Length Tail to Trunk" required/>
							<input type="text" name="ngirth" placeholder="Neck Girth" required/>
							<input type="number" name="cgirth" placeholder="Chest Girth" required/>
							<input type="number" name="weight" placeholder="Weight" required/>
							<input type="number" name="frnail" placeholder="Front Right Nail Count" required/>
							<input type="number" name="hrnail" placeholder="Hind Right Nail Count" required/>
							<input type="number" name="flnail" placeholder="Front Left Nail Count" required/>
							<input type="number" name="hlnail" placeholder="Hind Left Nail Count" required/>
							<input type="number" name="molset" placeholder="Molar Set" required/>
							<input type="submit" name="ok" class="btn btn-primary" value="SUBMIT">
						</form>
					</div><!--/sign up form-->
	</div>
</body>
</html>'''