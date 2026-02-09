# Bug Report

### Describe the bug

The pathname normalization logic is not working correctly when dealing with trailing slashes. URLs with trailing slashes are being processed incorrectly, resulting in unexpected pathname values.

### Reproduction

```js
// When navigating to a URL with a trailing slash
const location = {
  pathname: '/docs/intro/ ',
  // ... other location properties
}

// The pathname is not being normalized properly
// Expected: '/docs/intro'
// Actual: Different behavior than expected
```

### Steps to reproduce

1. Navigate to a page with a trailing slash in the URL (e.g., `/docs/intro/`)
2. Add whitespace after the trailing slash
3. Observe how the pathname is normalized

### Expected behavior

The pathname should be normalized consistently, removing trailing slashes and trimming whitespace in the correct order to produce clean, canonical URLs.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
