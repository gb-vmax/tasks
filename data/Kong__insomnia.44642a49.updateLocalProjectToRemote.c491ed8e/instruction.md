# Bug Report

### Describe the bug

I'm experiencing an issue where the project sync is creating duplicate code in the `updateLocalProjectToRemote` function. It looks like there's a syntax error or merge conflict that wasn't properly resolved - the function has duplicate/malformed return statement blocks.

### Reproduction

When trying to push a local project to remote:

```js
await updateLocalProjectToRemote({
  project: localProject,
  organizationId: 'org-123',
  sessionId: 'session-456',
  vcs: vcsInstance
});
```

The function fails to execute properly because the code structure is broken. Looking at the source, there appear to be two incomplete code blocks that don't form a valid function body.

### Expected behavior

The function should successfully:
1. Create a new cloud project via POST request
2. Update the local project with the remote ID
3. Push the initial snapshot
4. Return the new cloud project object

Instead, the function has malformed code that prevents it from running at all.

### Additional context

This seems to have been introduced recently. The function definition appears to have duplicate closing braces and an orphaned `error: string;` type definition that's not part of any proper type declaration.

---
Repository: /testbed
