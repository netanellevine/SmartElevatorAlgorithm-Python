# Assignment 1 - Object Oriented Programming :elevator:

**Yanir Cohen**  
**Netanel Levine** 

## Sources:

  - https://www.youtube.com/watch?v=siqiJAJWUVg
  - https://github.com/00111000/Elevator-Scheduling-Simulator
  - https://www.researchgate.net/publication/31595225_Estimated_Time_of_Arrival_ETA_Based_Elevator_Group_Control_Algorithm_with_More_Accurate_Estimation



## Offline Algorithm:

Our offline algorithm is similar to the Look algorithm with some modifications.
First we will divide it into 2 arrays , one for all the calls which are going up and one for all the calls which are going down.
If there are 2 calls in the same direction the elevator will go to the furthest in the zone and will pick up both (furthest means the call whose source floor is further from the destination), calculates the travel time between picking them both at once or picking one taking him to the destination and returning and picking the other up.
Note: all that assuming there isn’t any other available elevator.

If there are any other calls in the route to the destination pick them up unless they are in the opposite direction.
When an elevator has reached the destination, go to the next and nearest call source floor and check 2.




## Online Algorithm:

1. First divide into 3 cases: flag 0, flag 1 and flag 2.

   - Flag 0 will be designed for a case in which the building has only one Elevator.

   - Flag 1 is designed for a building with slow Elevators and a high amount of floors.

   - Flag 2 is designed for a building with fast Elevators or a decent amount of floors.

2. Flag 0 will check if there is a stop in between the calls and pick them up otherwise it will complete its’ existing route.
     
3. Flag 1 will have an elevator waiting for long travels such as 60 floors
Meaning we will go over the route of each elevator in the building and will choose the elevator by which one will finish its route the fastest after adding the call.
This will be done by calculating the floors in each route and dividing by the speed, then adding to the one with the lowest time to finish.
However there will be an elevator which waits and picks up all the long calls and waits then travels again and again from top to bottom.

4. Flag 2 will go from the fastest to reach the call and finish it. bla
Meaning we will go over the route of each elevator in the building and will choose the elevator by which one will finish its route the fastest after adding the call.
  
    
---
![]("C:\Users\netan\Smart Elevator UML.png "Smart Elevator UML"")
   
   <p align="center">
    <img width="800" height="900" src="![Smart Elevator UML](https://user-images.githubusercontent.com/74298433/142627608-d2f9e7ea-25b0-4188-8e26-63ac07be7473.png)" title="Smart Elevator UML">
   </p>


## How to use:
```
git clone https://github.com/yanir75/Ex1_oop.git
```
```
pip install -r requirements.txt
``` 
```
python Ex1_main.py <json_file> <csv_file>
```

### Here are our results for the avarage waiting time:
   - **The B1...B5 represents each of the buildings we tested.** 
   - **The Calls_a...Calls_d  represents each of the calls scenrio we tried.** 

|           | **B1** | **B2** | **B3** | **B4** | **B5** |
|-----------|--------|--------|--------|--------|--------|
|**Calls_a**|	112.9	 | 42.2   |	44.2   | 36.9   |	26.7   |
|**Calls_b**|		     |        | 412.6  | 170.1  |	71.5   |
|**Calls_c**|		     |        | 420.8  | 157.2  |	64.7   |
|**Calls_d**|		     |        | 408.3  | 168.3  |	66.8   |
