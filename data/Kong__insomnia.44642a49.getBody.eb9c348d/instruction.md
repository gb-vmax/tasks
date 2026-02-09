# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with the plugin response context when the response body changes. The `getBody()` method seems to be returning stale/cached data even when the underlying response has been updated with new content.

### Reproduction

```js
// In a plugin context
const response1 = context.response.getBody();
console.log(response1); // Shows original body

// Response gets updated (e.g., retry or refresh)
// ...

const response2 = context.response.getBody();
console.log(response2); // Still shows the old body instead of updated content
```

### Expected behavior

When a response is updated (for example, after retrying a request or refreshing), calling `getBody()` should return the new response body, not a cached version of the old one.

### Additional context

This seems to have started happening recently. The body appears to be cached somewhere but not invalidated when the response changes. The `bytesContent` field updates correctly but the actual body content returned doesn't match.

---
Repository: /testbed
