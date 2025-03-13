# from crewai import Agent, Crew, Task, LLM
# from crewai.project import CrewBase, agent, crew, task
# from weather_internet_agent_chat.tools.weather_tool import get_weather
# import os

# weather_tool = get_weather



# # import agentops
# # agentops.init(
# #     api_key='88e0cae8-c352-4a97-80f3-ccf4aec68b20',
# #     default_tags=['crewai']
# # )

# API_KEY=os.getenv("GOOGLE_API_KEY")

# llm =LLM(
#      model= "gemini/gemini-1.5-flash",
#      api_key= API_KEY
# )


# @CrewBase
# class WeatherInternetAgentChatCrew():
#     """WeatherInternetAgentChat crew"""

#     @agent
#     def weather_agent(self)->Agent:
#         return Agent(
#             role="Weather Forecaster",
#             goal="Provide accurate real-time weather data for given city {city}.",
#             backstory="Providing up-to-date and accurate weather reports",
#             llm=llm,
#             tools=[weather_tool],  # Add the tool here
#             verbose=True  # Enable logging
#         )
    
#     @task
#     def weather_task(self)->Task:
#         return Task(
#             description="Fetch the latest weather details for a {city}.",
#             expected_output="A weather report with temperature, humidity, wind speed, and condition."
#     )

  
#     @crew
#     def crew(self) -> Crew:
#         """Creates the WeatherInternetAgentChat crew"""
#         return Crew(
#             agents=self.weather_agent, # Automatically created by the @agent decorator
#             tasks=self.weather_task, # Automatically created by the @task decorator
#             verbose=True,
#             planning=True,
#             planning_llm= llm,
#         )
