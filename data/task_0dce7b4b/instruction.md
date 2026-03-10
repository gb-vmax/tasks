I'm a FinOps analyst and I need your help setting up access controls for our cloud cost reporting system on our Linux server. We have a shared directory at `/home/user/finops/reports` that contains sensitive budget files. I need to lock it down properly so that only members of the `finops` group can read the files, and no one outside the group can access the directory at all.

Here's what I need done:

1. Add the user `analyst` to the group `finops`. (Both already exist on the system.)

2. Set the group ownership of the directory `/home/user/finops/reports` and **all files inside it** to `finops`.

3. Set the permissions on `/home/user/finops/reports` itself to `750` (owner has full access, group can read and traverse, others have no access).

4. Set the permissions on **every file directly inside** `/home/user/finops/reports` to `640` (owner can read/write, group can read, others have no access). Only the files directly in that directory need updating — do not recurse into subdirectories.

Please make these changes on the system now. I'll verify by running `ls -la /home/user/finops/reports` and checking the output, and also by running `groups analyst` to confirm group membership.

The expected output of `ls -la /home/user/finops/reports` should show:
- The directory entry itself (`drwxr-x---`) with group `finops`
- Each of the three `.csv` files (`q1_budget.csv`, `q2_budget.csv`, `q3_budget.csv`) showing permissions `-rw-r-----` with group `finops`

The expected output of `groups analyst` should include `finops` in the list of groups.
