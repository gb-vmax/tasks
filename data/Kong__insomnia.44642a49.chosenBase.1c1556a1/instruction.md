# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with workspace initialization. The application seems to hang or crash during startup when loading workspaces that have multiple cookie jars associated with them.

### Reproduction

1. Create a workspace with multiple cookie jars (this can happen if you've imported data or had sync conflicts)
2. Restart the application
3. The workspace fails to load properly

I noticed this started happening after updating to the latest version. Previously, the app would automatically merge duplicate cookie jars, but now it seems like that cleanup process isn't completing.

### Expected behavior

The application should handle workspaces with multiple cookie jars gracefully, either by merging them automatically or at least loading the workspace without crashing.

### Additional context

This seems to affect workspaces that were created or synced before the update. New workspaces don't seem to have this problem. The issue is particularly noticeable when you have cookie jars with different numbers of cookies - the app should probably keep the one with the most data.

---
Repository: /testbed
