from crewai import Task
from textwrap import dedent


class ScenarioTask:
    def __tip_section(self):
        return "Se você fizer seu MELHOR TRABALHO, eu lhe darei uma comissão de US$ 10.000!"

    def making_test_scenarios(self, agent, history, feature):
        with open(f'data/{history}.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        
        return Task(
            description=dedent(
                f"""
                    **Atividade**: Escrever cenarios de testes em BDD
                    
                    **Descrição**: Analisar a historia informada e cria cenários de testes em BDD, com detalhes e caracteristicas importantes.
                    Cobrir TODOS os possíveis erros que possam acontecer e criar TODOS os possíveis cenários de testes.
                    Revise os cenarios e veja se há alguma informação que deveria ser adicionada a algum cenário ou se há algum cenário de teste que 
                    não foi incluso.
                                        
                    **Informações**
                    - Historia: {conteudo}
                    - Funcionalidade: {feature}
                    
                    **Notas**: {self.__tip_section()}
                    """
            ),
            agent=agent,
            expected_output='Os cenários de testes mais claros e detalhados possíveis, cobrindo todos as partes da funcionalidade passada.'
        )

