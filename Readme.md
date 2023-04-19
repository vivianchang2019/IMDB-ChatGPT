## 使用ChatGPT建置個人(IMDB電影)知識庫AI
這個專案包含三個 Python 腳本，使用ChatGPT 3.5 建置個人(IMDB)電影知識庫AI。
可直接從Jupyter notebook版本，查閱代碼輸出結果。

腳本摘要如下: 

1. gpt_chatbot_Demo.ipynb : 簡單展示ChatGPI API的使用方式。
2. imdb_webscraper_Demo.ipynb: 從IMDb網站爬取電影資料。
3. imdb_gptbot_Demo.ipynb: 利用IMDb網站資料與ChatGPT，建置個人(IMDB)電影知識庫AI。

<br>

## [腳本說明]
### 1. gpt_chatbot_Demo.ipynb

**gpt_chatbot_Demo.ipynb** 是一個jupyter notebook，簡單的展示如何使用Python串接Open API的形式，來呼叫ChatGPI 3.5，並建立上下文相關聯的對答形式(建立如同使用Open AI網頁版ChatGPT的對答)。
<br>

### 2. imdb_webscraper
**imdb_webscraper.py** 是一個從 IMDb 網站("IMDb Top 250 Movies")中爬取電影數據的 Python 腳本，並儲存電影資料成TXT文檔，供後續ChatGPT使用。同時創建"喜歡"的電影假數據成為資料的一部分，代表客製化資料。
<br>
<br>
**imdb_webscraper_Demo.ipynb** 跟以上內容相同，但使用jupyter notebook展示結果。
<br>

### 3. imdb_gptbot
**imdb_gptbot.py** 是一個使用GPT-3.5語言模型，建立**自定義(IMDB)電影知識庫AI**的Python腳本。
ChatGPT會根據用戶提供的電影數據(imdb_webscraper爬蟲儲存的TXT檔)，回答用戶對電影相關問題的提問。
<br>
<br>
**imdb_gptbot_Demo.ipynb** 跟以上內容相同，但使用jupyter notebook展示結果。
<br>

## [需求]
這三個 Python 腳本需要網路連線才能使用 OpenAI API 或從 IMDb 網站上抓取電影數據。<br><br>
gpt_chatbot_Demo.py 和 imdb_gptbot.py 腳本需要一個 OpenAI API 金鑰，可以從 OpenAI 網站上獲取。<br><br>
imdb_webscraper.py 腳本需要使用 pip 安裝 requests 和 BeautifulSoup 函式庫。
<br>

## [用法]
要使用任何一個腳本，只需在終端機或 IDE 中執行 Python 檔案。腳本會提示用戶輸入並在控制台上顯示結果。
<br><br>
關於 gpt_chatbot_Demo.py 和 imdb_gptbot.py，請確保在運行之前在腳本中設置您的 OpenAI API 金鑰。
<br><br>
關於 imdb_webscraper.py，運行腳本後，會自動從 IMDb 網站上爬取數據並在控制台上顯示結果。
<br>
<br>




## Building a Personal (IMDB Movie) Knowledge Base AI with ChatGPT
This project includes three Python scripts that use ChatGPT 3.5 to build a personal (IMDB) movie knowledge base AI. Code output results can be viewed directly from the Jupyter notebook version.

Script summaries are as follows:

1. gpt_chatbot_Demo.ipynb: Demonstrates the use of the ChatGPI API in a simple way.
2. imdb_webscraper_Demo.ipynb: Scrapes movie data from the IMDb website.
3. imdb_gptbot_Demo.ipynb: Builds a personal (IMDB) movie knowledge base AI using data from the IMDb website and ChatGPI.

## [Explanations of scripts]

### 1. gpt_chatbot_Demo
**gpt_chatbot_Demo.py** is a Jupyter notebook that demonstrates how to use Python to connect to the OpenAI API, call ChatGPT 3.5, and create a contextually relevant question-and-answer format (similar to using the web version of Open AI's ChatGPT).
<br>

### 2. imdb_webscraper
**imdb_webscraper.py** iis a Python script that scrapes movie data from the IMDb website ("IMDb Top 250 Movies") and saves the movie information as a TXT file for later use by ChatGPT. It also generates fake movie data for "liked" movies to represent customized data as part of the dataset.
<br>
<br>
**imdb_webscraper_Demo.ipynb** is the same as the above, but demonstrates the results using a jupyter notebook.
<br>

### 3. imdb_gptbot
**imdb_gptbot.py** is a Python script that uses the GPT-3.5 language model to create a custom (IMDB) movie knowledge base AI. ChatGPT will answer user questions about movies based on the movie data provided by the user (stored in a TXT file obtained through the imdb_webscraper web scraper).
<br>
<br>
**imdb_gptbot_Demo.ipynb** is the same as the above, but demonstrates the results using a jupyter notebook.
<br>

## [Requirements]
All three scripts require an internet connection to use the OpenAI API or scrape data from the IMDb website. <br><br>
The gpt_chatbot_Demo.py and imdb_gptbot.py scripts require an OpenAI API key, which can be obtained from the OpenAI website. <br><br>
The imdb_webscraper.py script requires the requests and BeautifulSoup libraries, which can be installed using pip.
<br>

## [Usage]
To use any of the scripts, simply run the Python file in a terminal or IDE. The scripts will prompt the user for input and display the results on the console.
<br><br>
For gpt_chatbot_Demo.py and imdb_gptbot.py, make sure to set your OpenAI API key in the script before running it.
<br><br>
For imdb_webscraper.py, running the script will automatically scrape data from the IMDb website and display the results on the console