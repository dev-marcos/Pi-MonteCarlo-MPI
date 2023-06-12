# Cálculo de Aproximação de π utilizando o Método de Monte Carlo em Python com MPI

Este repositório contém uma implementação do método de Monte Carlo para calcular a aproximação de π. Ele apresenta duas versões do mesmo algoritmo, uma versão serial e uma versão paralela usando a biblioteca MPI em Python.

## Como o Método de Monte Carlo funciona?

O método de Monte Carlo é uma técnica estatística que permite a obtenção de resultados aproximados para problemas complexos por meio de experimentos com números aleatórios. Nesse caso, utilizamos o método de Monte Carlo para calcular uma aproximação de π.

Imagine um quadrado de lado 2 com um círculo inscrito nele de raio 1. O quadrado tem área 4, e o círculo tem área π. Se escolhermos pontos aleatórios dentro do quadrado, a proporção que cairá dentro do círculo será aproximadamente a proporção das duas áreas, que é π / 4.

## Instalação

Para executar este projeto, você precisará instalar o seguinte:

- Python 3.x
- mpi4py: `pip install mpi4py`

## Uso

1. Clone este repositório em sua máquina local.
2. Navegue até a pasta onde o repositório foi clonado.
3. Execute o programa serial com `python monte_carlo_pi_serial.py`.
4. Execute o programa paralelo com `mpiexec -n 4 python monte_carlo_pi_mpi.py`, onde `-n 4` é o número de processos que você deseja iniciar.

## Contribuição

Pull requests são bem-vindos. Para mudanças importantes, abra um problema primeiro para discutir o que você gostaria de alterar.

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
