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
# get private ip address of ec2 instance using instance metadata
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& PRIVATE_IP=`curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/local-ipv4`
# get public ip address of ec2 instance using instance metadata
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& PUBLIC_IP=`curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4` 
# get date and time of server
DATE_TIME=`date`
# create a custom index.html file
echo "<body>
    <h1>Testing Application Load Balancer and Autoscaling</h1>
    <p>This web server is launched from launch template by Clarusway</p>
    <p>This instance is created at <b>$DATE_TIME</b></p>
    <p>Private IP address of this instance is <b>$PRIVATE_IP</b></p>
    <p>Public IP address of this instance is <b>$PUBLIC_IP</b></p>
</body>
</html>" >> /usr/share/nginx/html/index.html
my_ip=`curl http://checkip.amazonaws.com`
sed -i "s/link11/$PUBLIC_IP/g" /usr/share/nginx/html/index.html
systemctl start nginx
