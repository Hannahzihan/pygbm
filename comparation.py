from pygbm . gbm_simulator import GBMSimulator
import matplotlib . pyplot as plt

y0 = 1.0
mu = 0.05
sigma = 0.2
T = 1.0
N = 100

simulator = GBMSimulator(y0, mu, sigma)

t_analytical, y_analytical = simulator.simulate_path(T, N)
t_em, y_em = simulator.euler_maruyama(T, N)
t_milstein, y_milstein = simulator.milstein(T, N)

plt.figure(figsize=(10, 6))
plt.plot(t_analytical, y_analytical, label="Analytical Solution", linestyle="--", color="blue")
plt.plot(t_em, y_em, label="Euler-Maruyama", color="green")
plt.plot(t_milstein, y_milstein, label="Milstein", color="orange")
plt.xlabel("Time")
plt.ylabel("Y(t)")
plt.title("Comparison of Analytical, Euler-Maruyama, and Milstein Solutions for GBM")
plt.legend()
plt.show()