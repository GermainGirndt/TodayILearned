# Configuring a new user for deploy

```
sudo apt update
sudo apt upgrade
adduser new_user_name
usermod -aG sudo deploy
cd home/new_user_name
mkdir .ssh
chrown deploy:deploy .ssh
cp ~/.ssh/authorized_keys /home/new_user_name/.ssh
chrown deploy:deploy authorized_keys
exit
ssh new_user_name@IP
```
