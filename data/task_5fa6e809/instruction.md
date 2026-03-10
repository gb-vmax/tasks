I'm an infrastructure engineer automating server provisioning and I need your help solving a resource allocation problem using a linear programming solver.

I have a data center with a fixed budget and limited physical rack space, and I need to figure out the optimal number of each server type to provision in order to maximize total compute capacity (measured in vCPUs). Each server type has a different cost, rack unit (RU) footprint, and vCPU count.

The problem specification is in `/home/user/provisioning/server_spec.json`. It has the following structure:

- `budget`: total budget in dollars (integer)
- `rack_units`: total available rack units (integer)
- `servers`: a list of server objects, each with:
  - `name`: string identifier
  - `cost`: cost per unit in dollars (integer)
  - `ru`: rack units consumed per unit (integer)
  - `vcpus`: vCPUs provided per unit (integer)

Write a Python script at `/home/user/provisioning/solve_provisioning.py` that:

1. Reads `/home/user/provisioning/server_spec.json`.
2. Formulates and solves the linear programming problem using `scipy.optimize.linprog` to maximize total vCPUs subject to the budget and rack unit constraints, with each server count constrained to be ≥ 0. Use the LP relaxation (continuous solution) — do not use integer programming.
3. Writes the results to `/home/user/provisioning/provisioning_plan.txt`.

The output file `/home/user/provisioning/provisioning_plan.txt` must have exactly this format:

```
=== PROVISIONING PLAN ===
Budget used: $<X> of $<Y>
Rack units used: <X> of <Y>
Total vCPUs: <Z>

Allocation:
  <server_name>: <count>
  <server_name>: <count>
  ...
```

Where:
- Server names are listed in the same order as they appear in `server_spec.json`.
- `<count>` is each server's allocated count rounded to **2 decimal places** (e.g., `3.00` or `1.75`), because this is an LP relaxation.
- `Budget used` shows the dollar amount consumed (rounded to 2 decimal places) followed by the total budget.
- `Rack units used` shows rack units consumed (rounded to 2 decimal places) followed by the total available.
- `Total vCPUs` is the maximized objective value, rounded to **2 decimal places**.
- There are no trailing spaces on any line.

Run the script after writing it to produce `/home/user/provisioning/provisioning_plan.txt`.

The input file `/home/user/provisioning/server_spec.json` already exists — do not modify it.
