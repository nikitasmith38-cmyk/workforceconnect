#!/bin/bash

echo '=== WorkforceConnect Setup Script ==='

sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-dev python3-pip python3-venv default-libmysqlclient-dev build-essential mysql-server nginx -y
sudo service mysql start
sudo mysql -u root <<'EOF'
CREATE DATABASE IF NOT EXISTS workforcedb;
CREATE USER IF NOT EXISTS 'wfcuser'@'localhost' IDENTIFIED BY 'BootcampPass2025!';
GRANT ALL PRIVILEGES ON workforcedb.* TO 'wfcuser'@'localhost';
FLUSH PRIVILEGES;
USE workforcedb;
CREATE TABLE IF NOT EXISTS registrations (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(50) NOT NULL,
  submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
EOF

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install flask flask-mysqldb gunicorn
deactivate

echo 'Setup complete.'
echo 'Run: source venv/bin/activate && gunicorn --bind 127.0.0.1:5000 app:app'
