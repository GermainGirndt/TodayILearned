# Node - Async

### PROMISE.ALL - Make multiple requests at the same time

```
async function loadData(): Promise<void> {
  const [repository, issues] = await Promise.all([
    api.get(`repos/${params.repository}`),
    api.get(`repos/${params.repository}/issues`),
  ]);
```



### RACE - Make multiple request and return just the faster return

```
async function loadData(): Promise<void> {
  const [repository, issues] = await Promise.race([
    api.get(`repos/${params.repository}`),
    api.get(`repos/${params.repository}/issues`),
  ]);
```