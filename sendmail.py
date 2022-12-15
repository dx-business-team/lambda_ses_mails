import boto3
import os
import json

ADDR_TO = os.environ['MailRecipient']  # 送信先
ADDR_FROM = os.environ['MailSender']  # 送信元
SUBJECT = 'SESから送信しました。'  # 見出し（タイトル）
MESSAGE = '本文です。'  # 本文
REGION = 'us-east-1'  # リージョン指定


def send_email(source, addr_to, subject, body):
    client = boto3.client('ses', region_name=REGION)

    response = client.send_email(
        Source=source,
        Destination={
            'ToAddresses': [
                addr_to,
            ]
        },
        Message={
            'Subject': {
                'Data': subject,
            },
            'Body': {
                'Text': {
                    'Data': body,
                },
            }
        }
    )
    return response


def lambda_handler(event, context):
    r = send_email(ADDR_FROM, ADDR_TO, SUBJECT, MESSAGE)
    return r
