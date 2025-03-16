class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        l = 1
        r = ranks[0] * cars * cars
        res = -1

        def calc_repaired_cars(time):
            count = 0
            for r in ranks:
                count += int(sqrt(time/r))
            return count

        while l <= r:
            m = (l+r) // 2
            repaired_cars = calc_repaired_cars(m)
            if repaired_cars >= cars:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
        