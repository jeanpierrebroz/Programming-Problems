class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #recursive
        visited = {0}

        keys = rooms[0]

        def visit_room(keys: List[int]):
            for key in keys:
                if key not in visited:
                    visited.add(key)
                    visit_room(rooms[key])

        visit_room(keys)
        
        return len(visited) == len(rooms)