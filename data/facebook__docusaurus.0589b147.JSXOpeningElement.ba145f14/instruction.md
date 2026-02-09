# Bug Report

### Describe the bug

The `no-html-links` ESLint rule is not correctly identifying fully resolved URLs and is incorrectly flagging valid external links that should be ignored when `ignoreFullyResolved` option is enabled.

### Reproduction

```jsx
// This should NOT trigger the rule when ignoreFullyResolved is true
<a href="https://example.com">Link</a>

// This should also NOT trigger the rule
<a href={`https://example.com`}>Link</a>
```

With the `ignoreFullyResolved` option enabled, these fully qualified URLs should be allowed, but they're still being flagged by the linter.

### Expected behavior

When `ignoreFullyResolved` is set to `true`, the rule should allow `<a>` tags with fully resolved URLs (starting with `http://` or `https://`) and only flag relative or internal links.

### Additional context

This seems to have started happening recently. The rule is being too aggressive and flagging links that should be exempt based on the configuration.

---
Repository: /testbed
