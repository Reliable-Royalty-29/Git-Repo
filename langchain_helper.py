import os
from langchain_openai import AzureOpenAI
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


OPENAI_API_VERSION = "2023-12-01-preview"
azure_openai_api_key = os.environ.get('AZURE_OPENAI_API_KEY')

llm = AzureOpenAI(
    deployment_name="Dheeman",
    api_version=OPENAI_API_VERSION,
    azure_endpoint="https://d29.openai.azure.com/",
    temperature=0.7
)

def test(cuisine):
    # Define PromptTemplate for restaurant name suggestion
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    # Create LLMChain for restaurant name suggestion
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Define PromptTemplate for menu items suggestion
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}"
    )

    # Create LLMChain for menu items suggestion
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Create SequentialChain with both LLMChain instances
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"]
    )

    # Execute the chain with the input value
    res = chain({"cuisine": cuisine})

    return res

if __name__ == "__main__":
    print(test("Indian"))

