import boto3
from dotenv import load_dotenv
import os

load_dotenv()
client = boto3.client('textract', region_name=os.getenv("AWS_REGION"))

def textract_text(file_bytes, filename):
    response = client.analyze_document(
        Document={'Bytes': file_bytes},
        FeatureTypes=["FORMS"]
    )
    lines = [block["Text"] for block in response["Blocks"] if block["BlockType"] == "LINE"]
    return "\n".join(lines)
