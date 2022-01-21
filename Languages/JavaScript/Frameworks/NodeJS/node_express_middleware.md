## Middleware

**Purpose**: Intercepts / edit request (ex. edit query, body, etc...)

* Middleware Function can be used in the requests for executing pre-defined tasks, like loging arguments or validating a parameter.

* All routes are example of middleweres

```
// middleware
function validateProjectId(request, response, next) {
  const { id } = request.params;

  if (!isUuid(id)) {
    return response.status(400).json({ error: "Invalid project ID." });
  }

  return next();
}

// apply to all requests types with path '/projects/:id'
// one OR MORE middleweres 
  
app.use('/projects/:id', validateProjectId);

```

#### Alternative

* **Applying directly**
```
app.put("/projects/:id", validateProjectId, (request, response) => {
.
.
.
});

```
