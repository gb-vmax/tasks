# Bug Report

### Describe the bug

After a recent update, the application crashes when trying to repair workspaces with multiple base environments. The database repair process seems to be incomplete and causes the app to fail during startup or when performing workspace operations.

### Reproduction

1. Create a workspace with multiple base environments (this can happen when importing or syncing)
2. Launch the application
3. The repair function attempts to merge the base environments
4. Application crashes or becomes unresponsive

This appears to be affecting the workspace repair functionality specifically when dealing with duplicate base environments that need to be consolidated.

### Expected behavior

The repair process should successfully merge multiple base environments into a single one, updating all sub-environments to point to the chosen base environment, and then remove the duplicate base environments. The application should continue running normally after the repair is complete.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
