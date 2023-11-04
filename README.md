# Better Aliases


Tired of aliases with a single world ? This is cool:
```bash
alias gcl='git clone --depth 1'
alias gc='git commit -m'
alias gp='git push origin master'
alias gl='git log --all --decorate --oneline --graph'

alias ap='asusctl profile -P Performance'
alias aq='asusctl profile -P Quiet'
```

But this is cooler:
```
$ git log 
>>Executing "git log --all --decorate --oneline --graph"

$ git init 
>>Executing git init

$ actl perf
>>Executing "asusctl profile -P Performance"

$ a quiet 
>>Executing "asusctl profile -P Quiet"
```

With a single configuration file !
```yaml
commands:
  git:
    all: git
    log: log --all --decorate --oneline --graph
  asusctl:
    all: asusctl
    perf: profile -P Performance
    quiet: profile -P Quiet
prefix:
  asusctl: ["a", "actl", "asusctl"]
```

(And a bit of modification in your .zsh/.bashrc file... Will be fixed)
```bash
# Special aliases
alias git="aliases git"
alias asusctl="aliases asuctl"
function command_not_found_handler() {
    aliases "$@"
}
```

