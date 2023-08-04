#!/usr/bin/python3

# MySQL root user credentials
MYSQL_ROOT_USER="root"
MYSQL_ROOT_PASSWORD="your_root_password"  # Replace with your actual root password

# Database and User information
DB_NAME="hbnb_test_db"
DB_USER="hbnb_test"
DB_PASSWORD="hbnb_test_pwd"

# Create the database hbnb_test_db if it doesn't exist
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"

# Create the user hbnb_test if it doesn't exist
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "CREATE USER IF NOT EXISTS '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASSWORD';"

# Grant all privileges on hbnb_test_db to hbnb_test user
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_USER'@'localhost';"

# Grant SELECT privilege on performance_schema to hbnb_test user
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "GRANT SELECT ON performance_schema.* TO '$DB_USER'@'localhost';"

echo "MySQL server is prepared for the project."
