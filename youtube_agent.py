import time
from phi.agent import Agent
from phi.tools.youtube_tools import YouTubeTools
import openai  # Import openai package

agent = Agent(
    tools=[YouTubeTools()],
    show_tool_calls=True,
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
)

def get_video_summary():
    retries = 5
    backoff_time = 60  # Start with 1 minute
    for attempt in range(retries):
        try:
            agent.print_response("Summarize this video https://www.youtube.com/watch?v=Iv9dewmcFbs&t", markdown=True)
            break  # Exit the loop if the request succeeds
        except openai.RateLimitError:
            print(f"Rate limit exceeded. Retrying in {backoff_time} seconds...")
            time.sleep(backoff_time)  # Wait for the backoff time before retrying
            backoff_time *= 2  # Exponentially increase the backoff time
        else:
            break  # Exit the loop if no error occurs

get_video_summary()
