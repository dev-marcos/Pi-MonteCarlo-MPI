from mpi4py import MPI
import random

def monte_carlo_pi_part(n, start, end):
    count = 0
    for _ in range(start, end):
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        if x**2 + y**2 <= 1:
            count += 1
    return count

inicio = MPI.Wtime()

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = 10000000

# calculando o intervalo para cada processo
start = rank*(n//size)
end = (rank+1)*(n//size)

# cada processo calcula sua parte
count = monte_carlo_pi_part(n, start, end)

# reúne os resultados de todos os processos
counts = comm.gather(count, root=0)

# o processo mestre calcula a estimativa final de pi
if rank == 0:
    fim = MPI.Wtime()
    print(fim - inicio)
    total = sum(counts)
    pi_approx = (total / n) * 4
    print("Estimativa de Pi = ", pi_approx)
    print(fim - inicio)


