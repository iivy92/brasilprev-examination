# Desafio Brasilprev

Este projeto é uma simulação de um jogo de tabuleiro similar ao Banco Imobiliário, desenvolvido em Python. O jogo consiste em uma partida com múltiplos jogadores que se alternam em rodadas, movendo-se pelo tabuleiro, comprando propriedades e pagando aluguéis.


## Requisitos do Sistema

- Python 3.x
- Pip, Poetry

## Executando Localmente

1. **Clonar o Repositório:**

    ```bash
    git clone https://github.com/iivy92/brasilprev-examination.git
    ```

2. **Entrar no diretório do projeto:**

    ```bash
    cd brasilprev-examination
    ```

3. **Instalar Poetry:**

    Certifique-se de ter Poetry instalado. 

    ```bash
    pip install poetry
    ```
4. **Instalar Dependências:**

    Dentro do diretório do projeto, execute:

    ```bash
    poetry install
    ```

5. **Ativar Ambiente Virtual:**

    Para ativar o ambiente virtual criado pelo Poetry, execute:

    ```bash
    poetry shell
    ```

5. **Executar o Projeto:**

    Agora você está pronto para executar o projeto:

    ```bash
    python main.py
    ```

6. **Acompanhe os resultados:**

    Acompanhe o resultado da simulação no console.
    ```
    ========================= Game Statistics =========================
        Total timed-out games: 207

        Average turns per game: 716.53

        Percentage of wins by strategy:
        - CAUTIOUS: 37.33%
        - IMPULSIVE: 45.00%
        - DEMANDING: 8.67%
        - RANDOM: 9.00%

        Most winning strategy: IMPULSIVE

    ```


## Rodando os testes unitários

1. **Executar comando:**

    ```bash
    pytest --cov=src
    ```
