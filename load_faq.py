# load_faq.py
from knowledge_base import knowledge_base
from dotenv import load_dotenv

load_dotenv()


def main():
    print("📥 Loading FAQ data into the knowledge base...")
    knowledge_base.load()  # 👈 no await
    print("✅ FAQ data successfully loaded into Postgres!")


if __name__ == "__main__":
    main()
