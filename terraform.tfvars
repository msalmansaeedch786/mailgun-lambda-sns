aws_region = "eu-west-1"

s3_bucket_name = "receeve-challenge-bucket"

sns_topic_name = "receeve_challenge_topic"

sns_topic_subscription_protocol = "email"
sns_topic_subscription_endpoint = "muhammad.salman@empglabs.com"

lambda_function_name = "receeve_challenge_lambda"
lambda_handler_name       = "lambda_handler.lambda_handler"

iam_role_name = "receeve_challenge_iam_role"

iam_policy_name = "receeve_challenge_iam_policy"

api_gateway_name = "receeve_challenge_api_gateway"

ssm_webhook_signing_key_name = "/receeve/signing_key"