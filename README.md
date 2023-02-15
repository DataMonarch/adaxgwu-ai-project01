# adaxgwu-ai-project01

\section{Introduction}

\subsection{Background} 
The water pitcher problem is a well-known problem in the field of Artificial Intelligence and computer science. It involves searching for the shortest path from an initial state to a final state. The problem is used to expand on the understanding of the search problem and to introduce students to informed search algorithms like A*.

\subsection{Problem statement}
In this project, we are given a text file with two lines. The first line contains a variable number of comma-separated integers, while the second line contains an integer. Our task is to calculate the shortest path (number of steps) from the initial state (all pitchers are empty) to the final state (where the “infinite” capacity pitcher has the target quantity).

\subsection{Purpose of the report}
The purpose of this report is to present the solution of the water pitcher problem using A* algorithm. The report explains the lower bound used in the A* algorithm and how the algorithm was implemented to find the shortest path from the initial state to the final state. The report also includes the test cases used to ensure the program works as expected.

\section{Methodology}

\subsection{Explanation of the problem representation}
In the problem, we are given a set of pitchers with different capacities and a target value. The task is to find the minimum number of moves required to get the target value in one of the pitchers. The problem is represented as a state in the form of a tuple, where each element of the tuple represents the amount of water in a pitcher. The first element represents a virtual pitcher with infinite capacity and the last element represents a virtual pitcher with zero capacity.

\subsection{Heuristic function used}
In this paper, the heuristic function used to solve the water jug problem is a simple, yet effective one. The function takes into account the distance between the target value and the current amount of water contained in the target pitcher. This distance is calculated as the absolute value of the difference between the two.

To provide a more accurate estimate of the minimum steps required to reach the target, the result of the above calculation is divided by the capacity of the pitcher with the maximum capacity. This normalization step ensures that the heuristic value is independent of the actual size of the jugs used.

Finally, the result is multiplied by 2 to account for the possibility of emptying a pitcher to the infinite pitcher, which doubles the number of operations required to reach the target. This step is necessary because the problem can only be solved if the jugs can be emptied as well as filled.

The resulting heuristic function provides a lower bound estimate of the minimum number of operations required to reach the target, and is used in this paper to guide the search for an optimal solution to the water jug problem.

\subsection{Process of state generation}
The process of state generation is performed by the get\_next\_state function. The function takes in the current state and generates the next possible states by iterating through the pitchers and finding the water transfer possibilities between them. The resulting states are returned as tuples.

\subsection{Approach to evaluate states}
The approach to evaluate states is based on the A* algorithm. The algorithm uses a priority queue, where each state is assigned a score based on its f-value, which is the sum of the g-value and h-value. The g-value is the number of moves required to reach the current state from the start state and the h-value is the estimated number of moves required to reach the target state from the current state. The priority queue is maintained in ascending order of f-values, so that the state with the lowest f-value is always at the front of the queue.

\subsection{ Approach to maintain the priority queue}
The priority queue is implemented using the heapq module in Python. The queue is a min heap, where each element is a tuple containing the f-value, h-value, and the state. The priority queue is maintained using the heapq.heappush and heapq.heappop functions, which add and remove elements from the queue, respectively. The heapq.heapify function is used to convert the list into a heap. When a state's g-value is updated, its f-value is also updated, and its position in the queue is adjusted accordingly using the heapq.heapify function.

\section{Results and Discussion}

\subsection{Result of the Implementation}
The A* algorithm implemented in the code is used to solve the puzzle of finding the minimum number of steps to reach a target value using a set of pitcher capacities. The code first reads the pitcher capacities and target value from an input file, and then calls the A* function. The A* function checks if the target value is divisible by the GCD of all the pitcher capacities, and returns -1 if it is not. If the target value is divisible, the algorithm begins by initializing the starting state and the scores for each state. The A* algorithm then uses the heuristic function, which calculates the difference between the target value and the current state, to guide its search for the optimal solution. The algorithm then iterates through all possible next states and updates their scores, keeping track of the previous state in the process. Once the target state is reached, the code prints the number of states evaluated, and the path from the starting state to the target state.

\subsection{Limitations and Possible Improvements}
The code may have limitations in terms of performance when the input data is very large. The code could also be improved by incorporating more advanced heuristics to guide the search process and reduce the number of states evaluated. Additionally, the code could be optimized for memory usage, for example by using a priority queue instead of a list to store open states. These improvements could result in faster and more efficient solutions for larger input data.

\section{References}
\begin{itemize}
  \item Github repository for the code: 
\end{itemize}
