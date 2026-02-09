# Bug Report

### Describe the bug

Markdown link destinations are not being parsed correctly. Links with angle bracket syntax (`<url>`) are being treated as raw URLs, and regular URLs are being treated as if they have angle brackets.

### Reproduction

```markdown
[link text](<https://example.com>)
[link text](https://example.com)
```

The first link (with angle brackets) should be parsed as a literal/enclosed destination, but it's being parsed as a raw destination instead. The second link (without angle brackets) is incorrectly being parsed as if it had angle brackets.

It looks like the condition checking for the `<` character (code 60) got inverted somehow - now it's triggering the enclosed path when it shouldn't and vice versa.

### Expected behavior

- `[link](<url>)` should parse the URL as an enclosed/literal destination
- `[link](url)` should parse the URL as a raw destination
- Links should render correctly in the output

### System Info
- remark version: 15.0.1
- Browser: N/A (server-side parsing)

---
Repository: /testbed
