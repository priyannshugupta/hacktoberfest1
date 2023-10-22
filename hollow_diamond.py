'''
Print hollow diamond pattern using '*'

Input Format
First line of input contains T - number of test cases. Its followed by T lines, each line contains a single odd integer N - the size of the diamond.

Constraints
1 <= T <= 100
3 <= N <= 201

Output Format
For each test case, print the test case number as shown, followed by the diamond pattern, separated by newline.

Sample Input 0
4
3
7
5
15
Sample Output 0
Case #1:
 *
* *
 *
Case #2:
   *
  * *
 *   *
*     *
 *   *
  * *
   *
Case #3:
  *
 * *
*   *
 * *
  *
Case #4:
       *
      * *
     *   *
    *     *
   *       *
  *         *
 *           *
*             *
 *           *
  *         *
   *       *
    *     *
     *   *
      * *
       *
'''
T = int(input())

for case in range(1, T+1):
    N = int(input())
    print("Case #{}:".format(case))
    for i in range(N//2+1):
        spaces = " "*(N//2 - i)
        stars = "*" if i == 0 else "*" + " "*(2*i - 1) + "*"
        print(spaces + stars)
    for i in range(N//2 -1, -1, -1):
        spaces = " "*(N//2 - i)
        stars = "*" if i == 0 else "*" + " "*(2*i - 1) + "*"
        print(spaces + stars)
