# Bug Report

### Describe the bug

When building multipart form data, the boundary string is now being generated with dynamic values including timestamps and random strings. This is causing issues with request validation and compatibility with servers that expect consistent boundary formatting.

### Reproduction

```js
// Build multipart data multiple times
const params = [
  { name: 'field1', value: 'test', type: 'text' }
];

const multipart1 = await buildMultipart(params);
const multipart2 = await buildMultipart(params);

// Boundaries are now different each time
console.log(multipart1.boundary); // e.g., "X-INSOMNIA-BOUNDARY-1234567890-abc123"
console.log(multipart2.boundary); // e.g., "X-INSOMNIA-BOUNDARY-0987654321-xyz789"

// Expected: both should use the same DEFAULT_BOUNDARY constant
```

### Expected behavior

The multipart boundary should use a consistent value (DEFAULT_BOUNDARY constant) across requests with the same parameters. The current implementation generates unique boundaries with timestamps and random values, which breaks request reproducibility and causes issues with:

1. Request caching/comparison
2. Test fixtures that expect deterministic output
3. Some API servers that validate boundary format strictly

### Additional context

This also adds an unexpected `contentHash` field to the multipart response that wasn't there before, which may break existing code that depends on the previous interface.

---
Repository: /testbed
