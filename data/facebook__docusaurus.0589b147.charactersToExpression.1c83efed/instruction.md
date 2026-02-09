# Bug Report

### Describe the bug
I'm encountering an issue with character escaping in HTML entities when using rehype-stringify. Special regex characters are not being properly escaped, which causes the generated regular expressions to malfunction.

### Reproduction
When processing HTML content that contains special characters like `[`, `]`, `(`, `)`, `{`, `}`, `|`, `\`, `^`, `$`, `+`, `*`, `?`, or `.`, these characters should be escaped in the regular expression pattern. However, it appears they're being passed through without proper escaping.

For example, when trying to match characters that include brackets or parentheses:
```js
// Characters like [ ] ( ) { } should be escaped in regex
// Currently they're treated as regex metacharacters instead of literal characters
```

This causes the regex pattern to be invalid or match unintended strings.

### Expected behavior
Special regex metacharacters should be properly escaped with backslashes when building the character expression pattern. The regex should treat these as literal characters to match, not as regex syntax.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
