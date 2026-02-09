# Bug Report

### Describe the bug

When creating new responses, the system is keeping the wrong responses in the database. Instead of keeping the most recent responses and removing the old ones, it seems to be doing the opposite - removing the recent responses and keeping the older ones.

### Reproduction

```js
// Create multiple responses for a request
await response.create({ parentId: requestId }, maxResponses = 5);
await response.create({ parentId: requestId }, maxResponses = 5);
await response.create({ parentId: requestId }, maxResponses = 5);
// ... create more responses

// Expected: Only the 5 most recent responses should remain
// Actual: The 5 most recent responses are deleted, older ones are kept
```

### Steps to reproduce:
1. Send multiple requests to the same endpoint (more than the maxResponses limit)
2. Check the response history
3. Notice that the newest responses are missing and old responses are still present

### Expected behavior
When creating a new response with `maxResponses` set to a specific limit (e.g., 5), the system should keep the most recent responses and remove older ones that exceed the limit.

### Additional context
This also seems to affect the environment filtering logic. When `filterResponsesByEnv` setting is enabled, responses from the current environment should be filtered, but it appears to be working in reverse.

---
Repository: /testbed
