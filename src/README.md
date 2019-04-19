Features:
---------
* User registration

* User email verification

* Change password - with password reset email.

* View user profile


API Documentation
-----------------

i. User - Registration
Create/ Register a new user.

	Endpoint 	: /api/accounts/register/
	Request Type 	: POST
	Request Params 	: username, email, password, password_2, first_name, last_name, invite_code
	Non-mandatory params : invite_code

	Response Http status codes : HTTP_200_OK or HTTP_400_BAD_REQUEST
	
	Sample Input 	: https://api.myjson.com/bins/o1id5
	Sample Output 	: https://api.myjson.com/bins/v6pmh

ii. User - Email Verification
Verify the email inorder to activate the user account.

User will recieve an email on successful registration with the verification_code. 
	
	Endpoint 	: /api/accounts/verify/<verification_code>/
	Request Type 	: GET
	Request Params 	: invite_code
	
	Response Http status codes : HTTP_200_OK or HTTP_404_NO_CONTENT
	
iii. User - Login
Obtain authentication token given the user credentials.

	Endpoint 	: /api/accounts/login/
	Request Type 	: POST
	Request Params 	: email (or username) and password
	
	Response 	: { "token": <token> }
	HTTP status code: HTTP_200_OK or HTTP_400_BAD_REQUEST
	
iv. User - Request for Password Reset
Receive an email with password reset link.

	Endpoint 	: /api/accounts/password_reset/
	Request Type 	: POST
	Request Params 	: email
	Request Sample : {"email": "some_email_id@gmail.com"}
	
	HTTP status code: HTTP_200_OK

v. User - Password Change
Change the password. Link as recieved from email by above request (iv).
	
	Endpoint 	: /api/accounts/reset/<reset_code>/
	Request Type 	: POST
	Request Sample : {"new_password": "33441122", "new_password_2": "33441122"}
	
	HTTP status code: HTTP_200_OK or HTTP_400_BAD_REQUEST
	
	
