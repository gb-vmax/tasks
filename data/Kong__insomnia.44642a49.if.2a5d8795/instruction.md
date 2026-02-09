# Bug Report

### Describe the bug
After a recent update, I'm experiencing an issue where response bodies are not being read correctly. When I try to view a response, I get duplicate content or the application seems to be reading from an old cached version even though the actual response file has changed.

### Reproduction
```js
// Make a request that returns a response body
const response = await sendRequest();

// Try to get the body buffer
const body = getBodyBuffer(response);

// The body appears to be duplicated or contains stale data
// Expected: Fresh response body content
// Actual: Old cached content or duplicated data
```

Steps to reproduce:
1. Make an API request and save the response
2. Make the same request again (or a different one that uses the same bodyPath)
3. Try to read the response body
4. The body content doesn't match what's actually in the response file

### Expected behavior
Each call to `getBodyBuffer()` should return the current content from the response body file, not cached or duplicated data.

### System Info
- Insomnia version: latest
- OS: Various

This seems to have started happening recently. The response body reading logic might have an issue with how it's handling the file reads.

---
Repository: /testbed
