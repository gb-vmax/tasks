# Bug Report

### Describe the bug

The `no-html-links` rule is incorrectly flagging valid URLs as violations. After a recent change, URLs with protocols (like `http://`, `https://`, `mailto:`, etc.) are no longer being recognized as fully resolved URLs, causing false positives.

### Reproduction

```js
// This should be recognized as a fully resolved URL but isn't
<a href="https://example.com">Link</a>

// Same issue with other protocols
<a href="mailto:test@example.com">Email</a>
<a href="ftp://files.example.com">FTP</a>
```

All of these valid URLs are now being flagged by the linter even though they have proper protocols and should be considered fully resolved.

### Expected behavior

URLs with valid protocols should be recognized as fully resolved and not trigger the `no-html-links` rule. The rule should only flag relative or incomplete URLs.

### System Info
- eslint-plugin version: latest
- Node version: 18.x

---
Repository: /testbed
