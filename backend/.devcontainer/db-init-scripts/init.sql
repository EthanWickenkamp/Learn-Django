-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS '${MYSQL_DATABASE}';

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS '${MYSQL_USER}'@'%' IDENTIFIED BY '${MYSQL_PASSWORD}';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON '${MYSQL_DATABASE}'.* TO '${MYSQL_USER}'@'%';
FLUSH PRIVILEGES;