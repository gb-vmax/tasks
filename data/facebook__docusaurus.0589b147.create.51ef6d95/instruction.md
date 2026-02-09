# Bug Report

### Describe the bug

The `no-html-links` ESLint rule is incorrectly flagging all `<a>` tags as violations, even when they should be allowed. It appears that the rule is now triggering on every anchor element regardless of whether it's a valid HTML link or not.

### Reproduction

```jsx
// This should NOT trigger the rule but it does
<a href="/docs/intro">Documentation</a>

// This should also NOT trigger the rule but it does
<a href="https://example.com">External Link</a>

// With ignoreFullyResolved option enabled, this should be allowed but isn't
<a href="https://example.com/page">Fully Resolved Link</a>
```

All of these examples are now being flagged by the linter when they shouldn't be.

### Expected behavior

The rule should only flag anchor tags that are actual HTML links that need to be converted. Normal anchor tags with valid `href` attributes should not trigger violations.

When `ignoreFullyResolved` is enabled, fully resolved URLs (like `https://example.com`) should be allowed without triggering the rule.

### System Info
- eslint-plugin version: latest
- ESLint version: 8.x

---
Repository: /testbed
