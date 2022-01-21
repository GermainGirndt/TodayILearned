
## Before - Promise without Async
```
const minhaPromise = () => new Promise((resolve, reject) => {
    setTimeout(() => {resolve('OK')}, 2000);
});

// can turn into cascate
minhaPromise().then(response => {console.log(response)})

```


## After - with Async

```
//  async doesn't need callback/cascate
// async oesn't need then...
// if await, the next line just will just be execute, when the 
async function executePromise() {

    console.log(await minhaPromise());
    console.log(await minhaPromise());
    console.log(await minhaPromise());
    
    
}
executePromise();
```

## Alternatively
```

const executePromise2 = async () => {

    console.log(await minhaPromise());
    console.log(await minhaPromise());
    console.log(await minhaPromise());
}

executePromise2();

```


## Example 1 - Async with Axios

```
import axios from 'axios';

class Api {
    static async getUserInfo(username) {
        const response = await axios.get(`https://api.github.com/users/${username}`);
        console.log(response)
    }
}

Api.getUserInfo('GermainPereira')
```


## Example 2 - Before/After (awaits 1 sec and print)

#### Before
```

const delay = () => new Promise(resolve => setTimeout(resolve, 1000));
function umPorSegundo() {
 delay().then(() => {
 console.log('1s');
 delay().then(() => {
 console.log('2s');
 delay().then(() => {
 console.log('3s');
 });
 })
 });
}
umPorSegundo();

```

#### After
```
const delay = () => new Promise(resolve => setTimeout(resolve, 1000));


async function umPorSegundo() {
 await delay();
 console.log("1s");
 await delay();
 console.log("2s");
 await delay();
 console.log("3s");
}

umPorSegundo();

```


## Example 3 - Before/After - non-async to async


#### Before

```
import axios from 'axios';
function getUserFromGithub(user) {
 axios.get(`https://api.github.com/users/${user}`)
 .then(response => {
 console.log(response.data);
 })
 .catch(err => {
 console.log('Usuário não existe');
 })
}
```

#### After

```
import axios from 'axios';


class Api {
    static async getUser(username) {
        try {
            let data = await axios.get(`https://api.github.com/users/${username}`)
            console.log(data)
        } catch {
            console.log('Usuário não existe');
        }
    }
}

```

