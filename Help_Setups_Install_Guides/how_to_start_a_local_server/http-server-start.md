Starting web servers in the terminal can be done in multiple ways depending on the server software you're using. Here's a list of common web servers with commands to start them. Keep in mind that you need to have these servers installed on your system:

1. Apache HTTP Server:
   Start Apache:
   On macOS with Homebrew:
   bash
   sudo apachectl start
   On Linux (Ubuntu/Debian):
   bash
   sudo systemctl start apache2
   or
   bash
   sudo service apache2 start
   Stop Apache:
   sudo apachectl stop (macOS with Homebrew)
   sudo systemctl stop apache2 or sudo service apache2 stop (Linux)
   Restart Apache:
   sudo apachectl restart (macOS with Homebrew)
   sudo systemctl restart apache2 or sudo service apache2 restart (Linux)

2. Nginx:
   Start Nginx:
   On macOS with Homebrew:
   bash
   sudo nginx
   On Linux (Ubuntu/Debian):
   bash
   sudo systemctl start nginx
   or
   bash
   sudo service nginx start
   Stop Nginx:
   sudo nginx -s stop (macOS with Homebrew)
   sudo systemctl stop nginx or sudo service nginx stop (Linux)
   Reload Nginx (to apply configuration changes without stopping):
   sudo nginx -s reload (macOS with Homebrew)
   sudo systemctl reload nginx or sudo service nginx reload (Linux)

3. Python's SimpleHTTPServer or http.server:
   Python 2 (SimpleHTTPServer):
   bash
   python -m SimpleHTTPServer \[port]
   By default, it uses port 8000.
   Python 3 (http.server):
   bash
   python3 -m http.server \[port]
   Again, default port is 8000 if not specified.

4. Node.js HTTP Server:
   If you have Node.js installed and want to start a quick server:

bash
node -e "require('http').createServer((req, res) => res.end('Hello World')).listen(3000)"

Or with Express.js, if installed:

bash
node server.js
Assuming server.js is your Express server script.

5. Lighttpd:
   Start:
   bash
   sudo lighttpd -f /etc/lighttpd/lighttpd.conf
   Stop:
   bash
   sudo killall lighttpd

6. PHP Built-in Server:
   If you're working with PHP:

bash
php -S localhost:8000

7. Ruby WEBrick:
   For Ruby users with WEBrick:

bash
ruby -run -e httpd . -p 5000

General Notes:
Port Conflicts: Each server must run on a unique port unless you're using different IP addresses or virtual hosts. The default port for web servers is 80 for HTTP and 443 for HTTPS, but for testing, you'll often use higher ports like 8000, 3000, etc.
Permissions: Many of these commands require sudo due to their need to bind to lower port numbers or access system files.
Status Check: For systemctl managed services, you can check status with sudo systemctl status \<service\_name>.
Configuration: Each server has its configuration file(s) which can be edited for more complex setups, like setting up SSL, virtual hosts, etc.

This list isn't exhaustive as there are many more web servers (like Gunicorn for Python, Unicorn for Ruby, etc.), but these are among the most commonly used. If you're unsure which server you've installed, you might need to check your installation history or look in /etc/ for configuration files.
