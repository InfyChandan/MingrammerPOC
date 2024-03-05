from diagrams import Diagram,Cluster,Node
from diagrams.azure.web import AppServices
from diagrams.azure.ml import BotServices
from diagrams.azure.web import Search
from diagrams.azure.database import SQLDatabases
from diagrams.azure.ml import CognitiveServices


with Diagram("Ecommerce Search", filename="ecommerce_search"):
    # Data source
    data_source = Node("Any Device")

    web_app= AppServices("Web App")
    sql_database=SQLDatabases("Azure Sql DB")

    botservices= BotServices("botservices")
    search_service= Search("Azure AI search")
    cognitive_services= CognitiveServices("Azure AI services")

    data_source >> web_app
    data_source >> botservices
    
    [web_app - sql_database]-search_service - [cognitive_services] 
    [web_app >> search_service] -cognitive_services
    [botservices >> search_service] - cognitive_services

