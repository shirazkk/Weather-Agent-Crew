# #!/usr/bin/env python
# import sys
# from weather_internet_agent_chat.crew import WeatherInternetAgentChatCrew

# # This main file is intended to be a way for your to run your
# # crew locally, so refrain from adding unnecessary logic into this file.
# # Replace with inputs you want to test with, it will automatically
# # interpolate any tasks and agents information

# city_name = input("Enter Your City Name To search weather... ")   
# def run():
#     """
#     Run the crew.
#     """
    
#     WeatherInternetAgentChatCrew().crew().kickoff(inputs={"city": city_name})


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """

#     try:
#         WeatherInternetAgentChatCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs={"city":city_name})

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         WeatherInternetAgentChatCrew().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     try:
#         WeatherInternetAgentChatCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs={"city":city_name})

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: main.py <command> [<args>]")
#         sys.exit(1)

#     command = sys.argv[1]
#     if command == "run":
#         run()
#     elif command == "train":
#         train()
#     elif command == "replay":
#         replay()
#     elif command == "test":
#         test()
#     else:
#         print(f"Unknown command: {command}")
#         sys.exit(1)











