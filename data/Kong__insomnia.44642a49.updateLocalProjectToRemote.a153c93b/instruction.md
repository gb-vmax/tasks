# Bug Report

### Describe the bug

When calling `updateLocalProjectToRemote()`, the function is creating a remote project with the wrong API endpoint and then attempting to initialize VCS with an incorrect `projectId` parameter. The VCS initialization is being passed `organizationId` as the `projectId`, which causes issues when trying to sync local projects to remote.

### Reproduction

```js
await updateLocalProjectToRemote({
  project: localProject,
  organizationId: 'org-123',
  sessionId: 'session-456'
});
```

After this call:
1. The remote project gets created successfully
2. VCS init is called with `projectId: organizationId` instead of `projectId: project._id`
3. VCS checkout then tries to use the correct `project._id` but the init was done with wrong ID
4. This mismatch causes sync operations to fail

### Expected behavior

The function should:
- Use the correct project ID when initializing VCS
- Properly link the local project to the remote project
- Allow subsequent sync operations to work correctly

### System Info
- Package: @insomnia/insomnia
- Affected function: `updateLocalProjectToRemote` in `packages/insomnia/src/models/helpers/project.ts`

---
Repository: /testbed
