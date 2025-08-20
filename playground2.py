from agno.agent import Agent
from agno.playground import Playground
from agno.storage.sqlite import SqliteStorage
from agno.models.groq import Groq
from knowledge_base import knowledge_base
import os

from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPEN_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")


agent_storage: str = "tmp/agents.db"

faq_agent = Agent(
    name="FAQ Agent",
    model=Groq(id="qwen/qwen3-32b"),
    knowledge=knowledge_base,
    search_knowledge=True,
    instructions=[
        "Answer only from the FAQ knowledge base. "
        "If the answer is not found, say: 'I couldn't find this in FAQs. Do you want me to create a support ticket?'"
    ],
    storage=SqliteStorage(table_name="faq_agent", db_file=agent_storage),
    add_datetime_to_instructions=False,
    add_history_to_messages=True,
    num_history_responses=3,
    markdown=True,
)

playground = Playground(agents=[faq_agent])
app = playground.get_app()

if __name__ == "__main__":
    playground.serve("playground2:app", reload=True)
