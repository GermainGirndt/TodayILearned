# Fig pre block. Keep at the top of this file.
[[ -f "$HOME/.fig/shell/zprofile.pre.zsh" ]] && builtin source "$HOME/.fig/shell/zprofile.pre.zsh"
export PROFILE_FILE="$HOME/.zprofile"
export ALIAS_DEFINITION_FILE="$PROFILE_FILE"
export APPLICATION_INSTALL_HOME="$HOME/installs"
export SOURCE_CODE_HOME="$HOME/source"

export STANDARD_SOURCE_FILE='~/.zprofile'

### Terminal

alias codeprofile="cd $PROFILE_FILE"
alias codealias="cd $ALIAS_DEFINITION_FILE"


### Installs
export JAVA_HOME="/usr/bin/java"
export MAVEN_HOME="$APPLICATION_INSTALL_HOME/apache-maven-3.8.7"
export MAVEN_BINARY_HOME="$MAVEN_HOME/bin"
export KUBERNETES_HOME="$APPLICATION_INSTALL_HOME/kubernetes"

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

alias condaactivate="source /Users/germaingirndt/installs/anaconda/anaconda3/bin/activate"
alias condadeactivate="conda deactivate"

### Docker
#export DOCKER_DEFAULT_PLATFORM=linux/amd64

### ASDF
. /opt/homebrew/opt/asdf/libexec/asdf.sh

### Path
PATH="$PATH:$MAVEN_BINARY_HOME:$KUBERNETES_HOME"

### Functions
alias reload-source="source $STANDARD_SOURCE_FILE"


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


check-ports() {
    if [ $# -eq 0 ]; then
        echo "Please provide at least one port number."
        return 1
    fi

    for port in "$@"
    do
        echo "Checking port: $port"

        echo "Using LSOF:"
        lsof -i :$port

        echo "Using NETSTAT:"
        netstat -tuln | grep :$port

        echo "----------------------------"
    done
}


scan-vulnerabilities() {
    if [ -z "$1" ]; then
        echo "Please provide an IP address."
        return 1
    fi

    nmap --script vuln $1
}


### Mac/ZSH Specific

eval "$(/opt/homebrew/bin/brew shellenv)"

# Fig post block. Keep at the bottom of this file.
[[ -f "$HOME/.fig/shell/zprofile.post.zsh" ]] && builtin source "$HOME/.fig/shell/zprofile.post.zsh"


kill-process() {
    if [ -z "$1" ]; then
        echo "You must provide a process name."
        return 1
    elif ! pgrep -x "$1" > /dev/null; then
        echo "No process found with name: $1"
        return 1
    fi
    local before=$(pgrep -x "$1" | wc -l)
    pkill "$1"
    local after=$(pgrep -x "$1" | wc -l)
    local killed=$((before - after))
    echo "Successfully terminated process: $1. Instances killed: $killed. Remaining instances: $after."
}
