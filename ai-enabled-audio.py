from diagrams import Diagram,Node
from diagrams.aws.storage import SimpleStorageServiceS3
from diagrams.aws.compute import Lambda
from diagrams.aws.ml import Transcribe
from diagrams.aws.ml import Translate
from diagrams.aws.ml import Comprehend
from diagrams.aws.ml import Kendra
from diagrams.aws.mobile import APIGateway
from diagrams.aws.database import Dynamodb

with Diagram("Ecommerce Search", filename="ai_enabled_audio"):
    # Data source
    data_source = Node("Any Device")
    another_data_source = Node("Users")
    raw_audios3_bucket= SimpleStorageServiceS3("raw_audios3")
    transcribed_audio= SimpleStorageServiceS3("transcribed_audio")
    translated_audio = SimpleStorageServiceS3("translated_audio")
    audio_job_lambda= Lambda("audio_job_lambda")
    text_job_lambda= Lambda("text_job")
    insight_job_lambda= Lambda("insight_job")
    get_match_lambda= Lambda("get_match_function")

    transcribe = Transcribe("transcribe")
    translate = Translate("translate")
    comprehend = Comprehend("comprehend")
    kendra= Kendra("kendra")
    apigateway= APIGateway("api_gateway")
    dynamodb= Dynamodb("dynamodb")

    

    
    data_source >> raw_audios3_bucket >>  [ transcribe - audio_job_lambda] >> transcribed_audio >> [translate-text_job_lambda] >> translated_audio >> [comprehend-insight_job_lambda] 

    audio_job_lambda >> dynamodb
    text_job_lambda >> dynamodb
    insight_job_lambda >> dynamodb

    another_data_source - apigateway >> get_match_lambda
    dynamodb - get_match_lambda >>  kendra
