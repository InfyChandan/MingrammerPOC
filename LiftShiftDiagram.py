from diagrams import Cluster, Diagram
from diagrams.azure.compute import VM
from diagrams.azure.network import Subnets, VirtualNetworks
from diagrams.azure.security import KeyVaults
from diagrams.azure.identity import ActiveDirectory

with Diagram("Cross-Tenant Secure Access with Private Endpoints", show=False):
    with Cluster("Tenant A"):
        with Cluster("Virtual Network A"):
            vnet_a = VirtualNetworks("Virtual Network A")
            subnet_a = Subnets("Subnet A")
            vm_a = VM("VM A")

            vnet_a - subnet_a
            subnet_a - vm_a

    with Cluster("Tenant B"):
        with Cluster("Virtual Network B"):
            vnet_b = VirtualNetworks("Virtual Network B")
            subnet_b = Subnets("Subnet B")
            vm_b = VM("VM B")

            vnet_b - subnet_b
            subnet_b - vm_b

    with Cluster("Cross-Tenant Secure Access"):
        key_vault = KeyVaults("Key Vault")
        aad = ActiveDirectory("Azure Active Directory")

        vm_a - key_vault
        vm_b - key_vault
        aad - key_vault
