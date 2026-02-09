# Bug Report

### Describe the bug

When creating a Response object with duplicate headers (same header name with different casing), only the last header value is kept instead of preserving all headers. This breaks scenarios where multiple headers with the same name should coexist (like `Set-Cookie`).

### Reproduction

```js
const response = new Response({
  code: 200,
  header: [
    { key: 'Content-Type', value: 'application/json' },
    { key: 'Set-Cookie', value: 'session=abc123' },
    { key: 'set-cookie', value: 'user=john' },
    { key: 'SET-COOKIE', value: 'theme=dark' }
  ]
});

// Only one Set-Cookie header is present
console.log(response.headers.count()); // Expected: 4, Actual: 2
```

### Expected behavior

All headers should be preserved, even when they have the same name with different casing. HTTP allows multiple headers with the same name (case-insensitive), especially for headers like `Set-Cookie` where each value should be a separate header entry.

The current behavior appears to be deduplicating headers by their lowercase key, which causes data loss when multiple headers with the same name are provided.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
