# Bug Report

### Describe the bug

The `no-html-links` ESLint rule is not working correctly when `ignoreFullyResolved` option is enabled. It seems to be reporting errors for anchor tags with fully resolved URLs that should be ignored according to the configuration.

### Reproduction

```jsx
// With ignoreFullyResolved: true in ESLint config
<a href="https://example.com">Link</a>
```

The rule reports an error for this link even though it's a fully resolved URL and should be ignored based on the `ignoreFullyResolved` setting.

### Expected behavior

When `ignoreFullyResolved` is set to `true`, anchor tags with fully resolved URLs (like `https://example.com`) should not trigger the lint error. The rule should only flag relative or incomplete URLs.

### Additional context

This appears to have started happening recently. The rule was working fine before and correctly ignoring fully resolved URLs when the option was enabled.

---
Repository: /testbed
