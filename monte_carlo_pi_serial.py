import random
import time

def monte_carlo_pi_serial(num_samples):
    inside = 0
    for _ in range(num_samples):
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        if x**2 + y**2 <= 1:
            inside += 1
    return (inside / num_samples) * 4



def main():
    inicio = time.time()
    tamanho = 524288*2
    num_samples = 10000000
    print("Estimativa de Pi = ", monte_carlo_pi_serial(num_samples))
    fim = time.time()
    print(fim - inicio)


if __name__ == '__main__':
    main()