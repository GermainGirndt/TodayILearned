
brew install coreutils curl git

brew install asdf

echo -e "\n. $(brew --prefix asdf)/asdf.sh" >> ~/.bash_profile




echo -e "\n. $(brew --prefix asdf)/etc/bash_completion.d/asdf.bash" >> ~/.bash_profile




arch -x86_64 asdf install nodejs 12.22.12


/usr/sbin/softwareupdate --install-rosetta --agree-to-license
arch -x86_64 brew config


Docker BuildKit.
docker buildx create --name my_builder
docker buildx use my_builder
docker buildx inspect --bootstrap


https://www.postman.com/downloads/

