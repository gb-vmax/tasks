# Bug Report

### Describe the bug

The `no-html-links` rule is incorrectly flagging valid relative URLs as fully resolved URLs. Links that should be allowed (like relative paths `/about`, `./contact`, or `../home`) are being treated as if they have a protocol, causing the linting rule to behave incorrectly.

### Reproduction

```jsx
// These relative links are being incorrectly handled
<a href="/about">About</a>
<a href="./contact">Contact</a>
<a href="../home">Home</a>
<a href="docs/guide">Guide</a>
```

The rule should distinguish between:
- Fully resolved URLs with protocols: `https://example.com`, `http://site.com`
- Relative URLs without protocols: `/path`, `./path`, `../path`, `path`

### Expected behavior

Relative URLs (paths without protocols) should be treated differently from fully resolved URLs with protocols. The rule should correctly identify when a URL has a valid protocol vs when it's just a relative path.

### System Info
- eslint-plugin version: latest
- Node version: 18.x

---
Repository: /testbed
