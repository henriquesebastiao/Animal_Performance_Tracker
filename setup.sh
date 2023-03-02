#!/bin/bash

# Verifica a distribuição Linux
if [ -f /etc/lsb-release ]; then
    # Ubuntu ou Debian
    sudo apt-get update
    sudo apt-get install python3
elif [ -f /etc/redhat-release ]; then
    # Red Hat, CentOS ou Fedora
    sudo yum update
    sudo yum install python3
elif [ -f /etc/arch-release ]; then
    # Arch Linux
    sudo pacman -Syu
    sudo pacman -S python
else
    # Distribuição desconhecida
    echo "Distribuição Linux desconhecida"
fi
