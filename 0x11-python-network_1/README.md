This directory contains:

Task 0 - Python script that fetches https://alx-intranet.hbtn.io/status using the package urllib 

Task 1 - Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable	   found in the header of the response use the packages urllib and sys only, alongside the 'with' statement.

Task 2 - Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parame	   ter, and displays the body of the response (decoded in utf-8). The email must be sent in the email variable uinge	     the packages urllib and sys only alongside the 'with' statement.

Task 3 - Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in u	   tf-8), managing urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code uing th	     e packages 'urllib' and 'sys'only alongside the 'with' statement.

Task 4 - Python script that fetches https://alx-intranet.hbtn.io/status use the package 'requests' only, displaying the   	   body of the response in 'tabulation before -' format.

Task 5 - Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id 	   in the response header using the packages requests and sys

Task 6 - Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as 	   a parameter, and finally displays the body of the response, sending the email in the variable email, using the 	     packages 'requests' and 'sys' only.

Task 7 - Python script that takes in a URL, sends a request to the URL and displays the body of the response.If the HTTP 	   status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code 	     using the packages 'requests' and 'sys' only.

Task 8 - Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter 	   as a parameter. The letter must be sent in the variable q. If no argument is given, set q="". If the response 
	 body iserly JSON formatted and not empty, display the id and name like this: [<id>] <name> Otherwise: Display 
	 Not a valid JSON if the JSON is tf the JSON is invalid and 'No result' if it's empty, using the package 
	 'requests' and 'sys'only.

Task 9 - Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your 	   id. You must use Basic Authentication with a personal access token as password to access to your information (
	 only read:user permission is needed). The first argument will be your username. The second argument will be your 
	 password (in your case, a personal access token as password) using the packages 'requests' and 'sys' only. 
