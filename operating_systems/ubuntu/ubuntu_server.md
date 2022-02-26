### Setting up a Server

- **Create an server instance**
- Log onto it
- Run the following commands

```
sudo su - # super user


sudo apt update
apt install net-tools # for quering ports
sudo apt install nginx
```

### Check which program is listening on the port 80

```
sudo netstat -plant | grep 80
```

### Check the public ip

```
curl --silent http://checkip.amazonaws.com

```

### Installing Project Dependencies

#### ASDF

```
# Install ASDF
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.9.0

echo ". $HOME/.asdf/asdf.sh" >> ~/.bashrc
echo ". $HOME/.asdf/completions/asdf.bash" >> ~/.bashrc

# Reload bashrc
source ~/.bashrc


# Install Node

apt-get install dirmngr gpg curl gawk
asdf plugin add nodejs https://github.com/asdf-vm/asdf-nodejs.git


asdf list all nodejs # all available
asdf list nodejs # all installed

asdf install nodejs 16.13.2 # install node version 16.13.2

asdf global nodejs 16.13.2 # set nodejs version


node --version # check the version without nodeJS

# Verify the current versions of the installed programs
asdf current



### Yarn

asdf plugin-add yarn
asdf install yarn 1.22.17
asdf global yarn 1.22.17
yarn --version


```

### Install Docker

```
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null


sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

sudo docker run hello-world
```

### Configure Nginx

```
cd /etc/nginx/sites-available
nano default
```

```
server {
    listen 80;
    server_name _;

    location / {
          # First attempt to serve request as file, then
          # as directory, then fall back to displaying a 404.
          proxy_set_header X-Forwarded-For $remote_addr;
          proxy_set_header Host $http_host;

          proxy_pass http://172.31.28.113:8080;

          try_files $uri /index.html; #also or just add
    }

}


```

```
systemctl status nginx
systemctl restart nginx
```

```
yarn build


```

- Copy Build folder projects into var/www/html

```
sudo cp -r /home/ubuntu/your-project-folder/build/. /var/www/html
```

### Firewall rules

```
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https

sudo ufw status
```

### STL Certificate

Pre-Requisite: A registered domain pointing to the server.

Cert Bot -> has a link for each operating system and web server

`cat /etc/issue` for getting ubuntu version

### Stable Node Js Server

Install pm2 bib globally
Call it with the server file (so that it lives forever, also after reebots and power shortages)

Another commands:

```
pm2 start ~/app/server.js --name my_server
pm2 status
pm2 stop 0 # stops process 0
pm2 delete

pm2 startup # get link for always running pm2 by startup

pm2 save # for it to remember
```
