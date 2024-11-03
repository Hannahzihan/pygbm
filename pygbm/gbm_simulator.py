import numpy as np
from .base_simulator import BaseSimulator

class GBMSimulator(BaseSimulator):
    def __init__(self, y0, mu, sigma):
        super().__init__(y0, mu, sigma)
    def simulate_path(self, T, N):
        """Simulate a path for Geometric Brownian Motion.
        
        Parameters:
            T (float): The total time period.
            N (int): The number of steps.
        
        Returns:
            tuple: A tuple (t_values, y_values) where
                   t_values is an array of time points and
                   y_values is the simulated GBM values at each time point.
        """
        dt = T / N  # Time step
        t_values = np.linspace(0, T, N + 1)
        y_values = np.zeros(N + 1)
        y_values[0] = self.y0
        
        for i in range(1, N + 1):
            dB = np.random.normal(0, np.sqrt(dt))  # Brownian increment
            y_values[i] = y_values[i - 1] * np.exp((self.mu - 0.5 * self.sigma**2) * dt + self.sigma * dB)
        
        return t_values, y_values
    
    def euler_maruyama(self, T, N):
        """Simulate a path for Geometric Brownian Motion using the Euler-Maruyama method."""
        dt = T / N
        t_values = np.linspace(0, T, N + 1)
        y_values = np.zeros(N + 1)
        y_values[0] = self.y0

        for i in range(1, N + 1):
            dB = np.random.normal(0, np.sqrt(dt))
            y_values[i] = y_values[i - 1] + self.mu * y_values[i - 1] * dt + self.sigma * y_values[i - 1] * dB

        return t_values, y_values

    def milstein(self, T, N):
        """Simulate a path for Geometric Brownian Motion using the Milstein method."""
        dt = T / N
        t_values = np.linspace(0, T, N + 1)
        y_values = np.zeros(N + 1)
        y_values[0] = self.y0

        for i in range(1, N + 1):
            dB = np.random.normal(0, np.sqrt(dt))
            y_prev = y_values[i - 1]
            y_values[i] = y_prev + self.mu * y_prev * dt + self.sigma * y_prev * dB + 0.5 * self.sigma**2 * y_prev * (dB**2 - dt)

        return t_values, y_values