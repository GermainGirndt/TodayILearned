# API

Normal Flux:
Request by a client (AJAX - normal browser request )
Response by a data structure (instead of whole html)
Client


## Request Body
* Just utilized with post and put


## Request Header
* Methods like: Post, get, delete, etc..
* Aditional information (no content related) 

eg.:
```
{"Locale": "pt_BR"}
```

## HTTP Codes - Response status
* 1XX - Informational
* 2XX - Success eg. 200 Success - 201 Created
* 3XX - Redirection 301 - Moved permanently; 302 Moved

* 4XX - Client error - 400 Bad request; 401 unauthorized (not logged, no permission); 404 not found

* 5XX - Internal Server Error - The backend could not format the response

