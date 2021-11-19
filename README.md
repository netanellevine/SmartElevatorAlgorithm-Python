
   <p align="center">
    <img width="600" height="100" src="https://github.com/yanir75/Ex1_oop/blob/main/Images/header1.png"> 
   </p>  
   
---
![](https://img.shields.io/aur/last-modified/google-chrome)   
## Assignment 1 - Object Oriented Programming :office: :elevator:
**Yanir Cohen**  
**Netanel Levine** 
--- 
The project is about utilizing a building which is composed from a number of elevators and their parameters in the most efficient way for less waiting time of each person.  
In the project we will receive 2 files, a building file in json format and calls in csv format, calls are composed from few components the main ones are source floor and destination floor. In the algorithm we will try to determine what is the most efficient waiting time solution for the given problem.  
  
Reference to the UML: [ click here](#Smart-Elevator-UML)  
Reference to how to use: [ click here](#How-to-use)  
  
  
---
## Offline Algorithm:

According to a research shown in the sources , it can be seen that zoning has proved to have the best average wait time for each people.  
As a result we decided that our offline algorithm will be deviding the calls into zones and assigning the calls according to the speed of the elevator.  
Since this is an offline we added a tweak which calculates which zone should have the fastest elevator.  

---

## Here are our results for the avarage waiting time:
   - **The B1...B5 represents each of the buildings we tested.** 
   - **The Calls_a...Calls_d  represents each of the calls scenrio we tried.** 
   - The buildings B1, and B2 can be tested only on calls_a because this is the only scenario with calls that are in the floor range of these buildings. (-2,10)  

|           | **B1** | **B2** | **B3** | **B4** | **B5** |
|-----------|--------|--------|--------|--------|--------|
|**Calls_a**|	112.9	 | 42.2   |	44.2   | 36.9   |	26.7   |
|**Calls_b**|		     |        | 412.6  | 170.1  |	71.5   |
|**Calls_c**|		     |        | 420.8  | 157.2  |	64.7   |
|**Calls_d**|		     |        | 408.3  | 168.3  |	66.8   |  

 *Values were rounded to 1 digit after the decimal point.*    
 
---
## Smart Elevator UML

   
   <p align="center">
    <img width="800" height="900" src="https://github.com/yanir75/Ex1_oop/blob/main/Images/Smart%20Elevator%20UML.png">
   </p>

## GUI
[GUI Github Link](https://github.com/yanir75/ElevUi)  
[GUI Github Readme](https://github.com/yanir75/ElevUi/blob/master/README.md)  
Link for a youtube video which simulates two elevator  
[2 Elevators simultaor](https://youtu.be/HnYb2Hm9wEg)  
Link for a youtube video which simulates one elevator   
[1 Elevator simulator](https://youtu.be/-tUELfBsF24)

---


## How to use:
Clone the repository and cd(enter) the folder.
```
git clone https://github.com/yanir75/Ex1_oop.git & cd Ex1_oop
```
Install required packages.
```
pip install -r requirements.txt
``` 
To insert your own building and call files you can use this option
```
python Ex1_main.py <building_json_file_name> <calls_csv_file_name> <output_file_name>
```
To use existing building and call files use this command
```
python Ex1_main.py <output_file_name>
```
Use default paremters in case of no parameters
```
python Ex1_main.py
```
* `building_json_file_name` : reletive/full path and the file name, must be a json format.
* `calls_csv_file_name` : reletive/full path and the file name, must be a csv format.
* `output_file_name` : the output file name, will be as csv format.  
------
## Tests and testing jar
In order to test the results run the following
```
java -jar Ex1_checker_V1.2_obf.jar <IDs, building, calls, log_out>
```  
* `IDs` : at least 1 ID seperated by "," maximum 3.  
* `building` : the json file representing the building  
* `calls` : the csv file representing the calls  
* `log_out` : the output file name   

Run tester  
```
python Ex1_tester.py
```
*Note:*     
*If the tester succeeded it will delete the files it created automatically.*  
*In case of failure the files will be kept in order to observe the errors.*  

------
## Sources:

  - <a href="https://www.youtube.com/watch?v=siqiJAJWUVg">Elevator System Design OOP - Youtube</a>
  - <a href="http://vedantmisra.com/elevator-algorithms/">Elevator Algorithms - Vedant Misra</a>
  - <a href="https://github.com/00111000/Elevator-Scheduling-Simulator">Elevator Scheduling Simulator - GitHub</a>
  - <a href="https://www.researchgate.net/publication/31595225_Estimated_Time_of_Arrival_ETA_Based_Elevator_Group_Control_Algorithm_with_More_Accurate_Estimation">(ETA) Based Elevator Group Control Algorithm with More Accurate Estimation</a>
  - <a href="https://www.geeksforgeeks.org/scan-elevator-disk-scheduling-algorithms/">SCAN Elevator - GeegsForGeeks</a>
  - <a href="https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-elevators/">The
   Hidden Science of Elevators</a>
