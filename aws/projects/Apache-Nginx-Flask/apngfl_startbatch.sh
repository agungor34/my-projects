#!/bin/bash

yum update -y
yum install -y git
git clone https://github.com/agungor34/my-projects.git

chown -R ec2-user.ec2-user /home/ec2-user/my-projects
cd /home/ec2-user/my-projects/aws/projects/Apache-Nginx-Flask/flask-04-handling-forms-POST-GET-Methods/Flask_GET_POST_Methods
sed -i 's/app.run(debug=True)/app.run(host="0.0.0.0")/g' app.py
pip3 install flask
python3 app.py &

yum install -y httpd
sed -i 's/Listen 80/Listen 8080/g' /etc/httpd/conf/httpd.conf
cp /home/ec2-user/my-projects/aws/projects/Apache-Nginx-Flask/static-web/* /var/www/html/
systemctl start httpd

amazon-linux-extras install nginx1 -y
chmod -R 777 /usr/share/nginx/html
rm index.html
cp /home/ec2-user/my-projects/aws/projects/Apache-Nginx-Flask/cikolata/* /usr/share/nginx/html/
my_ip=`curl http://checkip.amazonaws.com`
sed -i "s/link11/$my_ip/g" /usr/share/nginx/html/index.html
systemctl start nginx
