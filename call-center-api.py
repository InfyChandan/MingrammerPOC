from diagrams import Diagram, Cluster
from diagrams.azure.compute import VM
from diagrams.azure.database import CosmosDb
from diagrams.azure.general import APIManagement
from diagrams.azure.analytics import StreamAnalytics, SynapseAnalytics
from diagrams.azure.web import AppServices
from diagrams.azure.identity import AzureActiveDirectory
from diagrams.onprem.client import Users
from diagrams.azure.database import BlobStorage

with Diagram("Call Center Analytics with OpenAI", show=False):
    with Cluster("Azure"):
        with Cluster("Data Ingestion"):
            stream_analytics = StreamAnalytics("Stream Analytics")
            openai_api = APIManagement("OpenAI API")
            openai_vm = VM("OpenAI VM")

            stream_analytics >> openai_api >> openai_vm

        with Cluster("Data Storage"):
            cosmos_db = CosmosDb("Cosmos DB")

        with Cluster("Data Processing"):
            synapse_analytics = SynapseAnalytics("Synapse Analytics")

            cosmos_db >> synapse_analytics

        with Cluster("Application"):
            app_services = AppServices("App Services")

        with Cluster("Identity & Access"):
            aad = AzureActiveDirectory("Azure AD")

        with Cluster("User"):
            users = Users("Users")

            users >> app_services
            aad >> app_services
