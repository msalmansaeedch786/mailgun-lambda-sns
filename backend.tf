# The backend terraform will use to store stack state. It should be kept on cloud
# if using CI/CD and runners so state is central.

# Note: As this is the first bit that gets loaded, variables are not allowed
#     to be used here, hence anytime the account needs to be changed a manual
#     update would be required here.
#

terraform {
  backend "s3" {
    bucket = "receeve-terraform-state-246168929807"
    key    = "terraform/terraform.tfstate"
    region = "eu-west-1"
  }
}
