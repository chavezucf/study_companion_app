import json
import os

PROFILE_PATH = 'data/profile.json'

class ProfileManager:
    def __init__(self):
        self.profile = {}
        self.load_profile()

    def load_profile(self):
        if not os.path.exists(PROFILE_PATH):
            print(f"[WARN] Profile not found at {PROFILE_PATH}, creating default profile.")
            self.profile = {
                "username": "Miguel",
                "xp": 0,
                "level": 1
            }
            self.save_profile()
        else:
            with open(PROFILE_PATH, 'r') as f:
                self.profile = json.load(f)

    def save_profile(self):
        with open(PROFILE_PATH, 'w') as f:
            json.dump(self.profile, f, indent=4)

    def get_username(self):
        return self.profile.get("username", "Unknown")

    def get_xp(self):
        return self.profile.get("xp", 0)

    def get_level(self):
        return self.profile.get("level", 1)

    def add_xp(self, amount):
        self.profile["xp"] += amount
        self.update_level()
        self.save_profile()

    def update_level(self):
        xp = self.profile["xp"]
        # Simple leveling logic:
        level_thresholds = [100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500]
        new_level = 1
        for threshold in level_thresholds:
            if xp >= threshold:
                new_level += 1
            else:
                break
        self.profile["level"] = new_level
        
    def get_topics(self):
        return self.profile.get("topics", {})

    def update_topic_performance(self, topic, correct):
        if "topics" not in self.profile:
            self.profile["topics"] = {}

        if topic not in self.profile["topics"]:
            self.profile["topics"][topic] = {"correct": 0, "incorrect": 0}

        if correct:
            self.profile["topics"][topic]["correct"] += 1
        else:
            self.profile["topics"][topic]["incorrect"] += 1

        self.save_profile()
