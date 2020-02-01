# Grocery Shopping List Application
## Angular (FrontEnd) + (Python (Flask) + MongoDB) (BackEnd)
This is a demonstration project targeting a particular web-development stack.
I have developed Web application using Angular, Python (Flask) and MongoDB. The example application is for grocery shopping. 
This application helps the customer to add items and tasks to the grocery shopping list. Main interface of the Application is shown in Figure-1.
![Figure 1- Main Grocery Listing App](https://github.com/saadbinabid1/AngFlasMondb/blob/master/Demo_Pictures/pic1.GIF)

The customer can add the grocery shopping items/tasks to the list (Shown in Figure-2)

![Figure 2- Add Grocery Buying Task](https://github.com/saadbinabid1/AngFlasMondb/blob/master/Demo_Pictures/pic2.GIF)

If the customer thinks he put a wrong grocery item. He can change the grocery shopping item/task in the listing (Yellow part has been added.)
![Figure 3- You can also change the text of the grocery buying task](https://github.com/saadbinabid1/AngFlasMondb/blob/master/Demo_Pictures/pic3.GIF)

Once the customer thinks he has finished buying the grocery item or have done the task. He/she just push the done button and the grocery buying task is added to the done listing. As shown in Figure-4.
![Figure 4- Click Done button to make the task done](https://github.com/saadbinabid1/AngFlasMondb/blob/master/Demo_Pictures/pic4.GIF)

## Technical Specification
Following is the Technical Requirement for running the Application,

###### Python 3.8.1
###### Angular CLI: 8.3.23
###### Node: 12.14.1
###### OS: win32 x64
###### Angular:
...

Package                      Version
------------------------------------------------------
- @angular-devkit/architect    0.803.23
- @angular-devkit/core         8.3.23
- @angular-devkit/schematics   8.3.23
- @angular/cli                 8.3.23
- @schematics/angular          8.3.23
- @schematics/update           0.803.23
- rxjs                         6.0.0

## For running the application follow the steps,
         
1. Clone the repository
2. cd to the directory. Run the command set FLASK_APP=mongo.py
3. run the command 'flask run' in the terminal
4. cd to 'Client' folder in the project and run the command 'npm start'
5. go to web browser and add the url: http://localhost:4200/ (tested with recent version of chrome and firefox)
6. Enjoy the App.

##Trouble Shooting
You are required to make a MongoDB database (local database) with the name 'meantask' with the collection name 'tasks'