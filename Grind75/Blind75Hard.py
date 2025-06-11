from collections import defaultdict, deque


def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    inDegree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        inDegree[course] += 1

    queue = deque()
    for i in range(numCourses):
        if inDegree[i] == 0:
            queue.append(i)
    order = []
    while queue:
        course = queue.popleft()
        order.append(course)
        for neighbor in graph[course]:
            inDegree[neighbor] -= 1
            if inDegree[neighbor] == 0:
                queue.append(neighbor)
    return order if len(order) == numCourses else []

def test_findOrder():
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(findOrder(numCourses, prerequisites))