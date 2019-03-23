"""
Given n intervals find minimal set of points that each interval includes at least
one point.
"""

def main():
    n_points = int(input())
    intervals = []
    for _ in range(n_points):
        intervals.append(list(map(int, input().split())))
    intervals = sorted(intervals, key=lambda x: x[1])
   
    points = []
    while len(intervals):
        # Get leftmost point of from intervals' ends
        p = intervals[0][1]
        points.append(p)
        i = 1
        new_intervals = [] 
        for inter in intervals[1:]:
            if inter[0] <= p:
                pass
            else:
                new_intervals.append(inter)
        print("New intervals: ", new_intervals)
        intervals = new_intervals
        
    print(len(points))
    print(' '.join(list(map(str, points))))
    
if __name__ == "__main__":
    main()

