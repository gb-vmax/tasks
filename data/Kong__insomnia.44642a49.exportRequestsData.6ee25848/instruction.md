# Bug Report

### Describe the bug

When exporting workspace data, private documents are being included in the export even when `includePrivateDocs` is set to `false`. The export functionality seems to be inverting the privacy filter logic, causing private items to be exported when they shouldn't be.

### Reproduction

```js
// Export workspace without including private docs
await exportRequestsData(
  workspace,
  false, // includePrivateDocs = false
  'json'
);

// Result: Private documents are still included in the export
// Expected: Private documents should be excluded
```

Steps to reproduce:
1. Create a workspace with some private documents (requests, environments, etc.)
2. Call `exportRequestsData` with `includePrivateDocs` set to `false`
3. Check the exported data

### Expected behavior

When `includePrivateDocs` is `false`, private documents should be filtered out and not included in the exported data. Only public/non-private documents should be exported.

### Additional context

This also seems to affect the descendants filtering - items that should be included (like CookieJar, Environment, ApiSpec, etc.) are being filtered out instead of being included in the export.

---
Repository: /testbed
