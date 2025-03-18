class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low = 1
        ranks.sort()
        high = ranks[0] * (cars * cars)
        def check(time):
            fixedCar = 0
            for rank in ranks:
                if fixedCar < cars:
                    fixableCar = time // rank
                    carFixed = math.floor(math.sqrt(fixableCar))
                    fixedCar += carFixed
                else:
                    return True
            if fixedCar < cars:
                return False
            return True
        

        while low < high:
            mid = (low + high) // 2

            if check(mid):
                high = mid
            else:
                low = mid + 1
        return high



