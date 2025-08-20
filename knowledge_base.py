from agno.knowledge.json import JSONKnowledgeBase
from agno.vectordb.pgvector import PgVector
from agno.models.groq import Groq
from agno.embedder.google import GeminiEmbedder 
import os

groq_api_key = os.getenv("GROQ_API_KEY")


gemini_embedder = GeminiEmbedder(api_key=os.getenv("GOOGLE_API_KEY"))

knowledge_base = JSONKnowledgeBase(
    path="data/json",
    vector_db=PgVector(
        table_name="json_documents",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
        embedder=gemini_embedder, 
    ),
)
