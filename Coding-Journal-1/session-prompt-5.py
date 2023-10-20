import numpy as np

def main():
    x_start = 0
    x_end = 2 * np.pi
    entries =  1000
    x_values = np.arange(x_start, x_end, (x_end - x_start) / entries)
    print("x\t   sin(x)")

    for x in x_values:
        sin_x = np.sin(x)
        print(f"{x:.4f}\t   {sin_x:.4f}")
        
if __name__ == "__main__":
    main()
