## Form Validation with React.js

```
yarn add yup
```

#### Validation Example

* **Receiving data from fields of a sign up form**
```
const handleSubmit = useCallback(async (data: Record<string, unknown>) => {
try {
  const schema = Yup.object().shape({
    name: Yup.string().required('Nome obrigatório'),
    email: Yup.string()
      .required('E-mail obrigatório')
      .email('Digite um e-mail válido'),
    password: Yup.string().min(6, 'No mínimo 6 dígitos'),
  });

  // abort early for showing all errors
  await schema.validate(data, { abortEarly: false });
} catch (err) {
  console.log(err);
}
}, []);

```