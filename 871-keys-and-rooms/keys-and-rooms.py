class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()

        def dfs(room):
            visit.add(room)
            for key in rooms[room]:
                if key not in visit:
                    dfs(key)
        
        dfs(0)
        return len(visit) == len(rooms)


        