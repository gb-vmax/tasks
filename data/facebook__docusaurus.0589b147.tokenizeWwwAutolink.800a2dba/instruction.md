# Bug Report

### Describe the bug

I'm experiencing an issue with autolink detection for URLs starting with `www`. It seems like the parser is not correctly recognizing and converting these URLs into clickable links.

### Reproduction

```markdown
Check out www.example.com for more info
```

When this is parsed, the `www.example.com` URL should be automatically converted to a link, but it's not being detected at all.

### Steps to reproduce:
1. Parse markdown text containing a URL that starts with `www.` (without the protocol)
2. The URL is not converted to an autolink
3. Expected: `www.example.com` should be recognized and linkified

### Expected behavior

URLs beginning with `www.` should be automatically detected and converted to links, similar to how full URLs with protocols (like `https://example.com`) are handled.

### Additional context

This affects any markdown content where users write URLs in the common `www.domain.com` format without explicitly adding the protocol. It's a pretty common pattern in user-generated content.

---
Repository: /testbed
