- Clone repository <br> <br>

- Create an virtual environment:<br>
  virtualenv env<br>
 
- Then install packages inside the virtual environment: <br>
  pip install django <br>
  pip install pillow <br>

  pip freeze <br>
  (to check installed packages)<br>

- Working with email host: <br>

1. Rootlevel/settings.py <br>
	  change email_host_user and email_host_password fields (at line 135,136)<br><br>

2. website/template/carrer.html<br>
	  change example@gmail.com to your email address(at line 844) <br><br>

3. website/views.py<br>
	  change example@gmail.com to your email address(at line 23) <br><br>

- Now, migrate these changes: <br>  
  py manage.py makemigrations<br>
  py manage.py migrate<br> <br>

- Run the server:<br>
  py manage.py runserver

