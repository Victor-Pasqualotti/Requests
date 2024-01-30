import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

import pandas as pd
from io import BytesIO
import requests

import boto3

import openpyxl

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

payload = {'modalidade': 'Lotofácil'}
headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en,pt-BR;q=0.9,pt;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#'Connection': 'keep-alive',
'Host': 'servicebus2.caixa.gov.br',
'Origin': 'https://loterias.caixa.gov.br',
'Referer': 'https://loterias.caixa.gov.br/'}

#'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Lotof%C3%A1cil'
r = requests.get('https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=Lotof%C3%A1cil', data=payload, headers=headers, verify=False)

df = pd.read_excel(BytesIO(r.content))

s3 = boto3.client('s3')
s3.put_object(Bucket='s3-wrk-vpb-versioning-disabled', Key='workspacedb/wrk-api-caixa.csv', Body=df.to_csv(index=False))

job.commit()