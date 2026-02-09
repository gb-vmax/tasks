# Bug Report

### Describe the bug

I'm encountering an issue when trying to create a project with a `remoteId` that doesn't follow the expected format. The application now throws validation errors for remote IDs that were previously accepted.

### Reproduction

```js
// This used to work but now throws an error
const project = create({
  name: 'My Project',
  remoteId: 'custom_id_12345'
});

// Error: Invalid remoteId format: custom_id_12345. Must start with one of: proj_team, proj_org, proj_
```

Also seeing issues with short remote IDs:

```js
const project = create({
  name: 'Test',
  remoteId: 'proj_123'
});

// Error: Invalid remoteId: proj_123. ID is too short.
```

### Expected behavior

Projects should be created successfully with custom remote IDs, or at least the validation should have been present before to avoid breaking existing code. This seems like a breaking change that wasn't documented.

### Additional context

This started happening recently and is blocking our workflow where we generate custom remote IDs for projects. We have existing projects with remote IDs that don't match these new patterns and can no longer create similar ones.

---
Repository: /testbed
