# FamPay

# To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response
# search API to search the stored videos using their title and description.



prerequesites 
--pthon 3.6 
--docker 


# Installation 

git clone git@github.com:uday966666/FamPay.git

cd FamPay
-- 
# creating docker Image 
docker build -t fampay .

# get the latest image id ex 64eb8a6e5e16

# runing the docker instance of the application 
docker run -d -p 5000:5000 <image id>
  
API: 
  1)  /getResults
  params:
        'start': start from the page default is 0
        'per_page': no of videos per page   
  this end point fetched latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response
 responce 
  sample responce :
  
{
  "details": [
    {
      "description": "We Will Change Playing Football, The Team Cannot Win.",
      "key_word": "jabardasth",
      "publishedAt": "2021-06-08T14:55:51Z",
      "thumbnails": {
        "default": {
          "height": 90,
          "url": "https://i.ytimg.com/vi/7jPcYn-K1io/default.jpg",
          "width": 120
        },
        "high": {
          "height": 360,
          "url": "https://i.ytimg.com/vi/7jPcYn-K1io/hqdefault.jpg",
          "width": 480
        },
        "medium": {
          "height": 180,
          "url": "https://i.ytimg.com/vi/7jPcYn-K1io/mqdefault.jpg",
          "width": 320
        }
      },
      "title": "We Will Change Playing Football, The Team Cannot Win"
    }
  ],
  "pagination": {
    "pageSize": 1,
    "start": 4,
    "totalRecorsInPage": 1
  }
}
  
  
  2)  /searchResults
  params:
        "q" : to search in title and description stored in database 
  
  this end point fetches the stored videos using their title and description.

