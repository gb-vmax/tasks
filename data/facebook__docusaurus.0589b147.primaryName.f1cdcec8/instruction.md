# Bug Report

### Describe the bug

JSX tags in MDX are not being parsed correctly - they seem to consume characters indefinitely without properly terminating. This causes the parser to hang or behave unexpectedly when processing JSX elements.

### Reproduction

```mdx
<Component />
```

When trying to parse a simple self-closing JSX tag like the above, the parser doesn't properly recognize the end of the tag name and continues processing characters that shouldn't be part of the name.

This also affects:
- Regular JSX tags: `<div>content</div>`
- Tags with attributes: `<Component prop="value" />`
- Namespaced tags: `<ns:Component />`

### Expected behavior

The parser should correctly identify the end of a JSX tag name when it encounters characters like `/`, `.`, `:`, `>`, `{`, or whitespace, and proceed to parse the rest of the tag (attributes, closing bracket, etc.).

### System Info
- MDX version: 3.0.0
- Node version: Latest

---
Repository: /testbed
