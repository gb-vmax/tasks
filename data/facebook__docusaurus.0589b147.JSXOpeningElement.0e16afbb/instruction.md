# Bug Report

### Describe the bug

The `no-html-links` ESLint rule is incorrectly flagging anchor tags with fully resolved URLs when `ignoreFullyResolved` is enabled. Links that should be allowed are being reported as violations.

### Reproduction

```jsx
// This should NOT trigger a lint error when ignoreFullyResolved is true
<a href="https://example.com">External Link</a>

// This should also NOT trigger an error
<a href={`https://example.com/page`}>Template Link</a>
```

With the following ESLint config:
```js
{
  rules: {
    'no-html-links': ['error', { ignoreFullyResolved: true }]
  }
}
```

### Expected behavior

When `ignoreFullyResolved` option is set to `true`, anchor tags with fully resolved URLs (starting with `http://` or `https://`) should be ignored and not trigger lint errors.

### Additional context

This seems to have broken recently. The rule is now reporting errors for all anchor tags regardless of whether they have fully resolved URLs or not, even when the `ignoreFullyResolved` option is enabled.

---
Repository: /testbed
