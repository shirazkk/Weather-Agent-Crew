from crewai import Agent, Task, Crew , LLM
import os
from weather_internet_agent_chat.tools.weather_tool import get_weather
import chainlit as cl
import asyncio
 
weather_tool = get_weather

API_KEY=os.getenv("GOOGLE_API_KEY")

llm =LLM(
     model= "gemini/gemini-1.5-flash",
     api_key= API_KEY
)

weather_input_collector = Agent(
    role = "Validate Input",
    goal = "Collect user's input for {city} to initiate the weather retrieval process.",
    backstory = """As the initial input validator for this workflow, you ensure that all
    necessary details like city are accurately captured and passed on
    to subsequent processes.""",
    llm=llm,   
    verbose=True  
)


weather_agent = Agent(
    role="Weather Forecaster",
    goal="Provide accurate real-time weather data for given city {city}.",
    backstory="Providing up-to-date and accurate weather reports",
    llm=llm,   
    tools=[weather_tool],  
    verbose=True  
)

collect_weather_input = Task(
  description ='Prompt the user to provide the necessary location details: {city}. Ensure that the inputs are validated before proceeding.',
  expected_output ='Collected and validated inputs: {city}.',
  agent=weather_input_collector
)

weather_task = Task(
    description="Fetch the latest weather details for a {city}.",
    agent=weather_agent,
    expected_output="A weather report with temperature, humidity, wind speed, and condition."
)

crew = Crew(agents=[weather_input_collector,weather_agent], tasks=[collect_weather_input,weather_task],verbose=True)




@cl.on_chat_start
async def start_chat():
    # Initial message to the user
    await cl.Message(content="Enter your city name to see current weather.").send()

@cl.on_message
async def handle_message(message: cl.Message):
    
    
    city_name = message.content.strip()

    loading_msg = await cl.Message(content=f"⏳ Fetching weather data...").send()

    weather_response = crew.kickoff(inputs={"city":city_name})

    await loading_msg.remove()  
    
    await cl.Message(content=f"🌦 **Weather Report for {city_name}**\n{weather_response}").send()
