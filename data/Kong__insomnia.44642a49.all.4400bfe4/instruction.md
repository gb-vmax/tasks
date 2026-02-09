# Bug Report

### Describe the bug
After a recent update, the workspace list is completely empty even though workspaces exist in the database. When I try to view my workspaces, nothing shows up - the list is always blank.

### Reproduction
1. Create one or more workspaces in the application
2. Navigate to the workspace list/selector
3. The list appears empty even though workspaces were created successfully

I can confirm that workspaces are being created (the create function works), but when trying to retrieve or display them, the list is always empty.

### Expected behavior
The workspace list should display all existing workspaces that have been created and saved to the database.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
