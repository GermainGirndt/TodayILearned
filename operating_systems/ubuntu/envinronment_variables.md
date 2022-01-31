# Environment Variables

### Setting multiple environment variables from a .env file

Requirement:

.env file

```
A_VARIABLE=VALUE
ANOTHER_VARIABLE=VALUE
A_THIRD_VARIABLE=VALUE
```

Command:

```
set -o allexport; source .env; set +o allexport
```

Note: the variables doesn't persist by reboot
For that, add this command to .profil or .bashrc
