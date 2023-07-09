#!/usr/bin/env bash

# Install Nginx if not already installed
if ! dpkg -s nginx >/dev/null 2>&1; then
	    apt-get update
	        apt-get install -y nginx
fi

# Create necessary folders
web_static_dir="/data/web_static"
releases_dir="$web_static_dir/releases"
shared_dir="$web_static_dir/shared"
test_dir="$releases_dir/test"

mkdir -p "$test_dir"
echo "Hello, web_static!" > "$test_dir/index.html"

# Create or recreate symbolic link
current_dir="$web_static_dir/current"
if [ -L "$current_dir" ]; then
	    unlink "$current_dir"
fi
ln -sf "$test_dir" "$current_dir"

# Set ownership of /data/ folder recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
sed -i '/location \/ {/a\\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}\n' "$config_file"

# Restart Nginx
systemctl restart nginx
