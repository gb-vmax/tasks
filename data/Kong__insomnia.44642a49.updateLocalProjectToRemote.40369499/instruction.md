# Bug Report

### Describe the bug

I'm experiencing an issue with the cloud project creation functionality. When trying to convert a local project to a remote/cloud project, the operation seems to hang or fail silently without proper error handling. The UI doesn't provide any feedback about what's happening during the process.

### Reproduction

```js
// Attempting to update a local project to remote
await updateLocalProjectToRemote({
  project: myLocalProject,
  vcs: vcsInstance,
  sessionId: 'my-session-id',
  organizationId: 'my-org-id'
});

// Expected: Project should be created in the cloud with proper error handling
// Actual: Function appears to fail without completing the project update
```

### Expected behavior

The function should:
1. Successfully create the cloud project with retry logic
2. Complete the project update operation
3. Return appropriate success/error responses

Currently it seems like the function is incomplete or gets cut off midway through execution, preventing the project from being properly updated to remote.

### Additional context

This is blocking our ability to sync local projects to the cloud. The function signature was recently updated to include `onProgress` and `maxRetries` parameters, but the implementation doesn't seem to be fully working.

---
Repository: /testbed
