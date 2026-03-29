module "label" {
  source  = "cloudposse/label/null"
  version = "0.25.0"
  namespace   = var.namespace
  environment = var.environment
  name        = var.name
  delimiter   = "-"
}

module "dynamodb_table" {
  source     = "./modules/dynamodb"
  table_name = module.label.id 
  hash_key   = "id"
}

data "archive_file" "lambda_zip" {
  type        = "zip"
  source_dir  = "${path.module}/src"
  output_path = "${path.module}/lambda.zip"
}

resource "aws_iam_role" "lambda_role" {
  name = "${module.label.id}-lambda-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{ Action = "sts:AssumeRole", Effect = "Allow", Principal = { Service = "lambda.amazonaws.com" } }]
  })
}

resource "aws_iam_role_policy" "dynamodb_access" {
  name   = "${module.label.id}-dynamodb-policy"
  role   = aws_iam_role.lambda_role.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action   = ["dynamodb:PutItem", "dynamodb:GetItem", "dynamodb:Scan"]
      Effect   = "Allow"
      Resource = module.dynamodb_table.table_arn 
    }]
  })
}

resource "aws_lambda_function" "this" {
  filename         = data.archive_file.lambda_zip.output_path
  function_name    = "${module.label.id}-function"
  role             = aws_iam_role.lambda_role.arn
  handler          = "index.handler"
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  runtime          = "nodejs20.x"
  environment { variables = { TABLE_NAME = module.dynamodb_table.table_name } }
}
