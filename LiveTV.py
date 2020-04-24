#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import pafy
import vlc
import time


# In[14]:


class LiveTv:
    def __init__(self):
        self.channel_dict=self.__load_channel_list()
        self.__Instance=self.__get_vlc_instance()
        self.__player = self.__Instance.media_player_new()
    def set_media(self,url):
        playurl=self.__load_play_url(url)
        self.__load_media_url(playurl)
    def __load_media_url(self,playurl):
        Media = self.__Instance.media_new(playurl)
        Media.get_mrl()
        self.__player.set_media(Media)
    def __load_channel_list(self):
        csv_data=pd.read_csv("channel_list.csv",sep=",")
        csv_data.dropna(inplace=True)
        channel_dictionary=dict(zip(csv_data["channel_name"].tolist(),csv_data["channel_url"].tolist()))
        return channel_dictionary
    def __load_play_url(self,url):
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url
        return playurl
    def __get_vlc_instance(self):
        return vlc.Instance()
    def play_media(self):
        try:
            self.__player.play()
            print("Press Ctrl+C for exit")
            print("Please wait media is loading.......")
            time.sleep(120)
        except:
            print("Thank you for watching.")
            self.__player.stop()


# In[15]:


def main():
    livetvobj=LiveTv()
    choice_txt="Enter Your Choice : "
    channel_name_list=list(livetvobj.channel_dict.keys())
    channel_name_list.append("Quit")
    while True:
        for i,val in enumerate(channel_name_list):
            print(i+1,".",val)
        choice=input(choice_txt)
        try:
            choice=int(choice)
            if choice == len(channel_name_list):
                break
            elif choice > 0 and choice < len(channel_name_list):
                pass
            else:
                print("Please give number between 1 to ",len(channel_name_list))
        except:
            print("Please give number between 1 to ",len(channel_name_list))
        livetvobj.set_media(livetvobj.channel_dict[channel_name_list[choice]])
        livetvobj.play_media()


# In[ ]:


if __name__== '__main__':
    main()

