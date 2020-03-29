file=/home/ec2-user/prod-batch/src/conf/Env.py
: > $file

SLACK_WEBHOOK_URL=`sudo -u ec2-user aws ssm get-parameters --name slack_webhook_url --query "Parameters[*].{Value: Value}" --output text`
echo "SLACK_WEBHOOK_URL=\"$SLACK_WEBHOOK_URL\"" >> $file
