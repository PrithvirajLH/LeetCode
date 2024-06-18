class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        def calculate_slope (x,y):
            if  y[0]-x[0] != 0:
                return ((y[1] - x[1])/(y[0]-x[0]))
            else:
                return 0
        m1 = calculate_slope(points[0],points[1])
        m2 = calculate_slope(points[0],points[2])
        m3 = calculate_slope(points[1],points[2])
        if points[0] == points[1] or points[1] == points[2] or points[0]==points[2]:
            return False

        if m1==m2 and m2==m3:
            return False
        else: 
            return True
        
        
        # first = points[0]
        # m = []
        # for i in points[1:]:
        #     if  i[0]-first[0] != 0:
        #         m.append((i[1] - first[1])/(i[0]-first[0]))
        #     else:
        #         return False
        # if m[0] == m[1]:
        #     return False
        # else:
        #     return True
        