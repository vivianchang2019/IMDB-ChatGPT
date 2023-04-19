"""
使用ChatGPT建置個人(IMDB電影)知識庫

運行流程:
1. 安裝使用的套件
2. 定義function，使用GPT 3.5 模型建立個人知識庫。
3. 定義function，使用GPT建立問答方式。
4. 提供使用API所需的密鑰與數據來源(個人資料庫)。
5. 使用功能

Build a personal (IMDB movie) knowledge base using ChatGPT.

Process:
1. Install required packages.
2. Define functions to create a personal knowledge base using GPT 3.5 model.
3. Define functions to establish question-and-answer format using GPT.
4. Provide the API key and data source (personal database) required for use of API.
5. Use the Customerized AI.

"""

from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI
from api_secrets import *
import sys
import os


# 1. 安裝使用的套件(Install required packages.)

# !pip install llama-index
# !pip install langchain


# 2. 定義function，使用GPT模型建立個人知識庫。
# (Define functions to create a personal knowledge base using GPT 3.5 model.)

def construct_index(directory_path):
    # set maximum input size
    max_input_size = 4096
    # set number of output tokens
    num_outputs = 2000
    # set maximum chunk overlap
    max_chunk_overlap = 20
    # set chunk size limit
    chunk_size_limit = 600 

    # define prompt helper
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    # define LLM
    # llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="text-davinci-003", max_tokens=num_outputs))
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="gpt-3.5-turbo", max_tokens=num_outputs))
     
    documents = SimpleDirectoryReader(directory_path).load_data()
    
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)

    index.save_to_disk('index.json')

    return index

# 3. 定義function，使用GPT建立問答方式。
# (Define functions to establish question-and-answer format using GPT.)

def ask_ai():
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    Status = True
    
    while Status: 
        query = input("What do you want to ask? >> ")
        
        # when user input is 'stop', exit the loop.
        if query == 'stop':   
            Status = False 
            print(f'Goodbye!')

        else:
            response = index.query(query)
            print(response.response)
            print('='*20)


# 4. 提供使用API所需的密鑰與數據來源(個人資料庫)。
# (Provide the API key and data source (personal database) required for use of API.)

os.environ["OPENAI_API_KEY"] = chatgpi_api_key
construct_index("data")


if __name__ == '__main__':

    # 5.使用功能(Use the Customerized AI.)
    """
    # Here shows Three examples of questions to test the AI:
    1. According to user data, what is the top 1 to top 3 movie in IMDB ranking? (from webscraping data at 2023/04/18)
    2. Which movie get the highest likes numbers of all movie?  (Likes data is a fake data given by user.)
    3. Who is the director of the movie "亂世兒女"?
    """
    ask_ai()
