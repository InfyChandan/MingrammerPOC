from diagrams import Diagram, Cluster
from diagrams.azure.storage import StorageAccounts
from diagrams.azure.analytics import SynapseAnalytics
from diagrams.azure.ml import CognitiveServices
from diagrams.azure.security import KeyVaults
from diagrams.azure.compute import FunctionApps



with Diagram("audio-to-text-data-analysis"):
    transcription_storage= StorageAccounts("transcription_storage")
    synapse_analytics= SynapseAnalytics("synapse_anlytics")
    cognitive_services= CognitiveServices("cognitive_services")
    azure_function = FunctionApps("function_app")
    processed_storage = StorageAccounts("processed_storage")

    # with Cluster ("azure services"):
    key_valuts= KeyVaults("key_valuts")
    azure_group = [cognitive_services >> cognitive_services] - key_valuts
    

    transcription_storage >> synapse_analytics - azure_group >> processed_storage >> synapse_analytics 
