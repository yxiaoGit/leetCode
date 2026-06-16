def build_cartesian_tree(arr):
    stack = []
    parent = [-1] * len(arr)
    left = [-1] * len(arr)
    right = [-1] * len(arr)

    for i in range(len(arr)):
        last = -1
        while stack and arr[stack[-1]] <= arr[i]:
            last = stack.pop()
        if stack:
            parent[i] = stack[-1]
            right[stack[-1]] = i
        if last != -1:
            parent[last] = i
            left[i] = last
        stack.append(i)

    root = stack[0]
    return root, left, right


def euler_tour(root, left, right):
    euler = []
    depth = []
    first = {}

    def dfs(node, d):
        first.setdefault(node, len(euler))
        euler.append(node)
        depth.append(d)

        if left[node] != -1:
            dfs(left[node], d + 1)
            euler.append(node)
            depth.append(d)

        if right[node] != -1:
            dfs(right[node], d + 1)
            euler.append(node)
            depth.append(d)

    dfs(root, 0)
    return euler, depth, first


def preprocess_rmq(depth):
    # ±1 RMQ trick: block decomposition
    n = len(depth)
    import math

    block_size = max(1, int(math.log2(n) / 2))
    num_blocks = (n + block_size - 1) // block_size

    block_mins = [0] * num_blocks
    for b in range(num_blocks):
        start = b * block_size
        end = min(n, start + block_size)
        block_mins[b] = min(range(start, end), key=lambda i: depth[i])

    return block_size, block_mins


def rmq(depth, block_size, block_mins, L, R):
    # O(1) RMQ using block minima
    bL = L // block_size
    bR = R // block_size

    if bL == bR:
        return min(range(L, R + 1), key=lambda i: depth[i])

    candidates = []
    # left partial block
    endL = (bL + 1) * block_size
    candidates.append(min(range(L, endL), key=lambda i: depth[i]))

    # full blocks
    for b in range(bL + 1, bR):
        candidates.append(block_mins[b])

    # right partial block
    startR = bR * block_size
    candidates.append(min(range(startR, R + 1), key=lambda i: depth[i]))

    return min(candidates, key=lambda i: depth[i])


class RangeMaxQuery:
    def __init__(self, arr):
        root, left, right = build_cartesian_tree(arr)
        euler, depth, first = euler_tour(root, left, right)
        block_size, block_mins = preprocess_rmq(depth)

        self.arr = arr
        self.euler = euler
        self.depth = depth
        self.first = first
        self.block_size = block_size
        self.block_mins = block_mins

    def query(self, L, R):
        i = self.first[L]
        j = self.first[R]
        if i > j:
            i, j = j, i

        idx_in_euler = rmq(self.depth, self.block_size, self.block_mins, i, j)
        arr_index = self.euler[idx_in_euler]
        return arr_index, self.arr[arr_index]

   


class Solution:

    def includeAll(self, height: List[int], startLeft: int, endRight: int) -> int:
        maxh = min(height[startLeft], height[endRight])

        return sum([maxh-height[i] for i in range(startLeft+1, endRight)])


    def isLeftRightWall(self, height: List[int], leftPointer: int, rightPointer: int, rmq: RangeMaxQuery) -> bool:

        lh = height[leftPointer]
        rh = height[rightPointer]
        minh = min(lh, rh)
        maxh = max(lh, rh)
        includeAll = True
        

        maxvIndex, maxV = rmq.query(leftPointer+1, rightPointer-1)
        if maxV >= maxh or maxV > minh:
            return False, maxvIndex, maxV
        else:
            return True, 0, 0

        """
        import heapq


        heapMax = []
        heapMin = []

        for i in range(rightPointer-1, leftPointer, -1):
            if height[i] >= maxh:
               #print(f" found a middle peak, at {i} with value {height[i]} >= {maxh}")
               rightIndex = i
               rightPeak = height[i]
               heapq.heappush(heapMax, (-rightPeak,(rightIndex, rightPeak)))
               includeAll = False
            elif height[i] > minh:
               #print(f" found a middle peak, at {i} with value {height[i]} >= {minh}")
               rightIndex = i
               rightPeak = height[i]
               heapq.heappush(heapMin, (-rightPeak,(rightIndex, rightPeak)))
               includeAll = False

        if heapMax:
            peakV, (index, peak) = heapq.heappop(heapMax)
            return includeAll, index, peak
        elif heapMin:
            peakV, (index, peak) = heapq.heappop(heapMin)
            return includeAll, index, peak
        else:
            return includeAll, 0, 0
        """

    def trap(self, height: List[int]) -> int:

        
        

        prev=(0,-1)  # height and position
        index = 0
        #first leading edge, skip all leading 0
        total = len(height)

        if total < 3:
            return 0

        while index < total:
            if height[index] == 0:
                index +=1
            else:
                break

        if index == total -1:
            return 0




        index = 0
        # next to check if all acending to an index 2
        prevH, indexPrev = height[index], index
        index += 1
        startLeft = 0
        while index < total:
            if height[index] >= prevH :

                prevH = height[index]
                indexPrev = index
                startLeft = index
                index += 1
            else:
                break



        index = total -1
        prevH = height[index]
        rightPointer = total-1
        while index >= 0:
            if height[index-1] >= prevH :

                prevH = height[index-1]
                indexPrev = index-1
                rightPointer = index-1
                index -= 1
            else:
                break


        print(f" start and end index {startLeft} {rightPointer} total {total}")

        result = 0
        
        left = startLeft
        right = rightPointer
        index = 0
        peak = 0
        indexList=[(startLeft, rightPointer)]
        rmq = RangeMaxQuery(height)
        while indexList:
                leftPointer, rightPointer = indexList.pop()
                if rightPointer <= leftPointer or (rightPointer - leftPointer) < 2:
                    continue
                isWall, index, peak = self.isLeftRightWall(height, leftPointer, rightPointer, rmq)
                if isWall:
                    result += self.includeAll(height, leftPointer, rightPointer)
                    print(f"isWall {leftPointer} / {rightPointer} result updated to {result}")

                else:

                    indexList.append((leftPointer, index))
                    indexList.append((index, rightPointer))

        
        return result


    
