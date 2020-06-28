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


### Install

```
yarn add jsonwebtoken
yarn add @types/jsonwebtoken -d
```

### Use TOKEN

 

* **FIRST PARAMETER:** payload with  token informations.
note: encripted, but NOT secure!

* **SECOND PARAMETER:** Secret key
- any random string... you could use hashed algorithms

* **THIRD PARAMETER:** token configurations
* subject: user id -> the user that has the token
* experesIn: token expiration

```
import { sign } from 'jsonwebtoken';
...

const token = sign({}, '02329A3E7EB2A56CFFB0F99DD60AC22F', {
    subject: user.id,
    expiresIn: '2d',
});

```


### Send TOKEN

* Token is send in header

```
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1OTMzNDY5NTEsImV4cCI6MTU5MzUxOTc1MSwic3ViIjoiYTNmYmRlOGYtNGJjZi00OWFjLWE5NjUtZDdhZjQ2MDNjNzdhIn0.N3hxJ7S81iNR0AAL-GqLeuLxqFxdAEAWVcclYbUmc0o
```

