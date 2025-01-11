# Yes cpu consumer

import multiprocessing
import time

def cpu_stress_test():
    # Perform a heavy computation
    while True:
        sum(i * i for i in range(10000))

if __name__ == "__main__":
    # Get the number of CPU cores
    num_cores = multiprocessing.cpu_count()
    print(f"Starting CPU stress test on {num_cores} cores.")

    # Create a process for each core
    processes = []
    for _ in range(num_cores):
        p = multiprocessing.Process(target=cpu_stress_test)
        p.start()
        processes.append(p)

    try:
        time.sleep(6000)
    except KeyboardInterrupt:
        print("Stress test interrupted.")

    for p in processes:
        p.terminate()
    for p in processes:
        p.join()

    print("Stress test completed.")