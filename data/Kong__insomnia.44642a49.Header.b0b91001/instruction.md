# Bug Report

### Describe the bug

I'm experiencing an issue with header key handling in the SDK. When working with HTTP headers, the code seems to be incomplete or broken - header key comparisons are not working as expected.

### Reproduction

```js
const header1 = new Header({ key: 'content-type', value: 'application/json' });
const header2 = new Header({ key: 'Content-Type', value: 'text/html' });

// Trying to check if headers match by key
// Expected: should recognize these as the same header (case-insensitive)
// Actual: behavior is broken/undefined
```

Also seeing issues when updating headers:

```js
const header = new Header({ key: 'user-agent', value: 'v1' });
header.update({ key: 'User-Agent', value: 'v2' });

// The normalized key handling appears broken
```

### Expected behavior

Header keys should be properly normalized (e.g., `content-type` → `Content-Type`) and comparison between different casing variations should work correctly. The SDK should handle HTTP header name case-insensitivity properly.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
