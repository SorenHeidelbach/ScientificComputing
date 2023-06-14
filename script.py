
# %%
import argparse


parser = argparse.ArgumentParser(description='Calculates sum of two integers (Floating points are acceptable also)')

parser.add_argument('-a', help = "asd")
parser.add_argument('-b', help = "dsa", type = float)

args = parser.parse_args()
# %%

try:
  print(args.a + args.b)
except TypeError:
  print("Error: Please enter two numbers")

print("Done")



import nonsense


if __name__ == "__main__":
  print("dones")