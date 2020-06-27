# ormconfig.json

```
{
    "type": "postgres",
    "host": "localhost",
    "port": 5432,
    "username": "postgres",
    "password": "docker",
    "database": "gostack_barber",
    "migrations": [
        "./src/database/migrations/*.ts"
    ]
}

```

# package.json - scripts

```
        "typeorm": "ts-node-dev ./node_modules/typeorm/cli.js"
```

# Terminal - Migrations

```
 yarn typeorm migration:create -n CreateAppointments

```


## Migration Example

```
import { MigrationInterface, QueryRunner, Table } from 'typeorm';

export default class CreateAppointments1593092191606
    implements MigrationInterface {
    // DO
    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.createTable(
            new Table({
                name: 'appointments',
                columns: [
                    {
                        name: 'id',
                        type: 'varchar',
                        isPrimary: true,
                        generationStrategy: 'uuid',
                    },
                    {
                        name: 'provider',
                        type: 'varchar',
                        isNullable: false,
                    },
                    {
                        name: 'date',
                        type: 'timestamp with time zone',
                        isNullable: false,
                    },
                ],
            }),
        );
    }

    // UNDO
    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.dropTable('appointments');
    }
}

/**
 *
 * Project Timeline (Migrations' Example)
 *
 * 1. Week: Agendamentos
 * 2. Week: User
 * 3. Week: New developer enters the team
 * 4. Week: Purchse
 *
 */

```

## Run Migration - Terminal

```
yarn typeorm migration:run

```

## Migrations - other commands

```
yarn typeorm migration:show
yarn typeorm migration:rever
 
```



---

## ORM - Create Users

```
yarn typeorm migration:create -n CreateUsers
```

## In the Mirgration
```

```