# Bug Report

### Describe the bug

The `no-html-links` rule is incorrectly flagging valid URLs with protocols as errors. When I use a standard link with a protocol like `https://` or `http://`, the linter is reporting it as a violation even though these are fully qualified URLs.

### Reproduction

```jsx
// This is being flagged as an error but shouldn't be
<a href="https://example.com">Link</a>
<a href="http://example.com">Link</a>

// Same with other protocols
<a href="ftp://files.example.com">FTP Link</a>
```

All of these valid, fully-resolved URLs are being reported by the `no-html-links` rule when they should be allowed.

### Expected behavior

URLs with valid protocols (https://, http://, ftp://, etc.) should be recognized as fully resolved and not trigger the `no-html-links` rule. Only relative URLs or malformed links should be flagged.

### Additional context

This seems to have started happening recently. Previously these links were working fine without any linter errors. The rule appears to be inverting its logic somehow - treating valid URLs as invalid and vice versa.

---
Repository: /testbed
