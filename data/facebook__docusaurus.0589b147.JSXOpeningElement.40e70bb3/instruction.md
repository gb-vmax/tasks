# Bug Report

### Describe the bug

The `no-html-links` ESLint rule is now incorrectly flagging all anchor tags (`<a>`) in JSX code, even when they should be allowed according to the rule configuration. After a recent update, the rule appears to have inverted its logic and is reporting errors on valid anchor elements.

### Reproduction

```jsx
// This now incorrectly triggers the no-html-links rule
<a href="https://example.com">Link</a>

// Even with ignoreFullyResolved option enabled, 
// fully resolved URLs are being flagged
<a href="https://www.google.com">Google</a>

// Template literals with static URLs also trigger the error
<a href={`https://example.com/page`}>Page</a>
```

With the `ignoreFullyResolved` option set to `true`, the rule should allow anchor tags with fully resolved URLs (like `https://example.com`), but instead it's reporting violations on all anchor elements regardless of the href value.

### Expected behavior

- Anchor tags with fully resolved URLs should be allowed when `ignoreFullyResolved` is enabled
- Only anchor tags with relative or internal links should trigger the rule violation
- The rule should correctly identify and skip valid anchor elements

### System Info
- ESLint plugin version: latest
- Node version: 18.x

This seems to have broken after a recent change. All of my existing code that was previously passing linting is now showing errors for every `<a>` tag.

---
Repository: /testbed
