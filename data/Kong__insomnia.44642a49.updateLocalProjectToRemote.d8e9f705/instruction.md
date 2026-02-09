# Bug Report

### Describe the bug

After a recent update, the project creation flow seems to be hanging or failing silently when trying to convert local projects to remote/cloud projects. The operation doesn't complete and there's no clear error message shown to the user.

### Reproduction

1. Create a local project in Insomnia
2. Attempt to sync/convert it to a cloud project by linking it to an organization
3. The operation appears to start but never completes
4. No error feedback is provided to the user

### Expected behavior

The project should be successfully created on the cloud and synced, or if it fails, a clear error message should be displayed. The operation should complete within a reasonable timeframe.

### Additional context

This seems to affect the project conversion workflow specifically. Regular project operations work fine, but the cloud sync functionality appears broken. It's possible this is related to network retry logic or error handling during the API call to create the remote project.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
