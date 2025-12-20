from langchain_aws import ChatBedrockConverse

nova_lite = ChatBedrockConverse(
    model_id="eu.amazon.nova-lite-v1:0",
    temperature=0.5,
    region_name="eu-west-1"
)

nova_pro = ChatBedrockConverse(
    model_id="eu.amazon.nova-pro-v1:0",
    temperature=0.5,
    region_name="eu-west-1"
)