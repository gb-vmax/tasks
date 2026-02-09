# Bug Report

### Describe the bug

When updating a local project to remote, the function returns the wrong `remoteId` value. After successfully creating a remote project and updating the local project with the new remote ID, the returned object still contains the old `remoteId` from the project parameter instead of the newly assigned remote ID.

### Reproduction

```js
const project = {
  _id: 'local-project-123',
  name: 'My Project',
  remoteId: null, // or undefined
};

const result = await updateLocalProjectToRemote({
  project,
  organizationId: 'org-456',
  sessionId: 'session-789',
  vcs,
});

// Expected: result.remoteId should be the new remote ID from the API
// Actual: result.remoteId is still null (the old value)
console.log(result.remoteId); // prints null instead of the new remote ID
```

### Expected behavior

The function should return the project object with the newly assigned `remoteId` from the cloud API, not the original `remoteId` value from the input project parameter.

### Additional context

This appears to be a logic issue in the return statement where it's using `project.remoteId` as a fallback, but that's the old value before the update. The function should return the new `remoteId` that was just assigned from the API response.

---
Repository: /testbed
