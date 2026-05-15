levels = [
    {"level": 1, "title": "Care Explorer", "min_xp": 0},
    {"level": 2, "title": "Behavior Basics Learner", "min_xp": 100},
    {"level": 3, "title": "Reinforcement Apprentice", "min_xp": 250},
    {"level": 4, "title": "Simulation Practitioner", "min_xp": 500},
    {"level": 5, "title": "ABAT/RBT Ready Learner", "min_xp": 900}
]

missions = [
    {"id": 1, "name": "Understanding Reinforcement", "xp": 50},
    {"id": 2, "name": "Observing Behavior", "xp": 50},
    {"id": 3, "name": "Managing Transitions", "xp": 75},
    {"id": 4, "name": "Sensory Overload Response", "xp": 75},
    {"id": 5, "name": "Documenting for Supervision", "xp": 100}
]

def calculate_total_xp(completed_mission_ids):
    total_xp = 0

    for mission in missions:
        if mission["id"] in completed_mission_ids:
            total_xp += mission["xp"]

    return total_xp

def get_current_level(total_xp):
    current_level = levels[0]

    for level in levels:
        if total_xp >= level["min_xp"]:
            current_level = level

    return current_level

def unlock_next_mission(completed_mission_ids):
    completed_count = len(completed_mission_ids)

    if completed_count < len(missions):
        return missions[completed_count]

    return None

if __name__ == "__main__":
    completed = [1, 2, 3]

    total_xp = calculate_total_xp(completed)
    current_level = get_current_level(total_xp)
    next_mission = unlock_next_mission(completed)

    print("Total XP:", total_xp)
    print("Current Level:", current_level)
    print("Next Mission:", next_mission)
