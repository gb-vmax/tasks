# Bug Report

### Describe the bug

When trying to retrieve workspace metadata by Git repository ID, the function is returning incorrect results. It appears to be matching workspaces that shouldn't match, possibly due to type coercion issues.

### Reproduction

```js
// Create workspace meta with gitRepositoryId as a string
const workspaceMeta1 = {
  gitRepositoryId: "123",
  // ... other properties
}

// Create another workspace meta with gitRepositoryId as a number
const workspaceMeta2 = {
  gitRepositoryId: 123,
  // ... other properties
}

// Try to get by string ID
const result = await getByGitRepositoryId("123")

// Both workspaces are returned instead of just the one with string "123"
```

### Expected behavior

The function should only return workspace metadata that exactly matches the provided `gitRepositoryId`, with strict type checking. If I'm searching for the string `"123"`, it should not return items with the numeric value `123`.

### Additional context

This seems to have started happening recently. The function used to work correctly and only return exact matches. Now it's returning multiple results when it should only return one specific workspace meta.

---
Repository: /testbed
