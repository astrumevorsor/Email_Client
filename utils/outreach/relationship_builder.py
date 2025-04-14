from typing import List, Dict
from datetime import datetime, timedelta
import random

class RelationshipBuilder:
    def __init__(self):
        self.daily_limit = 50  # Maximum interactions per day
        self.interaction_cooldown = 7  # Days between interactions
        self.interaction_history = {}  # Track previous interactions
        
    def plan_interactions(self, profiles: List[Dict]) -> List[Dict]:
        """
        Plan a sequence of interactions with potential users.
        """
        planned_interactions = []
        today = datetime.now()
        
        for profile in profiles:
            if self._can_interact(profile['username'], today):
                interaction = {
                    'username': profile['username'],
                    'platform': profile['platform'],
                    'type': self._determine_interaction_type(profile),
                    'scheduled_time': self._schedule_interaction(today),
                    'content': self._generate_interaction_content(profile)
                }
                planned_interactions.append(interaction)
                
                if len(planned_interactions) >= self.daily_limit:
                    break
                    
        return planned_interactions
    
    def _can_interact(self, username: str, today: datetime) -> bool:
        """
        Check if we can interact with this user based on history and limits.
        """
        if username not in self.interaction_history:
            return True
            
        last_interaction = self.interaction_history[username]
        days_since_last = (today - last_interaction).days
        
        return days_since_last >= self.interaction_cooldown
    
    def _determine_interaction_type(self, profile: Dict) -> str:
        """
        Determine the best type of interaction based on profile data.
        """
        interaction_types = ['like', 'comment', 'follow', 'direct_message']
        return random.choice(interaction_types)
    
    def _schedule_interaction(self, today: datetime) -> datetime:
        """
        Schedule the interaction at a random time during the day.
        """
        random_hours = random.randint(9, 17)  # Business hours
        random_minutes = random.randint(0, 59)
        return today.replace(hour=random_hours, minute=random_minutes)
    
    def _generate_interaction_content(self, profile: Dict) -> str:
        """
        Generate personalized interaction content based on profile data.
        """
        # This would be expanded based on profile analysis
        return "Hi! I noticed your great content about {interest}..."
    
    def record_interaction(self, username: str, interaction_type: str):
        """
        Record that an interaction has occurred.
        """
        self.interaction_history[username] = datetime.now() 