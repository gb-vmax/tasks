# Bug Report

### Describe the bug

After a recent update, response bodies are not being read correctly when the body file is modified. When I make a request, get a response, then the response body file changes on disk, subsequent reads still return the old cached content instead of the updated file content.

### Reproduction

```js
// 1. Make a request and get a response
const response = await makeRequest();
const body1 = getBodyBuffer(response);

// 2. Modify the response body file on disk
fs.writeFileSync(response.bodyPath, 'updated content');

// 3. Try to read the body again
const body2 = getBodyBuffer(response);

// Expected: body2 should contain 'updated content'
// Actual: body2 still contains the old cached content from body1
```

### Expected behavior

When the response body file is modified on disk (e.g., file mtime changes), `getBodyBuffer()` should return the new content from the file, not the cached version. The cache should be invalidated when the file modification time changes.

### Additional context

This seems to be related to caching behavior. The cached entry is being checked against the file's mtime, but even when they match, the stale cached buffer is returned. This is problematic for scenarios where response bodies are updated or regenerated.

---
Repository: /testbed
