# General Concepts


# DTO - Data Transfer Object
* **Transfering data though components/files** -> JSON is ideal.

# Separation of concerns
* **Every file muss serve for one and just one purpose**  - Everything else should be delegated

eg. 
```
Routes should get a request, call a function to process it and deliver the result
No processing, no business rules inside it.
Just call some function that does it and "Magically" deliver.

Exception: simple data transformation, which can be done in the route
```