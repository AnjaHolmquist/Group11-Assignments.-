# Group11-Assignment A1
## Describe the use case you have chosen
Cost with focus om the walls

## Who is the use case for?
This use case is for the contractors, economy and Client (Bygherre) so he/she can se the cost of the wall production 

## What disciplinary (non BIM) expertise did you use to solve the use case
We have made a BPMN to find out the steps we are going thrue
![image](https://github.com/AnjaHolmquist/Group11-Assignments.-/blob/main/BPMN.png)
you can download the file in BPMN
and open it in [BPMN online](https://demo.bpmn.io/). 

## What IFC concepts did you use in your script (would you use in your script)
Len(wall)

for wall in walls:
    print(wall.Name)
    
for wall in walls:
    print(wall.ObjectType)

## What disciplinary analysis does it require?
- Structural analysis
- geometric analysis 
- material quantity output of concrete to schedule time and price

## What building elements are you interested in?
The exterior walls

## What (use cases) need to be done before you can start your use case?
Structureal and arcitectual

## What is the input data for your use case?
We need to know: 
- The materials
- The dimentions
- Prices and expenses
- Time-schedule for each process

## What other use cases are waiting for your use case to complete?
LCA and Structual
