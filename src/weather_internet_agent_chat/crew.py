from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import WebsiteSearchTool
import os

API_KEY=os.getenv("GOOGLE_API_KEY")

llm =LLM(
     model= "gemini/gemini-1.5-flash",
     api_key= API_KEY
)

web_search = WebsiteSearchTool(
    config=dict(
        llm=dict(
            provider="google",  # or google, openai, anthropic, llama2, ...
            config=dict(
                model="gemini/gemini-2.0-flash",
            ),
        ),
        embedder=dict(
            provider="google",  # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                title="Embeddings",
            ),
        ),
    )
)

@CrewBase
class WeatherInternetAgentChatCrew():
    """WeatherInternetAgentChat crew"""

    @agent
    def weather_input_collector(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_input_collector'],
            tools=[],
            llm = llm
        )

    @agent
    def weather_query_builder(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_query_builder'],
            tools=[],
            llm = llm
        )

    @agent
    def weather_data_retriever(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_data_retriever'],
            tools=[web_search],
            llm = llm
        )

    @agent
    def weather_data_parser(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_data_parser'],
            tools=[],
            llm = llm
        )

    @agent
    def weather_reporter(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_reporter'],
            tools=[],
            llm = llm
        )


    @task
    def collect_weather_input(self) -> Task:
        return Task(
            config=self.tasks_config['collect_weather_input'],
            tools=[],
        )

    @task
    def build_weather_query(self) -> Task:
        return Task(
            config=self.tasks_config['build_weather_query'],
            tools=[],
        )

    @task
    def retrieve_weather_data(self) -> Task:
        return Task(
            config=self.tasks_config['retrieve_weather_data'],
            tools=[web_search],
        )

    @task
    def parse_weather_data(self) -> Task:
        return Task(
            config=self.tasks_config['parse_weather_data'],
            tools=[],
        )

    @task
    def generate_weather_report(self) -> Task:
        return Task(
            config=self.tasks_config['generate_weather_report'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the WeatherInternetAgentChat crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            planning=True,
            planning_llm= llm,
            chat_llm = "gemini/gemini-2.0-flash"
        )
