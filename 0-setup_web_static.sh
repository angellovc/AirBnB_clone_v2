#!/usr/bin/env bash
#sets up the web servers for the deployment of web_static
if ! command -v nginx &> /dev/null
then
	apt-get install nginx -y
fi
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "
<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>
" > /data/web_static/releases/test/index.html
ln -s -f /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server;/ a location /hbnb_static/ {alias /data/web_static/current/;}' /etc/nginx/sites-available/default
/etc/init.d/nginx restart
