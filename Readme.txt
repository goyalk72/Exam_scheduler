Code is written in python2.7

Dependancies:
1.z3-solver
2.texttable
3.python2.7

Input Format :
1."numberOfDays" will be the number of available working days when the exam can be scheduled e.g if you dont want to include weekends as exam days then exclude them from total number of days.
2."numberOfTimeSlots" will be the number of Time Slots available per day.
3."courses": Every list in the courses describes a course name, batches for that course and the number of students in each batch.
4."roomsCapacity" stores the maximum capacity of each classroom that is available to use as an examination hall.
5."roomsAvailableOnDay" stores the rooms available per day for examination e.g. as given in the input.json for Day1 only CL1 is available for Day2 LH2 and LT1 are available and so on.


How to use:
1.Follow the input format specified above file to add list of courses and corresponding batches.
2.Use the command "python main.py" to get the Time Table as an output in the terminal.
3.Output will be displayed as a table:
    a.First Column will consist of Slots e.g D1S1 meaning Day 1 and TimeSlot 1.
    b.Second Column will consist of Courses for that respective Slot.

+-------+----------------------+
| Slots |       Courses        |
+=======+======================+
| D1S1  | ee611                |
+-------+----------------------+
| D1S2  | ee207                |
+-------+----------------------+
| D2S1  | hs201                |
+-------+----------------------+
| D2S2  | me606                |
+-------+----------------------+
| D3S1  | cs101                |
+-------+----------------------+
| D3S2  | me219 /me610         |
+-------+----------------------+
| D4S1  | me338 /ma207         |
+-------+----------------------+
| D4S2  | hs431                |
+-------+----------------------+
| D5S1  | ee309 /ee225 /me423  |
+-------+----------------------+
| D5S2  | ee101                |
+-------+----------------------+
| D6S1  | me209                |
+-------+----------------------+
| D6S2  | ee301 /me613         |
+-------+----------------------+
| D7S1  | me614 /cs216 /sl400  |
+-------+----------------------+
| D7S2  | me201 /ma105         |
+-------+----------------------+
| D8S1  | me615                |
+-------+----------------------+
| D8S2  | ee308 /me306         |
+-------+----------------------+
