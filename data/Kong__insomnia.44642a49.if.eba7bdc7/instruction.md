# Bug Report

### Describe the bug

I'm experiencing an issue where certain paths in templates are being rendered when they should be excluded based on the blacklist regex pattern. It seems like the blacklist filtering is inverted - paths that should be skipped are being processed, and paths that should be processed are being skipped.

### Reproduction

```js
const template = {
  url: '{{ _.baseUrl }}/api',
  headers: {
    auth: '{{ _.secret }}',
    'x-api-key': '{{ _.apiKey }}'
  }
}

const blacklistRegex = /headers\.auth/;

// When rendering with blacklist pattern
const result = await render(template, context, blacklistRegex);

// Expected: headers.auth should NOT be rendered (should stay as template)
// Actual: headers.auth IS rendered, but other paths are not
```

### Expected behavior

When a blacklist regex is provided, only the paths matching that regex should be excluded from rendering. All other paths should be rendered normally. Currently it appears to be doing the opposite - matching paths are rendered while non-matching paths are left as-is.

### System Info

- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
