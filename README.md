# Send It
Send It is basically a platform where people can make a parcel order and deliver orders

####Getting Started
clone the project using the [link](https://github.com/ekwaro/Send.git)
####Prerequisites
A browser with internet access
####Installing
* clone the project on your local machine
~~~
https://github.com/ekwaro/Send/blob/master/UI/admin/main.html
~~~
#####Accessing the frontend of the application
The front-end of the application is hosted on gh pages and can be accessed from [here](https://github.com/ekwaro/Send/blob/master/UI/admin/main.html)

##Features

* Users can create an account and login
* Users can create a parcel delivery order
* Users can change the destination of a parcel delivery order
* Users can cancel a parcel delivery order
* Users can see details of a parcel delivery order
* Admin can change the status and present location of a parcel delivery order
 

###End points
 HTTP method|End point|functionality 
 -----------|---------|--------------
 GET|/api/v1/parcels|Fetch all parcel delivery order
 GET|/api/v1/parcels/<parcelId>/|Fetch a specific parcel delivery order
 GET|/api/v1/users/<userId>/parcels|Fetch all parcel delivery order by a specific user
 PUT|/api/parcels/<parcelId>/cancel|cancel the specific parcel delivery order
 POST|/api/v1/parcels/|create a parcel delivery order
 
 ###Tools Used
 * [Flask](http://flask.pocoo.org/)
 * [Virtual Environment](https://virtualenv.pypa.io/en/stable/) - Used to create an isolated virtual environment
 * [PIP](https://pip.pypa.io/en/stable/) - A python package installer
 
 ### Deployment
 The API is hosted on [Heroku]()
 ## Built with 
 * python/ Flask
 ###Authors
 Ekwaro Dominic
