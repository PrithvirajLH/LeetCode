class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        already_been = set([0])
        to_visit = deque(rooms[0])
        while to_visit.__len__() > 0:
            room = to_visit.popleft()
            for key in rooms[room]:
                if key not in already_been:
                    to_visit.append(key)
            already_been.add(room)
            if already_been.__len__() == rooms.__len__():
                return True
        return already_been.__len__() == rooms.__len__()

        