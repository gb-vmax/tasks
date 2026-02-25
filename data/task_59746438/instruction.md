An incident was reported regarding the permissions on a directory used by the "analytics" team. Triaging this incident requires you to do the following:

1. Create a user named "analyst01" if the user does not already exist.
2. Create a group named "analytics" if the group does not already exist, and add "analyst01" as a member of this group.
3. Create a directory at /home/user/team_projects/analytics_data if it doesn't exist. Ensure that this directory is owned by the "analyst01" user and the "analytics" group.
4. Set the permissions on /home/user/team_projects/analytics_data so that only the owner and group members can read, write, and enter the directory (i.e., no permissions for others).
5. To confirm that the permissions and ownership are set correctly, generate a single-line report file at /home/user/analytics_permission_report.txt with the following format (all on one line, separated by spaces):

<directory_path> <owner> <group> <permissions>

Where:
- <directory_path> is /home/user/team_projects/analytics_data
- <owner> is the owner of the directory
- <group> is the group ownership of the directory
- <permissions> is the permission string as shown by 'ls -ld' (e.g., drwxrwx---)

Example output (the actual permission string must match the set permissions):
/home/user/team_projects/analytics_data analyst01 analytics drwxrwx---

The automated test will check the contents and formatting of /home/user/analytics_permission_report.txt as well as the directory's actual ownership and permissions.
