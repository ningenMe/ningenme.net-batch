file=/home/ec2-user/prod-batch/.env
: > $file

SLACK_WEBHOOK_URL=`aws ssm get-parameters --name 'slack_webhook_url' --query "Parameters[*].{Value: Value}" --output text`
export SLACK_WEBHOOK_URL=$SLACK_WEBHOOK_URL
echo "SLACK_WEBHOOK_URL=$SLACK_WEBHOOK_URL" >> $file