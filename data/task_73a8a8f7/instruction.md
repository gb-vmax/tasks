You are a capacity planner analyzing server resource limits using environment variables defined in a dotenv file. Perform the following steps:

1. In your home directory (/home/user), create a new dotenv file named /.env.capacity.
2. Add the following variable assignments to /.env.capacity, each on its own line, with no extra whitespace:
   - MAX_CPU=8
   - MAX_MEM_GB=32
   - STORAGE_TB=10
3. Write a shell command that loads these environment variables from the /.env.capacity file (without using external tools like dotenv or python-dotenv).
4. Output the following line, using the loaded environment variables (the values must NOT be hardcoded, but referenced from the environment):
   ```
   Resources: CPU=8 MEM=32GB STORAGE=10TB
   ```
   The format must exactly match, with a single space between each label, and GB/TB capitalized as shown.

To enable verification, create a file /home/user/capacity_output.log containing only the printed output, exactly as it is displayed on the terminal. The content must match precisely, including capitalization and spacing.
