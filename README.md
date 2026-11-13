# Algorithm-Visualizer
 An application which can visualize a few basic sorting and searching algorithms.
 
## Goal
An application which can visualize a few basic sorting and searching algorithms.

**Status:** `completed`  
**Started:**  `11/07/2026`
**Last Updated:** `11/13/2026`

## Objective

- To write a program in python which can visualize a few basic searching and sorting algorithms.
- Visualizer is shown in the form of graphs.

## Approach

-  A class is defined that includes all the algorithms that will be used as the methods.
-  A common array is used by all the methods that is passed into the class during calling.
-  The array of data consist of 10 random numbers in the range of 10-100.
-  A main function is called which will handle the user input.
-  The user input decides if searching or sorting algorithms are required and which one.
-  If sorting algorithms are used the visualization is done through matplotlib.
-  For searching algorithms the position is pointed to as the visualizer.

## Problems & Decisions

-  There was no possible way to demonstrate the searching algorithm without using a GUI other  than the pointing method used.
-  Due to the array being altered by other methods of the class the `.copy()` method had to be  used to preserve the initial array.
-  In order to make the project complicated the animation is created through repeatedly updating the changing values that the function outputs.

## Results

<img width="801" height="688" alt="Screenshot 2026-11-13 161920" src="https://github.com/user-attachments/assets/c8eb7ecf-8369-4bb6-8670-879834830afe" /><img width="894" height="395" alt="Screenshot 2026-11-13 162008" src="https://github.com/user-attachments/assets/1dc5cdac-ef7a-47b9-99a2-b74695e214ef" />

<img width="894" height="395" alt="Screenshot 2026-11-13 162008" src="https://github.com/user-attachments/assets/1e907f07-b0c4-454e-ae26-64c359328aa0" />



## Problems & Decisions

-  There was no possible way to demonstrate the searching algorithm without using a GUI other  than the pointing method used.
-  Due to the array being altered by other methods of the class the `.copy()` method had to be  used to preserve the initial array.
-  In order to make the project complicated the animation is created through repeatedly updating the changing values that the function outputs.


