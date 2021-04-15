# Mailgun - Lambda - SNS

AWS Lambda Function that is proxied to an AWS API Gateway sends notification using AWS SNS triggering on Webhooks and stores the results in AWS S3. 

## Getting Started

This project is build and AWS Lambda Function that triggered when an email goes out via [Mailgun](mailgun.com). Once it’s out Mailgun sends various events back (open, clicked, etc). The moment wehn an an email sent out via Mailgun, we now have those events with us via webhooks, hitting an API Gateway and that information is proxied to a Lambda. The Lambda will firt of all save a copy of the raw webhook and store it in any storage avilable i.e AWS S3 and publish a transformed version of the raw webhook into AWS SNS or using any publishing service.

## Design Choices and Implementation

For the provision of the infrastrcuture, Terraform is being used for IaC (Infrastructure as Code) to setup different AWS Services inlucding:

* AWS Lambda Function
* AWS API Gatewat
* AWS SSM
* AWS SNS
* AWS S3

Lambda function payload (**lambda_function_payload.zip**) contains the package for the deployment including:

- aws_s3.py (Contains AWS S3 Storage Service)
- aws_sns.py (Contains AWS SNS Publishing Service)
- aws_ssm.py (Contains AWS SSM Secret Management Service)

The lambda function first parse the event and extract the requried values then it validates the webhook from mailgun. Store the event (raw webhook) data into the AWS S3 data store, also notify the endpoint user about different events from mailgun webhooks through AWS SNS publishing service.

## Architecture Flow Diagram

                           
                            ___________________
      ______________       |  ______    _____  |        _______________ 
     |              |      | |DNS   |  |TLS  | |       |  Cloudflare   | 
     |   Clients    |----->| |Server|..|Tran | |-----> |DNS (TLS)- 853 |
     |______________|      | |_(53)_|  |sport| |       |_______________|
                           |___________________|
                           


## Terraform Setup

***Terraform should be installed on the machine, you want to setup the project alongwith the aws cli installed and default profile is set with appropriate Access and Secret Keys***

To run this project:

- Initialize the terraform with plugin and provider:
```
  terraform init
```

- To confirm what resources are going to be added in the infrastructure:
```
  terraform plan
```

- To validate the infrastructure code for any error:
```
  terraform validate
```

- To apply the infrastructure changes:
```
  terraform apply
```

- To destroy the infrastructure changes:
```
  terraform destroy
```

## Testing:

After the infrastructure is deployed successfully:

- Make sure to accept the confirmation email from AWS SNS Service

- Terraform will show you the API Invoke URL for the POST method, copy the URL and attach it with the Mailgun dashboard Sending Webhooks. Afterwards there is Mailgun sending python code **mailgun.py** in mailgun folder. 

Run it:

```
  python ./mailgun/mailgun.py
```
***Note: Configure the code properly with the appropriate values i.e YOUR_DOMAIN_NAME and YOUR_API_KEY***