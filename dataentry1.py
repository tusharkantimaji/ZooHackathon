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
						<h2>Elephant and Owner Data Entry</h2>
						<form name="frm" method="post" action="usersign_code_1.py">
							<input type="text" name="ename" placeholder="ElephantName" required/>
							<input type="text" name="cerno" placeholder="Certificate Number" required/>
							<input type="text" name="mno" placeholder="Microchip Number" required/>
							<input type="text" name="mrno" placeholder="Microchip RegIstration Number" required/>
							<input type="text" name="oname" placeholder="Owner Name" required/>
							<input type="number" name="age" placeholder="Elephant Age" required/>							
                            <h5 align="left">Elephant Gender</h5>
                            <input type="radio" name="gender" value="Female"> Female<br>
                            <input type="radio" name="gender" value="Male">Male<br>
                            <input type="text" name="address" placeholder="Owner Address" required/>
                            <h5 align="left">Migration Status</h5>
                            <input type="radio" name="mstat" value="Owner">Owner<br>
                            <input type="radio" name="mstat" value="Custodian">Custodian<br>
                            <input type="radio" name="mstat" value="Representative">Representative<br>
                            <input type="radio" name="mstat" value="Constructor">Constructor<br>
                            <input type="text" name="obs" placeholder="Obseravtion"/>
                            <input type="date" name="date" placeholder="Insert DATE"/>			
							<input type="submit" name="ok" class="btn btn-primary" value="SUBMIT">
						</form>
					</div><!--/sign up form-->
	</div>
</body>
</html>'''