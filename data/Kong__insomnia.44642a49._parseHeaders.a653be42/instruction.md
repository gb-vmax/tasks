# Bug Report

### Describe the bug

I'm experiencing an issue with HTTP header parsing where headers with folded/continued lines (multi-line headers) are not being handled correctly. According to RFC 2616, header values can span multiple lines when the continuation line starts with whitespace (space or tab), but these are being parsed as separate headers or ignored entirely.

### Reproduction

When making a request that returns headers with line folding, like:

```
X-Custom-Header: value part one
 continuation of value
```

The header value is truncated or not properly combined. This affects headers that legitimately use line folding for long values.

Example scenario:
1. Server sends a response with a multi-line header value
2. The continuation line starts with a space or tab (as per HTTP spec)
3. The parsed header either loses the continuation part or treats it incorrectly

### Expected behavior

Multi-line header values should be properly combined into a single value with the leading whitespace on continuation lines replaced by a single space, as specified in RFC 2616 section 4.2.

For the example above, the parsed value should be: `"value part one continuation of value"`

### System Info
- Insomnia version: latest
- OS: Various

This seems to have started happening recently. The old header parsing logic was simpler but didn't handle these edge cases from the HTTP specification.

---
Repository: /testbed
