file=/home/ec2-user/prod-batch/src/conf/Env.py
: > $file

for key in SLACK_WEBHOOK_URL MYSQL_HOST MYSQL_PORT MYSQL_DB MYSQL_USER MYSQL_PASSWORD
do
value=`sudo -u ec2-user aws ssm get-parameters --name $key --query "Parameters[*].{Value: Value}" --output text`
echo "$key=\"$value\"" >> $file
done
