print '''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>OWNER Login | Register</title>
    <style>
    .priyam:hover{
    text-decoration:none;
    background-color:orange;
    color:white;
    }
    </style>
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
</head><!--/head-->

<body>
	<header id="header"><!--header-->
	</header><!--/header-->
	<h1 align="center">Owner Login or Register</h1>
    <section id="form"><!--form-->
		<div class="container">
			<div class="row">
				<div class="col-sm-4 col-sm-offset-1">
					<div class="login-form"><!--login form-->
						<h2>Owner Login</h2>
						<form name="frm" method="post" action="owner_enter.py">
							<input type="text" name="name" placeholder="Name" required />
							<input type="password" name="pwd" placeholder="Password" required />
							<input type="submit" name="ok" class="btn btn-primary" value="LOGIN">
						</form>
					</div><!--/login form-->
				</div>
				<div class="col-sm-1">
					<h2 class="or">OR</h2>
				</div>
				<div class="col-sm-4">
					<div class="signup-form"><!--sign up form-->
						<h2>New Owner Signup</h2>
						<form name="frm" method="post" action="ownersign_code.py">
							<input type="text" name="name" placeholder="Name" required/>
							<input type="password" name="pwd" placeholder="Password" required/>
							<input type="text" name="contact" placeholder="Contact" required/>
							<input type="text" name="address" placeholder="Address" required/>
							<input type="number" name="eleno" placeholder="Number of Elephants" required/>
							<input type="submit" name="ok" class="btn btn-primary" value="SIGNUP">
						</form>
					</div><!--/sign up form-->
				</div>
			</div>
		</div>
	</section><!--/form-->
	</body>
	</html>
	'''
