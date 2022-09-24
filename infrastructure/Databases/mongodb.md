## Foreword

Difference between MongoDB and relational DB:

- "Tables" are called "Schemas"
- "Entries"/"Registries" are called "Documents"

## Install using Docker

`sudo docker run --name mongodb -p 27017:27017 -d -t mongo`

## Install Mongo Client

- **Mongo Compass**
  https://www.mongodb.com/try/download/compass

Note: You may need to install another dependencies

- Alternative: Mongo 3T

## Creating a new Database

1. With Mongo's Container running, open the connection using the client:

mongodb://localhost:27017

or

mongodb://localhost:27017/DATABASE_NAME

## MongoDB JavaScript Package

`yarn add mongodb`

## Example for Initial Setup Using TypeORM

- **Schema**

```
import {
    ObjectID,
    Entity,
    Column,
    ObjectIdColumn,
    CreateDateColumn,
    UpdateDateColumn,
} from 'typeorm';

@Entity('notifications')
class Notification {
    @ObjectIdColumn()
    id: ObjectID;

    @Column()
    content: string;

    @Column('uuid')
    recipient_id: string;

    @Column({ default: false })
    read: boolean;

    @CreateDateColumn()
    created_at: Date;

    @UpdateDateColumn()
    updated_at: Date;
}

export default Notification;

```

- **ORM Config**

```
 {
        "name": "mongo",
        "type": "postgmongodb",
        "host": "localhost",
        "port": 27017,
        "database": "gobarber",
        "useUnifiedTopology": true,
        "entities": [
            "./src/modules/**/infra/typeorm/schemas/*.ts"
        ]
    }
```

- **For many simultaneous database connections**

```
import { createConnections } from 'typeorm';

// reads for orm.config
createConnections();
```

- **Using standard mongo repository**

```
import { getMongoRepository, MongoRepository } from 'typeorm';

import SchemaName from "SCHEMA_DIRECTORY";

class ClassName implements Interface {

  private ormRepository: MongoRepository<SchemaName>;

  constructor() {
    this.ormRepository = getMongoRepository(Notification, 'mongo'); // 'mongo' is the connection name, which isn't 'default'
  }

}
```
