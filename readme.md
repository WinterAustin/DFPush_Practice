# My Flask Application

This is a simple Flask application with two routes:

- `/get`: Handles GET requests and returns a JSON response with the message "success".
- `/post`: Handles POST requests, extracts JSON data from the request, and echoes back the same data in a JSON response.

## Usage Examples

### GET Route

To send a GET request to the `/get` endpoint using cURL:

```bash
curl http://127.0.0.1:5000/get

#To send a POST request to the '/POST' endpoint:

curl -X POST -H "Content-Type: application/json" -d '{"key": "value"}' http://127.0.0.1:5000/post
