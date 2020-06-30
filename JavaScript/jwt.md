# JWT - Authentication in REST APIs

* **JSON Web Token** - Used in REST APIs instead of normal sessions

### Example

* **POST to JWT route** api.com/session (new session)
```
{
	"email": "germain@email.com"
	"password": "123456"
}

```

* if all informations are correct, the route generates a JWT Token:


### JWT TOKEN
* **3 Parts Structure:** XXXXXXXXXXXX.XXXXXXXXXXX.XXXXXXXXXX
  * **Part 1:** headers (identifies the generated token)
  * **Part 2:** playload (additional informations, like userid)
  * **Part 3:** token signature (integrity verifier)