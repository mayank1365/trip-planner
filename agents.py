from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI 

"""
Creating Agents cheat Sheet: 
    - Think like a boss. Work backwards from the goal and think which employee 
        you need to hire to the kob done.
    - Define the Captain of the crew who orientates the team towards the goal.
    - Define which experts the captain needs to communicate with to delegate tasks to.
    - Build a top down structure of the crew.

    Goal: 
    - Create a 7 day trip itinerary with detailed per-day plans,
        including budget, packing suggestions, and safety measures.

    Captain/Mangaer/Boss: 
    - Expert Travel Agent
    
    Employees/Experts to hire: 
    - City selection expert
    - Local Tour Guide 

    Notes: 
    - Agents should be results driver and have a clear goal in mind 
    - Role is ther job title 
    - Goal should be actionable 
    - Backstory should be their resume
"""

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""
                            Expert in travel planning and logistics,
                             I have decades of experience in making travel iteneraries.
                             """),
            goal=dedent(f"""
                        Create a 7 day trip itinerary with detailed per-day plans,
                         including budget, packing suggestions, and safety measures.
                        """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="CIty Selection Expert",
            backstory=dedent(f"""
                            Expert at analyzing travel data to pick ideal destinations.
                            """),
            goal=dedent(f"""
                        Select the best cities based on weather, season, prizes, and travelers' preferences.
                        """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
    
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""
                            Knowlegable local guide with extensive information 
                             about the city, its history, culture, and attractions.
                            """),
            goal=dedent(f"""
                        Provide the BEST insights about the selected city
                        """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )