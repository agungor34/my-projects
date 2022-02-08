#!/bin/bash

yum update -y
yum install -y git
pip3 install flask
cd /home/ec2-user
git clone https://github.com/agungor34/my-projects.git
chown -R ec2-user.ec2-user /home/ec2-user/my-projects
cd /home/ec2-user/my-projects/python/hands-on/flask/flask-04-handling-forms-POST-GET-Methods/Flask_GET_POST_Methods
sed -i 's/app.run(debug=True)/app.run(host="0.0.0.0")/g' app.py
python3 app.py &
yum install -y httpd
FOLDER="https://raw.githubusercontent.com/agungor34/my-projects/main/aws/projects/Project-101-kittens-carousel-static-website-ec2/static-web"
cd /var/www/html
wget $FOLDER/index.html
wget $FOLDER/akif.png
wget $FOLDER/cat0.jpg
wget $FOLDER/cat1.jpg
wget $FOLDER/cat2.jpg
wget $FOLDER/cat3.png
sed -i 's/Listen 80/Listen 8080/g' /etc/httpd/conf/httpd.conf
systemctl start httpd
amazon-linux-extras install nginx1 -y
cd /usr/share/nginx/html
chmod -R 777 /usr/share/nginx/html
rm index.html
wget https://raw.githubusercontent.com/awsdevopsteam/ngniex/master/index.html
wget https://raw.githubusercontent.com/awsdevopsteam/ngniex/master/ryu.jpg
systemctl start nginx
