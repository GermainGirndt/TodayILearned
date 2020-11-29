# MySQL CLI

### Connect

1. `mysql -u strapi -pstrapi -h 0.0.0.0 --port=33060 --protocol=TCP`
2. `service mysqld -u root -p12345678`


### Restart

`service mysql restart`

### Export DB Dump
`mysqldump -u username -p databasename > backup.sql`

### Import Dump to current DB
`mysql -h mysql -u strapi -pstrapi strapi < backup.sql`


### Check bind-address
`mysqld --verbose --help | grep bind-address`

