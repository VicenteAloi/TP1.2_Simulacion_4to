import math
from scipy.stats import norm, chi2
from scipy.special import erfc

class Tests():
    def monobit_test(bit_string):
        bits = [int(bit) for bit in bit_string]
        n = len(bits)
        s = sum(1 if bit == 1 else -1 for bit in bits)
        s_obs = abs(s) / math.sqrt(n)
        p_value = norm.sf(s_obs) * 2  # Two-tailed test
        return p_value

    def block_frequency_test(bit_string, block_size=8):
        bits = [int(bit) for bit in bit_string]
        n = len(bits)
        num_blocks = n // block_size
        proportions = [(sum(bits[i*block_size:(i+1)*block_size]) / block_size) for i in range(num_blocks)]
        chi_squared = 4 * block_size * sum((p - 0.5) ** 2 for p in proportions)
        p_value = 1 - chi2.cdf(chi_squared, df=num_blocks)
        return p_value

    def runs_test(bit_string):
        bits = [int(bit) for bit in bit_string]
        n = len(bits)
        pi = sum(bits) / n
        tau = 2 / math.sqrt(n)

        if abs(pi - 0.5) >= tau:
            return 0.0  # No se puede realizar la prueba si pi está fuera del rango

        v_n = 1 + sum(bits[i] != bits[i+1] for i in range(n-1))
        p_value = erfc(abs(v_n - 2*n*pi*(1-pi)) / (2 * math.sqrt(2*n) * pi * (1-pi)))
        return p_value

    def interpret_p_value(p_value, alpha=0.01):
        if p_value >= alpha:
            return "Los números generados no parecen ser aleatorios."
        else:
            return "Los números generados parecen ser aleatorios."

# Ejemplo de uso
# bits = '110101101010101'
# print(bits)
# # p_value_monobit = Tests.monobit_test(bits)
# # print(f"Monobit Test p-value: {p_value_monobit}")

# # block_size = 100
# # p_value_block_frequency = Tests.block_frequency_test(bits, block_size)
# # print(f"Block Frequency Test p-value: {p_value_block_frequency}")

# p_value_runs = Tests.runs_test(bits)
# print(f"Runs Test p-value: {p_value_runs}")