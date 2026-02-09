# Bug Report

### Describe the bug

I'm experiencing an issue with markdown title parsing where backslash escape sequences in titles are not being handled correctly. When a title contains a backslash followed by certain characters, the parsing behavior seems off and the output doesn't match what I'd expect.

### Reproduction

```js
const input = `[link](url "title with \\" quote")`
```

When parsing this markdown, the escaped quote in the title should be properly handled, but instead the title parsing seems to consume characters in the wrong order or skip the escape handling entirely.

### Expected behavior

Backslash escapes in link/image titles should work correctly. For example:
- `"title with \\" quote"` should parse the escaped quote properly
- `"title with \\\\ backslash"` should handle escaped backslashes

The parser should recognize escape sequences before checking for title delimiters or line endings.

### Additional context

This appears to affect any markdown construct that uses titles (links, images, etc.) when those titles contain backslash escape sequences. The issue is specifically with how the escape character is processed during title parsing.

---
Repository: /testbed
