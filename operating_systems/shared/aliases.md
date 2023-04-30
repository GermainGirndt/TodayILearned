### Profile

```
export APPLICATION_INSTALL_HOME="$HOME/installs"
export SOURCE_CODE_HOME="$HOME/source"

# Fig pre block. Keep at the top of this file.
[[ -f "$HOME/.fig/shell/zprofile.pre.zsh" ]] && builtin source "$HOME/.fig/shell/zprofile.pre.zsh"
eval "$(/opt/homebrew/bin/brew shellenv)"

### Installs
MAVEN_HOME="$APPLICATION_INSTALL_HOME/apache-maven-3.8.7"
MAVEN_BINARY_HOME="$MAVEN_HOME/bin"

### Apps aliases
alias python="python3"

### Z Profile File
alias codealias="code $HOME/.zprofile"
alias codeprofile="code $HOME/.zprofile"

### Projects
export TODAY_I_LEARNED_HOME="$SOURCE_CODE_HOME/TodayILearned"
export FLIGHT_WATCHER_HOME="$SOURCE_CODE_HOME/flight_watcher"


alias cdsource="cd $SOURCE_CODE_HOME"
alias cdinstalls="cd $APPLICATION_INSTALL_HOME"
alias codeinstalls="code $APPLICATION_INSTALL_HOME"


alias cdtil="cd $TODAY_I_LEARNED_HOME"
alias codetil="code $TODAY_I_LEARNED_HOME"

alias cdflight="cd $FLIGHT_WATCHER_HOME"
alias codeflight="code $FLIGHT_WATCHER_HOME"
alias cdflightapi="cd $FLIGHT_WATCHER_HOME/flight_watcher_api"
alias cdflightweb="cd $FLIGHT_WATCHER_HOME/flight_watcher_web"



### Docker
export DOCKER_DEFAULT_PLATFORM=linux/amd64


PATH="$PATH:$MAVEN_BINARY_HOME"


### Functions

# kill process listening on port
alias kill-port='
kill_process () {
    sudo kill -9 $(sudo lsof -t -i:$1);
}
kill_process '


alias get-ip='
ip_local_one=$((hostname -I | grep -oP "([^\s]+)" | head -1) 2>/dev/null)
ip_local_two=$(ipconfig getifaddr en0)
ip_local_three=$(ipconfig getifaddr en1)

ip_externa_onel=$(curl --silent http://checkip.amazonaws.com)
ip_external_two=$(curl --silent ifconfig.me)

echo "local     hostname     =>  ${ip_local_one}"
echo "local     eth0         =>  ${ip_local_two}"
echo "local     eth1         =>  ${ip_local_three}"
echo "external  aws          =>  ${ip_externa_onel}"
echo "external  ifconfig.me  =>  ${ip_external_two}"
'
```
