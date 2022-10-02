
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import preventBullying


import string
from youtube_comment_scraper_python import *
import time
import frontEnd

def youtubeParse(url) -> list:
    youtube.open(url)
    dictionary = youtube.video_comments()
    listOfComments = ["u fugly bro"]
    for key in dictionary["body"]:
        listOfComments.append(key["Comment"])
    print(listOfComments)
    return listOfComments


st.set_page_config(page_title="My Webpage", page_icon="🎉", layout="wide")

#this function connects to the website with animation and accepts the requests
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#get the images from the websites
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_ghg0pifn.json")
lottie_coding2 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_xbf1be8x.json")
lottie_coding3 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_pvlqvtxk.json")


#describes the main functionality and introduces the page to user
with st.container():
    st.markdown("<h1 style='text-align: center; font-size: 70px; color: orange;'> bNicer. </h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: black;'> Educate yourself on cyberbullying. Real time. Real examples. </h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: black;'> bNice is a website that scans the page url for any potential words/sentences that can be hurtful to someone. The code then runs it through a machine learning algorithm to determine if it's hurtful based on up-to-date trends of words. There are many types of bullying, so, bNice categorizes it for you and provides the relevant article so that you can be educated on the targeted information on REAL examples from REAL websites so we can all learn in the most efficient way on how to bNicer 😊 </p>", unsafe_allow_html=True)
    

#this section separates the search URL and supporting animations
with st.container():
    leftCol, rightCol = st.columns(2)
    with leftCol:

        with leftCol:
            st_lottie(lottie_coding, height=350, key = "coding")
            
        with rightCol:
            st_lottie(lottie_coding2, height=150, key = "boding")
    with rightCol:
        #TEXT INPUT HERE 
        url = st.text_input("Paste the URL you want to bully check below 😁")
        

if url != "":
    #exec(open('\Users\shrey\bNice\preventBullying.py').read())

    youtube.open(url)
    dictionary = youtube.video_comments()
    listOfComments = []
    for key in dictionary["body"]:
        listOfComments.append(key["Comment"])
    #listOfComments = preventBullying.youtubeParse(url)
    st.markdown(listOfComments)
    print(listOfComments)
    



#information on bullying is shown at the pages below.
with st.container():
    leftCol, rightCol = st.columns(2)
    with leftCol:
        st.subheader("What is cyberbullying?")
        st.write("It is the use of electronic communication to bully or degrade another person, typically by sending messages of an intimidating or threatening nature -Oxford Languages")

        st.subheader("How common is cyberbullying?")
        st.write("In a 2016 report from the Cyberbullying Research Center indicates that around 40% students between the ages of 12 to 17 were victims of cyberbullying in their lifetime. It can happen anywhere and to anyone. Most of cyberbullying occur on social media websites, such as Instagram, Snapchat, Reddit, Twitter, and YouTube. With an increase of dependency on the internet and technology for connecting with each other. Of all the social networks, kids on YouTube are the most likely to be cyberbullies at a whopping 80%, followed by Snapchat at 69 percent, TikTok at 64 percent, and Facebook at 49 percent. ")
        st.subheader("What are the 10 types of cyber bullying?")
        st.write("""1. Exclusion
2. Harassment 
3. Outing/Doxing
4. Trickery
5. Cyberstalking
6. Masquerading
7. Dissing
8. Trolling
9. Flaming
""")


    with rightCol:
        st.subheader("The effects of bullying")
        st.write("Bullying is something that should never be endorsed as it affect other because it negetively affects their mental health, academic performance, and encourage suicidal thoughts. About 41% of those who are bullied reported that they have became less active in class and 24% reported that their school performance had dropped and 35% of those had to repeat a grade. Being bullied is a serious issue and should never be accepted. ")

        st.subheader("Let’s all bNicer to each other, here’s ideas how to:")
... (9 lines left)
Collapse
frontEnd.py
7 KB
﻿
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import preventBullying


import string
from youtube_comment_scraper_python import *
import time
import frontEnd

def youtubeParse(url) -> list:
    youtube.open(url)
    dictionary = youtube.video_comments()
    listOfComments = ["u fugly bro"]
    for key in dictionary["body"]:
        listOfComments.append(key["Comment"])
    print(listOfComments)
    return listOfComments


st.set_page_config(page_title="My Webpage", page_icon="🎉", layout="wide")

#this function connects to the website with animation and accepts the requests
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#get the images from the websites
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_ghg0pifn.json")
lottie_coding2 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_xbf1be8x.json")
lottie_coding3 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_pvlqvtxk.json")


#describes the main functionality and introduces the page to user
with st.container():
    st.markdown("<h1 style='text-align: center; font-size: 70px; color: orange;'> bNicer. </h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: black;'> Educate yourself on cyberbullying. Real time. Real examples. </h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: black;'> bNice is a website that scans the page url for any potential words/sentences that can be hurtful to someone. The code then runs it through a machine learning algorithm to determine if it's hurtful based on up-to-date trends of words. There are many types of bullying, so, bNice categorizes it for you and provides the relevant article so that you can be educated on the targeted information on REAL examples from REAL websites so we can all learn in the most efficient way on how to bNicer 😊 </p>", unsafe_allow_html=True)
    

#this section separates the search URL and supporting animations
with st.container():
    leftCol, rightCol = st.columns(2)
    with leftCol:

        with leftCol:
            st_lottie(lottie_coding, height=350, key = "coding")
            
        with rightCol:
            st_lottie(lottie_coding2, height=150, key = "boding")
    with rightCol:
        #TEXT INPUT HERE 
        url = st.text_input("Paste the URL you want to bully check below 😁")
        

if url != "":
    #exec(open('\Users\shrey\bNice\preventBullying.py').read())

    youtube.open(url)
    dictionary = youtube.video_comments()
    listOfComments = []
    for key in dictionary["body"]:
        listOfComments.append(key["Comment"])
    #listOfComments = preventBullying.youtubeParse(url)
    st.markdown(listOfComments)
    print(listOfComments)
    



#information on bullying is shown at the pages below.
with st.container():
    leftCol, rightCol = st.columns(2)
    with leftCol:
        st.subheader("What is cyberbullying?")
        st.write("It is the use of electronic communication to bully or degrade another person, typically by sending messages of an intimidating or threatening nature -Oxford Languages")

        st.subheader("How common is cyberbullying?")
        st.write("In a 2016 report from the Cyberbullying Research Center indicates that around 40% students between the ages of 12 to 17 were victims of cyberbullying in their lifetime. It can happen anywhere and to anyone. Most of cyberbullying occur on social media websites, such as Instagram, Snapchat, Reddit, Twitter, and YouTube. With an increase of dependency on the internet and technology for connecting with each other. Of all the social networks, kids on YouTube are the most likely to be cyberbullies at a whopping 80%, followed by Snapchat at 69 percent, TikTok at 64 percent, and Facebook at 49 percent. ")
        st.subheader("What are the 10 types of cyber bullying?")
        st.write("""1. Exclusion
2. Harassment 
3. Outing/Doxing
4. Trickery
5. Cyberstalking
6. Masquerading
7. Dissing
8. Trolling
9. Flaming
""")


    with rightCol:
        st.subheader("The effects of bullying")
        st.write("Bullying is something that should never be endorsed as it affect other because it negetively affects their mental health, academic performance, and encourage suicidal thoughts. About 41% of those who are bullied reported that they have became less active in class and 24% reported that their school performance had dropped and 35% of those had to repeat a grade. Being bullied is a serious issue and should never be accepted. ")

        st.subheader("Let’s all bNicer to each other, here’s ideas how to:")
        st.write("Being nice can help in ways you cannot imagine. Little bit of kindness can go a long way and everyone including you are fully capable of helping someone by being kind. You can offer a helping hand by sending motivation texts to a friend or a family member or hold the door open for a stranger. You can also be there to listen to someone because everyone is going through some sort of struggle you never who needs a moment express their feelings. Be there to listen for a friend or family member. Remember that being a good listen requires you to give them your full attention. Stay connected with your people by checking in and connecting with family and friends whenever you can. A simple text or call lets them know that you are thinking of them. A little kindness goes a long way because kindness has a ripple effect")
        st_lottie(lottie_coding3, height=300, key = "coding3")
     

#references
    with st.container():
        st.subheader("References")
        st.write("""(UT Health Houston Med School, 2021), (Object Lesson for Kindness - The Domino Effect, 2022), (Hamilton, 2022), (The 10 Types of Cyberbullying - Blog, 2022),(Cyberbullying: Twenty Crucial Statistics for 2022 | Security.org, 2022)""")

