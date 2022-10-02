# bNicer - SASEHACKS Fall 2022

## Introduction
When coming up with an idea, we researched about bullying and often it occurs. We found out that almost half of students between 12 to 17 have experienced some sort of bullying. To try and minimize this, we had the idea to identify negativity in text through a deep learning network. Our ideal project was to be able to identify negative texts through a chrome extension, but due to time, we decided to make a proof of concept and launch it on a website.

#### Project Description
Our website takes a YouTube URL as an input. It then opens the page on a separate chrome browser and loads the given URL. Then, using the library youtube_comment_scraper_python we were able to extract all the comments on that webpage and store them in a list object. The list then gets parsed through by the deep learning model and returns positive or negative corresponding to the tone of the message. If the message ends up being marked as negative, we go through a second layer of search. We check if the string has any substring containing foul words. We do this by preemptively preparing different dictionaries corresponding to words that are discriminatory, bullying, or offensive or a combination of the three. Those correlations are then returned on the website along with education material that can help improve the person’s opinions, actions, and vocabulary so they never stoop as low as the commentors.

## Getting Started

#### Prerequisites
* Install Python3.10
* Install streamlit
```sh
pip install streamlit
```
* Install Packages
```sh
pip install tensorflow
pip install tensorflow-text
pip install streamlit-lottie
pip install youtube-comment-scraper-python
pip install -q transformers
pip install pandas
pip install 
```

#### Installation
1. Clone the repo
```sh
git clone https://github.com/tinabyte/bNice.git
```
2. Go into project and install npm libraries
```sh
cd bNice
cd bNice
pip install tensorflow
pip install tensorflow-text
pip install streamlit-lottie
pip install youtube-comment-scraper-python
pip install -q transformers
pip install pandas
pip install 
```
3. Run the project using the following command:
```sh
stremalit run frontEnd.py
```

## Notes
The repo has three main folders. The "/bNice" folder contains the main source code for the streamlit code using python. The machine learning model can be seen through the jupyter notebook under "/model". The "/preprocessCSV" was used to format the tweet data in an ideal csv format for tweet analysis using TensorFlow. TensorFlow demo was inspired by this demo https://youtu.be/P0o5U9pq8_s along with https://youtu.be/AkEnjJ5yWV0

