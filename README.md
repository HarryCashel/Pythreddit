Reddit Clone 
===========
[Trello Board (unfinished)](https://trello.com/b/U2TWuOIi/t3-idea-reddit)

Pythreddit
----------
Pythreddit will be a reddit-like clone. 

This was built to explore my knowledge of databases, apis, Python and assess my ability to create a web app from the ground up.
Practise a real-world web application.

This app aims to be a news/social network where users can sign up, browse many different topics and share their 
own opinions. Users can interact with one another through comments. Users may fill their profile with information and set a profile photo.


Features
=======
* Account Creation
* Profile Creation
* Subreddits
* Threaded comments
* Upvoting

Potential 
------
* Admin accounts
* Search
* Direct messaging between accounts


Wireframes
------

##### Landing page / home page
The entry page. Top threads. User can log in/ sign up.
Threads should be accessible without logging in.
![wire](/docs/wire-frames/Page%201.png)
##### Log in / sign up form
When a user clicks either login or sign up the modal/overlay should pop up
A modal for the user to sign in to their account or register for one.
Very simple. Can sign up or log in with socials or with username/password.
![wire](/docs/wire-frames/Page%202.png)
##### More in depth look at the main page / outlay
Users (logged in or not) should be able to browse the web apps comments/threads/subs
Votes should be visible to everyone. If thread creator has chosen an image/video it should be visible on main page before opening.
![wire](/docs/wire-frames/Page%203.png)
##### Profile settings / info
General info for the user to fill out.
Can change their linked email address, display name and upload their avatar here.
![wire](/docs/wire-frames/Page%204.png)
##### Threads
Content header/ Image/video at top if there is one. followed by creator text.
Users can comment, upvote thread and other users comments.
Owner can delete only his own comments + main thread.
![wire](/docs/wire-frames/Page%205.png)


Threads
------
* A subreddit is a collection of threads/posts
* All posts will have a title (req)
* Posts can have links, videos, photos, text (optional)
* All posts are submitted by users/mods/admin
* Each post can have upvotes/downvotes. The sum of these should be displayed
* Posts should display total number of comments

##### Comments
* Users comment on posts
* Users can comment on comments
* Comments can be upvoted & downvoted

Installation
======

* Clone this repo:`git clone https://github.com/HarryCashel/T2A3.git`
* Change directory into the repo: `cd Pythreddit`
* Install venv: `pip install venv`
* Create virtual environment: `python3 -m venv venv`
* Active the virtual environment: `source venv/venv/active` 
* Install the dependencies: `pip install -r requirements.txt`
* Run the app: `python src/main.py`

CI/CD
------

The CI/CD pipeline was created using Github Actions. 
It uses Python3.8, Pip3 and runs on the latest stable version of Ubuntu. 
The pipeline is started on a push to master.

Once it has pulled from master it installs the dependencies form requirements.txt 
and then it runs the tests in the tests directory

Database
------
1. Each user can have multiple posts - posts belong to only one user
2. Each user can belong to many subs - A sub can have many users
3. A sub can have many posts - Posts belong to one sub
4. Each comment belongs to one users
5. Are upvotes/downvotes owned, or just calculated?
6. A sub is owned by one user - a user can own many subs

Questions
1. Will each subreddit/post/comment need an id?   
![wire](/docs/db/PythredditdraftERD.png)