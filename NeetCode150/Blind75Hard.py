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


def sameSubstring(s, t, K):
    max_len = 0
    n = len(s)

    # Iterate over the lengths of the substrings
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            cost = 0
            for j in range(i, i + length):
                cost += abs(ord(s[j]) - ord(t[j]))
            if cost <= K and length > max_len:
                max_len = length

    return max_len


def sameSubstringDP(s, t, K):
    n = len(s)
    dp = [0] * (n + 1)

    max_len = 0

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + abs(ord(s[i - 1]) - ord(t[i - 1]))

    left = 0
    for right in range(1, n + 1):
        while dp[right] - dp[left] > K:
            left += 1
        max_len = max(max_len, right - left)

    return max_len


def intersect(nums1, nums2):
    nums2.sort()
    l1 = len(sorted(nums1))
    l2 = len(nums2)
    result = []
    i, j = 0, 0
    print(nums2)
    while i < l1 and j < l2:
        if nums1[i] == nums2[j]:
            result.append(nums2[j])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return result

