# Hell Let Loose Encylopedia

![picture of website on different devices](readme-pics/webiste-all-devices.png)

## About the Project

- I have created a website for a game called Hell Let loose. The game involves 2 teams of 50 players fighting against each other in a World War 2 immersive game, that can be played on a casual or a competitive level. As a result of the competitive side of the game, groups and clans have formed that play each other both on a competitive and a more friendly level. These clans have an organisation structure. They actively try to recruit new members and organise games against other clans, but none of this process is streamlined.

- The purpose of this website is to provide clan representatives with an area where they can both create a clan page to advertise their group and a channel through which they can contact other clan representatives to request games. It also provides a much needed service for the general user who can navigate around the website and seek out a clan to join. If they then find one that interests them, they can then investigate further by clicking on the clans discord link or the website link. 

[Live Website Link](https://hll-clans-encyclopedia-085b920e958c.herokuapp.com/)

## Target Audience

**What was the idea behind building the product?**

-	To allow users to have one location where they can search for hell let loose clans.
-	To allow users to get some detailed information about any specific clan.
-	To allow the user to be able to further research the clan by being shown the clans social network links.
-	Build an encyclopaedia style site. 
-	To allow clan representatives to be able to request games from other clans.
-	To allow representative from each clan to sign up and create an account on behalf of their clan.

**Who is the user?**

-	The user will be somebody of any age who has played hell let loose.
-	The user may be a regular player of hell let loose.
-	The user could  be either a casual or a competitive player.
-	The user will be seeking further information to help them  get more involved in the game.
-	The user will be looking to join a clan and is investigating the different options.
-	The user will already belong to a clan and be looking to recruit new members into the clan.


**What are the needs/wants of the users?**

-	A clan representative needs to be able to create a clan page
-	The clan representative needs to be able to write and add updates to  their  clan page as required.
-	The clan pages need to be visible and easily located.
-	The user will want the clan page to be clear and provide the relevant information.
-	Provided they create an account,  the clan representative will have  the correct level of access to make any changes required to the clan page
-	Clan reps they will have the ability to contact admin and raise a ticket to resolve any issues


**What are the needs/wants of the business?**

-	To create a website in an encyclopaedia style
-	The site should provide the user with a clear list of all the clans available in an A-Z format.
-	The site will be easy to navigate.
-	The site will contain a good balance of images and text.
-	The clan pages will be laid out in a way that keeps the user engaged.
-	For users who have signed up as a clan rep they will be given the correct permissions.
-	To keep traffic and user engagement, clan reps will be given the option to request games.
-	The system used to request games will be easy to use. 
-	The UI of the site will be seamless.



**How does the site meet the needs of the user and business?**

-	The website will be displayed in an encyclopaedia style. The front page will show an A-Z of the different clan names which will make it easy and simple to navigate 
-	By having it in encyclopaedia style, information will be available to the user straight away and will not require excessive searching.
-	The layout of the clan pages will be uniform across all pages to create a more professional looking site.
-	Clan representative will be have the required permissions to create the clan page and access to a support system with admin staff so any issues can be resolved in a timely manner.



## Scope

**what will the site include**

-	Description – there will be a section on the homepage that contains the rules of the site and how to create a clan page, request a game and raise a ticket with admin

-	Clan creation – both admin users and users who have signed up and created an account as a clan representative, will have the ability to create a clan which will give them full C.R.U.D access to the clan page

-	Clan page – users who view the site can see the different clan pages created

-	Match request – the ability for a clan rep to send a game request to another clan. This option is only  available to clan representatives and admin

-	Notifications tab – allows a clan representative and admin to see if they have a message from another clan representative, such as a game request or a ticket 

-	Sign up and log in – allows a user to sign up and log in either as a clan representative, basic user or admin

-	Administration system– create an admin /super user  

-	Ticket – create a ticket system for clan representatives or general users to contact admin

-	A-Z clan page directory – list of all the clans that have been created on the site


## Structure

### Site Map

- Below shows a breakdown of the website depending on the log in status of the user

**Admin user**

- Admin has access to edit and delete on any clan page

![picture of site map for admin](readme-pics/admin-site-map.png)

**Logged in user – clan representative**

- The logged in user only has access to edit and delete their own clan page

![picture of site map for clan representative](readme-pics/clan-rep-user-site-map.png)

**Logged in user – non clan representative**
- The logged in user only has access to notifications

![picture of site map for non clan representative](readme-pics/non-clan-rep-site-map.png)

## Data Schema

- Below is the data schema that I have created for the website, there are 4 main databases that have been created.  

- User database:  this has been created to log and store the users that have registered for the site. A Boolean field is included in the database and is used throughout the site to check if the user is a clan representative as they have access to additional features. There is also a ‘memorable name’ section which is used for password reset. 

- Clan database: this has been created to store the clans that have been created. They are linked on a one to one connection with the users database as one user can only have one clan. It also links the clan database in a one to many relationship with the notifications.

- Notification database: this stores all the messages that have been created and sent.

- Matches database:  this has a many to one relation to the clan page as many different game requests can be raised which relate to a single clan.

![picture of data scheme](readme-pics/data-schema.png)

## Skeleton

### Wireframe

- I created wireframes for each page of the website, showing how the site will appear both in mobile and browser format. 

**Homepage**

![picture of homepage](readme-pics/wireframe-homepage.png)

**Log in and out page**

![picture of log in and out page](readme-pics/wireframe-log-in-out.png)

**Clan Creation and Game Request**

![picture of Clan Creation and Game Request page](readme-pics/wireframe-clan-creation-game-request.png)

**Clan Page**

![picture of clan page](readme-pics/wireframe-clan-page.png)

**Notification Page**

![picture of Notification Page](readme-pics/wireframe-notifications.png)

**Individual Notification**

![picture of Individual Notification](readme-pics/wireframe-clan-indiv-notification.png)

**Individual Game Request**

![picture of Individual Game Request](readme-pics/wireframe-indiv-game-request.png)

**Edit Clan Page**

![picture of Edit Clan Page](readme-pics/wireframe-edit-clan-page.png)

**Raise Admin Ticket**

![picture of Admin Ticket request](readme-pics/wireframe-admin-ticket.png)

**Navigation Bars**

- Due to the different users, I also created different wireframes of the navigation bar, depending on the user’s log-in status

![picture of different navigation bars](readme-pics/wireframe-navbars.png)

## Surface


**Images**

- Most of the images used when creating the game have been taken from the official hell let loose website eg the logo. 

- The images used on the clan pages were taken from the Individual Discord channels for the related clan

- Other images have been taken from external sources such as an artist who creates artwork related to Hell let loose

![picture of different navigation bars](staticfiles/img/logo.svg)

**Colour Scheme**

- The website was created using colours that are in keeping with WW2. All colours were checked to make sure they did not clash and had the correct contrast with one another.

- Text - #FFFFFF

- Header background - #222222

- Body Background - #595959

- Focus  - #ff0000 – used for hover effects and buttons


**Typography**

- The theme for this website was WW2 therefore the font style was selected to compliment that theme. 

- Both fonts are from google fonts:

  - Header font: Font header - Black Ops One - [Link](https://fonts.google.com/specimen/Black+Ops+One)

  ![picture of header text example](readme-pics/font-header-example.png)

  - Main text font:  Font main - Special Elite - [Link](https://fonts.google.com/specimen/Special+Elite?query=Special+Elite+)

  ![picture of body text example](readme-pics/font-body-example.png)


