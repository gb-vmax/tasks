# Bug Report

### Describe the bug

I'm experiencing an issue when trying to update a local project to remote. The function appears to have duplicate code blocks and the `sessionId` parameter is being handled incorrectly.

### Reproduction

```js
await updateLocalProjectToRemote({
  project: myProject,
  organizationId: 'org-123',
  vcs: myVcs,
  sessionId: 'valid-session-id'
});
```

When calling `updateLocalProjectToRemote` with a valid `sessionId`, the request fails because the sessionId is being set to an empty string when it shouldn't be.

### Expected behavior

The function should properly pass the `sessionId` to the API request. If a sessionId is provided, it should be used. If not provided (null/undefined), then it should default to an empty string.

### Additional context

Looking at the code, there seems to be some duplication in the function body and the logic for handling `sessionId` appears inverted - it's checking `!sessionId ? sessionId : ''` which would set an empty string when a sessionId IS provided, which is the opposite of what we want.

This is blocking our ability to sync projects to the remote server when authenticated.

---
Repository: /testbed
