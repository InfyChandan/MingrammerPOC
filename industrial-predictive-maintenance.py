from diagrams import Diagram,Node
from diagrams.aws.iot import IotGreengrass
from diagrams.aws.compute import Lambda
from diagrams.aws.iot import IotFactory
from diagrams.aws.iot import IotLambda
from diagrams.aws.ml import Sagemaker
from diagrams.aws.iot import IotCore
from diagrams.aws.analytics import KinesisDataFirehose
from diagrams.aws.analytics import KinesisDataStreams
from diagrams.aws.analytics import KinesisDataAnalytics
from diagrams.aws.analytics import Athena
from diagrams.aws.analytics import Quicksight
from diagrams.aws.integration import SimpleNotificationServiceSns
from diagrams.aws.compute import LambdaFunction
from diagrams.aws.storage import SimpleStorageServiceS3

with Diagram("industrial-predictive-maintainance", filename="industrial_predective_mantainance"):
    
    iot_greengrass = IotGreengrass("aws iot greengrass")
    iot_core= IotCore("aws iot core")
    firehose= KinesisDataFirehose("amazon kinesis data firehose")
    s3= SimpleStorageServiceS3("amazon s3")
    athena= Athena("amazon athena")
    quick_sight= Quicksight("amazon quicksight")
    data_stream = KinesisDataStreams("amazon kinesis data stream")
    data_analytics= KinesisDataAnalytics("amazon kinesis data analytics")
    firehose2= KinesisDataFirehose("amazon kinesis data firehose")
    aws_lambda= Lambda("aws lambda")
    sagemaker = Sagemaker("sagemaker")
    aws_lambda_function= LambdaFunction("Lambda Function")
    sns = SimpleNotificationServiceSns("SNS")
    factory_machine = IotFactory("factory")
    
    factory_machine >> iot_greengrass >> iot_core >>firehose >> s3 >> athena >> quick_sight
    iot_core >> data_stream >> data_analytics >> aws_lambda >> sns
    s3 >> sagemaker >> aws_lambda_function
    data_analytics >> firehose2 >> s3