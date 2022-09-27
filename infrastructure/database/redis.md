# Redis

# Structure

- **Just Key and Values** - No tables

* Good for caches

### Run Redis with Docker

`docker run --name redis -p 6379:6379 -d -t redis:alpine`

### Redis Driver - ioredis

- **Install**
  `yarn add ioredis`
  `yarn add @types/ioredis -D`

- **Implementation**

```
import Redis, { Redis as RedisClient } from 'ioredis';


class RedisCacheProvider {
    this.client = new RedisClient();

    public async save(key: string, value: string): Promise<void> {
        this.client.set(key, value);
    }
}



```

- **Configs**

```

export default {
    host: 'localhost',
    port: 6379,
    password: null
}; // can use options object

```
