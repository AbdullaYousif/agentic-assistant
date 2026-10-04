from agno.agent import Agent
from agno.db.in_memory import InMemoryDb
from agno.models.openrouter import OpenRouter
from dotenv import load_dotenv
from agno.team import Team

# Load environment variables from .env file
load_dotenv()

# Constants
MAIN_MODEL_ID = "nvidia/nemotron-3-ultra-550b-a55b:free"
SIMPLER_MODEL_ID = "nvidia/nemotron-3.5-lightning:free"
SESSION_ID = "123456789" # You can change this to any unique session ID you want

# Agents
def create_story_teller_agent() -> Agent:
    return Agent(
        model=OpenRouter(id=SIMPLER_MODEL_ID),
        role="Your job is to create a story based on the text provided by the user. Make sure to be creative and engaging.",
        instructions="You must create short and concise stories based on the user's input. The stories must be max 200 words long.",
        name="Story Teller Agent",
        markdown=True,
        add_datetime_to_context=True,
    )

def create_feedback_agent() -> Agent:
    return Agent(
        model=OpenRouter(id=SIMPLER_MODEL_ID),
        role="Your job is to provide feedback on the story created by the Story Teller Agent. Make sure to be constructive and helpful.",
        name="Feedback Agent",
        markdown=True,
        add_datetime_to_context=True,

    )

def run() -> None:
    story_teller_agent = create_story_teller_agent()
    feedback_agent = create_feedback_agent()

    team = Team(
        model=OpenRouter(id=MAIN_MODEL_ID),
        name="Agentic Assistant Team",
        markdown=True,
        members=[story_teller_agent, feedback_agent],
        add_datetime_to_context=True,
        add_team_history_to_members=True,
        determine_input_for_members=False
    )


    while True:
        input_text = input("Enter your prompt (or 'exit' to quit): ")

        if input_text.lower() in ["exit", "quit"]:
            print("Exiting...")
            break

        team.print_response(input_text, debug_mode=True)
