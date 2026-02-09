# Bug Report

### Describe the bug

The `no-html-links` ESLint rule is not working as expected. It seems to be flagging all `<a>` tags regardless of their href values, even when they should be ignored according to the configuration.

### Reproduction

```jsx
// This should NOT trigger the rule but it does
<a href="https://example.com">External Link</a>

// This should trigger the rule but it doesn't
<div href="/internal">Not a link</div>
```

With the following ESLint config:
```js
{
  "rules": {
    "no-html-links": ["error", { "ignoreFullyResolved": true }]
  }
}
```

### Expected behavior

When `ignoreFullyResolved` is set to `true`, the rule should:
- NOT flag `<a>` tags with fully resolved URLs (like `https://example.com`)
- Flag `<a>` tags with relative URLs (like `/internal`)
- Only check `<a>` tags, not other elements

Currently it seems to be doing the opposite - it's checking everything except `<a>` tags.

### System Info
- eslint-plugin version: latest
- ESLint: 8.x

---
Repository: /testbed
