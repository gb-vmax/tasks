# Bug Report

### Describe the bug

The plugin `data.import.uri()` function doesn't accept an object parameter with options, even though the implementation seems to support it. When trying to pass configuration options like `merge`, `workspaceId`, or `retries`, the function fails or ignores these parameters.

### Reproduction

```js
// This should work but doesn't seem to be properly supported
await context.data.import.uri({
  uri: 'https://example.com/api-spec.json',
  options: {
    merge: true,
    workspaceId: 'wrk_123',
    retries: 3
  }
});

// Currently only the string format works
await context.data.import.uri('https://example.com/api-spec.json');
```

### Expected behavior

The function should accept both formats:
1. A simple string URI for basic imports
2. An object with `uri` and `options` properties for advanced configuration including merge behavior, workspace targeting, and retry logic

The options should allow controlling:
- Whether to merge with existing resources (`merge`)
- Which workspace to import into (`workspaceId`)
- Number of retry attempts for failed fetches (`retries`)

### Additional context

This would be really useful for plugin developers who need more control over the import process, especially when dealing with unreliable network connections or needing to merge imported data with existing workspaces.

---
Repository: /testbed
