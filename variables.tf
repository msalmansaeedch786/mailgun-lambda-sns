variable "aws_region" {
  type        = string
  description = "default region for the aws account"
}

variable "s3_bucket_name" {
  type        = string
  description = "name for the aws s3 bucket"
}

variable "sns_topic_name" {
  type        = string
  description = "name for the aws sns topic"
}

variable "sns_topic_subscription_protocol" {
  type        = string
  description = "protocol for aws sns topic subscription"  
}

variable "sns_topic_subscription_endpoint" {
  type        = string
  description = "endpoint for aws sns topic endpoint"
}

variable "lambda_function_name" {
  type        = string
  description = "name for aws lambda function"
}

variable "lambda_handler_name" {
  type        = string
  description = "name for aws lambda handler"
}

variable "iam_role_name" {
  type        = string
  description = "name for the aws iam role"
}

variable "iam_policy_name" {
  type        = string
  description = "name for the aws iam policy"  
}

variable "api_gateway_name" {
  type        = string
  description = "name for the aws api gateway"  
}

variable "ssm_webhook_signing_key_name" {
  type        = string
  description = "name for the aws ssm webhook signing key"  
}
