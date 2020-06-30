## Async erros with express:
```
yarn add express-async-errors
```
## Exception Handling

* **define error class**

```
export default class AppError {
    public readonly message: string;

    public readonly statusCode: number;

    constructor(message: string, statusCode = 400) {
        this.message = message;
        this.statusCode = statusCode;
    }
}

```

* **apply it to the services**

...
if (!passwordMatched) {
    throw new AppError('Incorrect email/password combination.', 401);
}
...



* **server.ts**

```

// after the routes: error handling

app.use(
    (err: Error, request: Request, response: Response, next: NextFunction) => {
        // if error already defined by me,
        // return defined message
        if (err instanceof AppError) {
            return response
                .status(err.statusCode)
                .json({ status: 'error', message: err.message });
        }

        console.log(err);
        // unexpected error
        return response.status(500).json({
            status: 'error',
            message: 'Internal server error',
        });
    },
);


```