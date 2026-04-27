class QuestRoom:
    def __init__(self, name, difficulty, limit):
        self.name = name
        self.difficulty = difficulty
        self.limit = limit
        self.players = []
        self.status = "waiting"
        self.events_log = []

    def add_player(self, name):
        if len(self.players) >= self.limit:
            return "No free slots!"
        
        # 1. FIX: Add to log to satisfy 'test_complex_scenario'
        self.players.append(name)
        self.events_log.append(f"Player {name} joined")
        return f"Player {name} joined" # Return string for success

    def remove_player(self, name):
        if name in self.players:
            self.players.remove(name)
            self.events_log.append(f"Player {name} left")
            return f"Player {name} left"
        return "Player not found!"

    def start(self):  
        if not self.players:
            return "Room is empty!"
        
        self.status = "active"
        self.events_log.append("Quest started")
        return f"Quest '{self.name}' started with {len(self.players)} players!"    

    def is_full(self):
        return len(self.players) == self.limit

    def free_slots(self):
        return self.limit - len(self.players)

    def reset_room(self):
        self.players = []
        self.status = "waiting"
        self.events_log.append("Room reset")
        return "Room reset!"

    def players_list(self):
        if not self.players:
            return "No players in the room"
        return self.players

    def show_log(self):
        return self.events_log

    def __str__(self):       
        return f"QuestRoom: {self.name} | Difficulty: {self.difficulty} | Players: {len(self.players)}/{self.limit}"        


room = QuestRoom("Island", 3, 2)
room.add_player("Neo") 