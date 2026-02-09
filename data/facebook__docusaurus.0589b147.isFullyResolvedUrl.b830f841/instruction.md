# Bug Report

### Describe the bug

The `no-html-links` ESLint rule is incorrectly flagging fully qualified URLs (like `https://example.com`) as violations, while allowing relative URLs (like `/about` or `./page`) to pass without warnings.

### Reproduction

```jsx
// This should be allowed but triggers a warning
<a href="https://example.com">External Link</a>

// This should trigger a warning but is allowed
<a href="/relative-path">Relative Link</a>
```

The rule seems to have inverted logic - it's treating absolute URLs as problems and relative URLs as acceptable, which is the opposite of what the rule is supposed to do.

### Expected behavior

The rule should allow fully resolved URLs with protocols (like `https://`, `http://`, etc.) and flag relative or incomplete URLs that don't have a protocol.

### System Info
- ESLint plugin version: latest
- Node version: 18.x

---
Repository: /testbed
