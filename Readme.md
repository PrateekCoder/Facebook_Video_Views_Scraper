# Facebook Video Views Scraper

## Softwares required:
1. Python 3
2. Terminal or Command line
3. Text Editor (Sublime Text or Atom)

## Python packages reuired:
1. Selenium
2. Pandas
3. xlsxwriter
4. bs4 (BeautifulSoup)

### ***Don't forget to enter your username and password before running the code.***

## How to use this code:

1. Install all the required softwares and python packages before proceeding.

2. Clone this repository or download the facebook_video_views.py file:
  **To clone this repository to local file use these commands:**
  ```
  Open Terminal/Commandline in the required directory.
  
  git init [This is to initialize the folder]
  
  git clone repository_url  [Replace repository_url with the link: https://github.com/PrateekCoder/Facebook_Video_Views_Scraper.git
  ```

3. Open terminal and run:
  ```
  python facebook_video_views.py
  ```

4. Once the script is executed, it will give you an excel file, facebook_videos.xlsx, which will contain four columns namely, the Date of Video Uploaded, Name of the video, Total Video Views and Video_Link.

### Things you might want to change in the code:
1. If you want to change the channel for which you want to scrape the video views, the you should change the urls list:
![](http://i63.tinypic.com/30ro4rs.png)

2. If you want to increase the number of videos to be scraped or more pages to be loaded, then you should increase the number from 100 to larger number in while loop, here:
![](http://i63.tinypic.com/oadtzq.png)
