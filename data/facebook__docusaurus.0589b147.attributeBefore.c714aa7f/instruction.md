# Bug Report

### Describe the bug

I'm encountering an issue with MDX tag parsing where self-closing tags and regular closing tags appear to be handled incorrectly. The parser seems to be confusing the `/` (forward slash) and `>` (greater than) characters when processing tag endings.

### Reproduction

When trying to parse MDX components with self-closing syntax, the behavior is not what I expect:

```mdx
<MyComponent />
```

The tag doesn't seem to be recognized as self-closing properly. Similarly, regular closing tags with `>` are also being mishandled.

This affects both:
- Self-closing tags like `<Component />`
- Regular tags with attributes like `<Component attr="value">`

### Expected behavior

The parser should correctly distinguish between:
- `/` followed by `>` for self-closing tags (e.g., `<Component />`)
- `>` for regular tag endings (e.g., `<Component>`)

Both syntaxes should be parsed correctly and the appropriate markers should be applied.

### Additional context

This seems to have started happening recently. The tag parsing logic appears to be mixing up these two different closing patterns, which breaks MDX component rendering.

---
Repository: /testbed
