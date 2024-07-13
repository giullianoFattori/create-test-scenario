import os

from crewai import Crew
from textwrap import dedent
from agents import QualityAssurenceAgent
from tasks import ScenarioTask
from tools.translate_tools import Translate
class QualityCrew:
    
    def __init__(self, history, feature):
        self.history = history
        self.feature = feature

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = QualityAssurenceAgent()
        tasks = ScenarioTask()

        # Define your custom agents and tasks here
        quality_agent = agents.quality_assurence()
        
        # Custom tasks include agent name and variables as input
        making_scenarios = tasks.making_test_scenarios(
            quality_agent,
            self.history,
            self.feature,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[quality_agent],
            tasks=[making_scenarios],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Bem-vindo ao Criador de Cenários de testes")
    print("-------------------------------")
    file = input( dedent("""Coloque o arquivo dentro da pasta data e me informe o nome. O arquivo deve ser em extensão txt:\n"""))
    feature = input( dedent("""Essa historia se trata de qual funcionalidade?\n"""))


    quality_crew = QualityCrew(file, feature)
    result = quality_crew.run()
    print("\n\n########################")
    print("## Aqui está o resultado da execução da equipe personalizada:")
    print("########################\n")
    print("Todo os cenarios foram criados com sucesso, verifique a pasta cenarios dentro do projeto")
    print("########################")    
    translated = Translate.translate_text(result)
    Translate.save_to_file(translated)
