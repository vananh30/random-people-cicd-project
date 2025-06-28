variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "eu-north-1"
}

variable "aws_profile" {
  description = "AWS CLI profile name"
  type        = string
  default     = "default"
}

variable "bucket_name" {
  description = "Raw data bucket name"
  type        = string
  default     = "random-people-cicd-project-bucket"
}
