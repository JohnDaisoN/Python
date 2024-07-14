

from typing import List

class Solution:
    class Robot:
        def __init__(self, position: int, health: int, direction: str, index: int):
            self.position = position
            self.health = health
            self.direction = direction
            self.index = index

    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        vals = [self.Robot(positions[i], healths[i], directions[i], i) for i in range(n)]
        vals.sort(key=lambda x: x.position)

        stack = []
        for robot in vals:
            if robot.direction == 'R':
                stack.append(robot)
                continue

            gone = False
            while stack and stack[-1].health <= robot.health and stack[-1].direction == 'R':
                if stack[-1].health == robot.health:
                    stack.pop()
                    gone = True
                    break
                robot.health -= 1
                stack.pop()

            if not gone and stack and stack[-1].direction == 'R' and stack[-1].health > robot.health:
                stack[-1].health -= 1
                gone = True

            if not gone:
                stack.append(robot)

        stack.sort(key=lambda x: x.index)

        return [robot.health for robot in stack]

'''
LeetCode Logo
Daily Question
18

avatar
Premium
Debugging...
Debugging...







Run
Description
Description
Editorial
Editorial
Solutions
Submissions
Submissions


Code
Testcase
Test Result
Test Result
All Solutions


✅💯🔥Explanations No One Will Give You🎓🧠Very Detailed Approach🎯🔥Extremely Simple And Effective🔥

heir-of-god
30 Days of Pandas
3369
24368
Jul 13, 2024
C++
Java
Python
Python3
6+
You’ve got to get up every morning with determination if you’re going to go to bed with satisfaction.

--- George Lorimer ---

👑Problem Explanation and Understanding:
🎯 Problem Description
You are given n robots each of which have its position, health and direction all represented with arrays. These robots in one moment of time start moving with equal speed each in its direction. Every time two robots share 1 cell it turns into collide with this rules:

If one robot has more health then decrease its health by 1 and remove the robot with less health
If robots have equal amount of health - remove them both
You want to return health of robots which stay alive in order they were given
📥⤵️ Input:
1 <= positions.length == healths.length == directions.length == n <= 10^5

Integer array positions | 1 <= positions[i] <= 10^9 ; all positions are distinct
Integer array healths | 1 <= healths[i] <= 10^9
String array directions | directions[i] in ('L', 'R')
📤⤴️ Output:
The array of healths of robots which will stay alive in order they were given

1️⃣🧠 Approach: Smart Simulation With Sorting
🤔 Intuition
The first thing that came to my mind was to simulate this process, but it is clear that due to the fact that the positions are not sorted, this is quite difficult to do.
However, what dissuaded me from sorting for a while was that we need to return the health of the robots in the order in which we were given them (which usually means that sorting is not necessary).
Okay, let's imagine that we sorted the robots. Now we can go through this sorted list and add robots to the stack one by one. Why the stack? Because if we meet a robot that goes to the left, then the first enemy it meets is the last robot that goes to the right that we met.
Thus, the whole logic is that every time we meet a robot that goes to the right, we add it to the stack and every time we meet a robot that goes to the left, we fight it with the last robot on the stack until the last the robot on the stack does not go left (Which means there are no more robots on the left that go right) or until the robot dies.
For better understanding, let's look at an example.
P.S. You can do the same thing but in reverse - go from right to left in the array, append left robots and fight right robots
Dry Run
Let's look at this example

positions = [3, 1, 4, 2]
healths = [10, 5, 11, 10]
directions = "RLLR"
Setup before loop:

n = 4
robots list after combining positions, healths, directions, and indices:
robots = [[3, 10, 'R', 0], [1, 5, 'L', 1], [4, 11, 'L', 2], [2, 10, 'R', 3]]
robots list after sorting by positions:
robots = [[1, 5, 'L', 1], [2, 10, 'R', 3], [3, 10, 'R', 0], [4, 11, 'L', 2]]
stack: []
Inside the loop:

Loop Index	Robot	Stack State	Action
0	[1, 5, 'L', 1]	[]	Append to stack
[[1, 5, 'L', 1]]	
1	[2, 10, 'R', 3]	[[1, 5, 'L', 1]]	Append to stack
[[1, 5, 'L', 1], [2, 10, 'R', 3]]	
2	[3, 10, 'R', 0]	[[1, 5, 'L', 1], [2, 10, 'R', 3]]	Append to stack
[[1, 5, 'L', 1], [2, 10, 'R', 3], [3, 10, 'R', 0]]	
3	[4, 11, 'L', 2]	[[1, 5, 'L', 1], [2, 10, 'R', 3], [3, 10, 'R', 0]]	Collide with last robot in stack
Last robot health < current robot health
[[1, 5, 'L', 1], [2, 10, 'R', 3]]	Last robot is removed from stack
Current robot health decreased by 1 (to 10)
[[1, 5, 'L', 1], [2, 10, 'R', 3]]	Collide with new last robot in stack
Last robot health == current robot health
[[1, 5, 'L', 1]]	Last robot removed from the stack and this robot won't be added
Final Stack State:

[[1, 5, 'L', 1]]
Sorted Stack by Original Indices:

[[1, 5, 'L', 1]]
Final Output:

[5]
👩🏻‍💻 Coding
Create a list robots that combines positions, healths, directions, and the original indices into a list of lists.
Sort the robots list based on the positions.
Initialize an empty list stack to keep track of the surviving robots.
Iterate through each robot in the sorted robots list:
If the current robot is moving right ("R") or the stack is empty or the last robot in the stack is moving left ("L"), append the current robot to the stack and continue to the next robot.
If the current robot is moving left ("L"):
Set a flag add to True.
While the stack is not empty, the last robot in the stack is moving right ("R"), and add is True:
Get the health of the last robot in the stack as last_health.
If the current robot's health is greater than last_health, pop the last robot from the stack and decrease the current robot's health by 1.
If the current robot's health is less than last_health, decrease the last robot's health by 1 and set add to False.
If the current robot's health is equal to last_health, pop the last robot from the stack and set add to False.
If add is True, append the current robot to the stack.
Return a list of the healths of the surviving robots, sorted by their original indices.
📚 Complexity Analysis
⏰ Time complexity: O(n * log n), since we use sorting twice in the code which lead to 2 * n * log n -> O(n log n)
🧺 Space complexity: O(n), since 1. Sorting functions can use extra memory. 2. We creating new list robots of size n
💻 Code
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = [[positions[ind], healths[ind], directions[ind], ind] for ind in range(n)]
        robots.sort()
        stack = []

        for robot in robots:
            if robot[2] == "R" or not stack or stack[-1][2] == "L":
                stack.append(robot)
                continue

            if robot[2] == "L":
                add = True
                while stack and stack[-1][2] == "R" and add:
                    last_health = stack[-1][1]
                    if robot[1] > last_health:
                        stack.pop()
                        robot[1] -= 1
                    elif robot[1] < last_health:
                        stack[-1][1] -= 1
                        add = False
                    else:
                        stack.pop()
                        add = False

                if add:
                    stack.append(robot)

        return [robot[1] for robot in sorted(stack, key=lambda robot: robot[3])]
💡💡💡I encourage you to check out my profile and Project-S project for detailed explanations and code for different problems (not only Leetcode). Happy coding and learning!📚
Please consider upvote⬆️⬆️⬆️ because I try really hard not just to put here my code and rewrite testcase to show that it works but explain you WHY it works and HOW. Thank you❤️
If you have any doubts or questions feel free to ask them in comments. I will be glad to help you with understanding❤️❤️❤️
There is image for upvote

Next
✅Beats 100% -Explained with [ Video ] -C++/Java/Python/JS - Sorting - O( n log n) - Explained
Comments (15)

Sort by:Best
Type comment here... (Markdown supported)
Preview
Comment

Dagfinn_
Introduction to Pandas
Jul 13, 2024
@heir-of-god you are so good at pretense using enormous amount of copy-pasting and self-upvoting.
Maybe it'd be better you to become an actor rather then programmer?
It is for you own good to realize that IT is not for self-upvoters...

50
Show 3 Replies
Reply

Khushi-Kari
21 hours ago
@heir-of-god I laugh at you!

10
Reply

xcg1234
100 Days Badge 2022
13 hours ago
what a way to waste your cheap time..

2
Reply

reas0ner
100 Days Badge 2024
20 hours ago
Nice post, I solved it using a linked list instead of a stack. May be interesting!
https://leetcode.com/problems/robot-collisions/solutions/5470502/collapse-a-linked-list-simple-simulation-approach-with-explanation/

1
Reply

suyalneeraj09
Jun LeetCoding Challenge
Jul 13, 2024
Superb Explanation

0
Show 1 Replies
Reply

vinod_aka_veenu
50 Days Badge 2022
a day ago
Thanks for the share, in case if some beginners need clear simple explanation, they can follow this helpful link

Read more
0
Reply

sighaha
50 Days Badge 2023
a day ago
https://leetcode.com/problems/robot-collisions/solutions/5469895/super-easy-stack-hashmap-approach-in-python3-detailed-explanation-beat-99

Try this out and let me know if the explanation is easy to understand 👍

0
Reply

shivakumar1
100 Days Badge 2024
Jul 13, 2024
Full Detailed Explanation 🏆
https://leetcode.com/problems/robot-collisions/solutions/5469725/full-detailed-explanation/

0
Reply

A206k
50 Days Badge 2022
19 hours ago
full detail solution with comments
https://leetcode.com/problems/robot-collisions/solutions/5468429/best-easy-understandable-python3-solution-explained-by-line

0
Reply

Rohan_k14
SQL I
20 hours ago
https://leetcode.com/problems/robot-collisions/solutions/5470856/simplest-solution-full-explanation/

0
Reply

291


15


Python3
Auto





1234567891011121314151617
from typing import List

class Solution:
    class Robot:
        def __init__(self, position: int, health: int, direction: str, index: int):
            self.position = position
            self.health = health
            self.direction = direction
            self.index = index

…            if not gone and stack and stack[-1].direction == 'R' and stack[-1].health > robot.health:
                stack[-1].health -= 1
                gone = True

            if not gone:
                stack.append(robot)

        stack.sort(key=lambda x: x.index)

        return [robot.health for robot in stack]
Saved
Case 1
Case 2
Case 3

positions =
[5,4,3,2,1]
healths =
[2,17,9,15,10]
directions =
"RRRRR"
1
[5,4,3,2,1]
[2,17,9,15,10]
"RRRRR"
[3,5,2,6]
[10,10,15,12]
"RLRL"
[1,2,5,6]
[10,10,11,11]
"RLRL"

Tag

'''