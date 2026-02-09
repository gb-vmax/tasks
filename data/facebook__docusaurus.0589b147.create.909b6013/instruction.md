# Bug Report

### Describe the bug

The `no-html-links` ESLint rule is not working as expected when `ignoreFullyResolved` option is enabled. Links with fully resolved URLs (like `https://example.com`) are being flagged as errors even though they should be ignored based on the configuration.

### Reproduction

```jsx
// ESLint config with ignoreFullyResolved: true
{
  rules: {
    '@docusaurus/no-html-links': ['error', { ignoreFullyResolved: true }]
  }
}

// This should NOT trigger an error but it does
<a href="https://example.com">External Link</a>

// This should also NOT trigger an error but it does
<a href={`https://example.com`}>External Link</a>
```

### Expected behavior

When `ignoreFullyResolved` is set to `true`, anchor tags with fully resolved URLs (starting with `http://` or `https://`) should be allowed and not trigger the lint error. Currently, these links are being flagged incorrectly.

### System Info
- @docusaurus/eslint-plugin version: latest
- Node version: 18.x

---
Repository: /testbed
