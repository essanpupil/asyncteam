#!/usr/bin/env bash
echo "***********************************************"
echo "***************** install *********************"
echo "***********************************************"

echo "***********************************************"
echo "---apt update e upgrade---"
echo "***********************************************"
apt-get -y update

echo "***********************************************"
echo "---OS dependencies---"
echo "***********************************************"
apt-get -y install python3-pip
apt-get -y install python3-dev python3-setuptools
# .....
# .....
# .....
# .....

echo "***********************************************"
echo "---install dependencies (including django)  ---"
echo "***********************************************"
pip install --upgrade pip
pip install -r requirements.txt

echo "***********************************************"
echo "---        GECKODRIVER (for tests)          ---"
echo "***********************************************"

if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root" 1>&2
    exit 1
fi

cd ~
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar xvjf geckodriver-v0.24.0-linux64.tar.gz

mv geckodriver-v0.24.0-linux64 /usr/local/share
ln -sf /usr/local/share/geckodriver-v0.24.0-linux64/geckodriver /usr/local/bin
echo "---    GECKODRIVER Finished    ---"

echo "***********************************************"
echo "---          Done Installing Stuff          ---"
echo "***********************************************"

pip freeze
