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
![wire](/wire-frames/Page%201.png)
##### Log in / sign up form
When a user clicks either login or sign up the modal/overlay should pop up
A modal for the user to sign in to their account or register for one.
Very simple. Can sign up or log in with socials or with username/password.
![wire](/wire-frames/Page%202.png)
##### More in depth look at the main page / outlay
Users (logged in or not) should be able to browse the web apps comments/threads/subs
Votes should be visible to everyone. If thread creator has chosen an image/video it should be visible on main page before opening.
![wire](/wire-frames/Page%203.png)
##### Profile settings / info
General info for the user to fill out.
Can change their linked email address, display name and upload their avatar here.
![wire](/wire-frames/Page%204.png)
##### Threads
Content header/ Image/video at top if there is one. followed by creator text.
Users can comment, upvote thread and other users comments.
Owner can delete only his own comments + main thread.
![wire](/wire-frames/Page%205.png)


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

`git clone https://github.com/HarryCashel/T2A3.git`

`pip install -r requirements.txt`

Navigate to the root directory and run:

`python src/main.py`