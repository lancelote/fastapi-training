#!/bin/bash

# Update machine
apt update
apt upgrade -y
reboot

# Setup a new user
adduser pavel
usermod -aG sudo pavel
ufw allow OpenSSH
ufw enable
rsync --archive --chown=pavel:pavel ~/.ssh /home/pavel

# Login as a new user
apt install zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Install more dependencies
sudo apt install -y -q build-essential git unzip zip nload tree
sudo apt install -y -q python3-pip python3-dev python3-venv

# Extra security
sudo apt install fail2ban -y

ufw allow 22
ufw allow 80
ufw allow 443
ufw enable

# Web app file structure
sudo chmod 777 /apps
sudo mkdir -p /apps/logs/weather_api/app_log

# Prepare the venv
python3 -mvenv /apps/.venv
source /apps/.venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install --upgrade httpie glances
pip install --upgrade gunicorn uvloop httptools

# Deploy to /apps/app/ and then
git clone https://github.com/lancelote/fastapi-training.git /apps/app
pip install -r /apps/app/requirements.txt

# Copy and enable the daemon
cp /apps/app/src/ch08/server/units/weather.service /etc/systemd/system

# Start the app
systemctl start weather
systemctl status weather
systemctl enable weather

# Setup the public facing server (NGINX)
apt install nginx

# CAREFUL HERE. If you are using default, maybe skip this
rm /etc/nginx/sites-enabled/default

cp /apps/app/src/ch08/server/nginx/weather.nginx /etc/nginx/sites-enabled/
update-rc.d nginx enable
service nginx restart

# Optionally add SSL support via Let's Encrypt:
# https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04

add-apt-repository ppa:certbot/certbot
apt install python3-certbot-nginx
certbot --nginx -d weatherapi.talkpython.com
