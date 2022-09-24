# Knex Migration - Sample

* **000_create_points.ts**
```

// Knex -> capitalized because it's a type
import Knex from 'knex';

export async function up(knex: Knex) {
    // CREATE TABLE
    return knex.schema.createTable('points', table => {
        table.increments('id').primary();
        // every collect point muss have an image
        table.string('image').notNullable();
        table.string('name').notNullable();
        table.string('email').notNullable();
        table.string('whatsapp').notNullable();
        table.decimal('latitude').notNullable();
        table.decimal('longitude').notNullable();
        table.string('city').notNullable();
        // 2 stands for max 2 characters
        table.string('uf', 2).notNullable();
    });
}

export async function down(knex:Knex) {
    // GO BACK
    return knex.schema.dropTable('point');
}

```

