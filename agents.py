from crewai import Agent
from textwrap import dedent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
class QualityAssurenceAgent:
    
    def __init__(self):
        self.gemini15 = ChatGoogleGenerativeAI(model='gemini-pro', verbose= True, temperature= 0.5)

    def quality_assurence(self):
        return Agent(
            role="Quality Assurence",
            backstory=dedent(f"""Especialista em qualidade de software, com vasto conhecimento sistemico em ecommerce e servições de streaming.
                             """),
            goal=dedent(f"""Crie cenários de testes baseados na história recebida e nos casos de usos escritos nas historias.
                        Interprete da melhor forma as informações passadas usando seu vasto conhecimento na area.
                        Crie SEMPRE cenarios usando BDD."""),
            tools=[],
            verbose=True,
            llm=self.gemini15,
            callback=[],
        )