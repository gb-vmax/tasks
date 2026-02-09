# Bug Report

### Describe the bug

When adding headers to a request using `addHeader()`, duplicate headers are always being added to the request even when they have the same key. There's no way to control how duplicate headers should be handled (replace existing, merge values, or add as duplicate).

### Reproduction

```js
const request = new Request({
  url: 'https://api.example.com',
});

// Add a header
request.addHeader({ key: 'Authorization', value: 'Bearer token1' });

// Add another header with the same key
request.addHeader({ key: 'Authorization', value: 'Bearer token2' });

// Expected: Should be able to control duplicate behavior
// Actual: Both headers are added, resulting in duplicate Authorization headers
```

The current behavior always adds headers without checking for duplicates. In many cases, you want to replace an existing header or merge values (especially for headers like `Accept` or `Cache-Control` that can have comma-separated values).

### Expected behavior

The `addHeader()` method should support options to control duplicate header handling:
- Replace existing header with the same key
- Merge values with existing header
- Add as duplicate (current behavior)

It would also be helpful to have case-insensitive key matching since HTTP headers are case-insensitive by specification.

### Additional context

This is particularly problematic when building requests programmatically where you might not know if a header was already added earlier in the code. Having to manually check and remove existing headers before adding new ones is cumbersome.

---
Repository: /testbed
