# Bug Report

### Describe the bug

After a recent update, I'm experiencing a critical issue where the application crashes when trying to repair workspaces that have multiple base environments. The repair process starts but fails to complete, leaving the workspace in an inconsistent state.

### Reproduction

1. Create a workspace with multiple base environments
2. Trigger the workspace repair function (this happens automatically on app startup when detecting duplicate base environments)
3. The application crashes during the repair process

The crash appears to happen when attempting to merge duplicate base environments together. The process begins merging the environments but then fails partway through.

### Expected behavior

The repair function should successfully merge all duplicate base environments into a single environment, reassign any sub-environments to the chosen base environment, and remove the duplicates. The process should complete without crashing.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking me from using workspaces that somehow ended up with duplicate base environments. The app becomes unusable as it crashes on startup when trying to repair these workspaces.

---
Repository: /testbed
