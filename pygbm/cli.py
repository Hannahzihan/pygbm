# pygbm/cli.py

import argparse
import matplotlib.pyplot as plt
from .gbm_simulator import GBMSimulator

def main():
    parser = argparse.ArgumentParser(description="pygbm: A tool for simulating Geometric Brownian Motion paths.")
    
    # 创建子命令解析器
    subparsers = parser.add_subparsers(dest="command")
    
    # simulate 子命令
    simulate_parser = subparsers.add_parser("simulate", help="Simulate a Geometric Brownian Motion path")
    simulate_parser.add_argument('--y0', type=float, required=True, help="Initial value Y0")
    simulate_parser.add_argument('--mu', type=float, required=True, help="Drift coefficient")
    simulate_parser.add_argument('--sigma', type=float, required=True, help="Diffusion coefficient")
    simulate_parser.add_argument('--T', type=float, required=True, help="Total time period")
    simulate_parser.add_argument('--N', type=int, required=True, help="Number of steps")
    simulate_parser.add_argument('--output', type=str, help="Output file for the plot (e.g., gbm_plot.png)")
    
    args = parser.parse_args()

    if args.command == "simulate":
        # Initialize and simulate GBM
        simulator = GBMSimulator(args.y0, args.mu, args.sigma)
        t_values, y_values = simulator.simulate_path(args.T, args.N)
        
        # Plot the simulated path
        plt.plot(t_values, y_values, label="GBM Path")
        plt.xlabel("Time")
        plt.ylabel("Y(t)")
        plt.title("Simulated Geometric Brownian Motion Path")
        plt.legend()
        
        # Save plot to file if output is specified
        if args.output:
            plt.savefig(args.output)
            print(f"Plot saved as {args.output}")
        else:
            plt.show()

if __name__ == "__main__":
    main()
