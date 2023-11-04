spe_aliases=("git" "docker" "kube" "asusctl")

if [[ " ${spe_aliases[*]} " == *" $1 "* ]]; then
    echo "hello"
fi
