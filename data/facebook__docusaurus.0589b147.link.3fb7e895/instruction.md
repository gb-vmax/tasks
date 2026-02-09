# Bug Report

### Describe the bug

The markdown link generation is completely broken. When trying to convert markdown AST nodes to markdown text, links are not being rendered at all. Instead of generating proper markdown link syntax like `[text](url)` or autolinks like `<url>`, the function appears to be missing or stubbed out.

### Reproduction

```js
const mdast = {
  type: 'link',
  url: 'https://example.com',
  children: [{ type: 'text', value: 'Example' }]
}

// Try to convert to markdown
const result = toMarkdown(mdast)

// Expected: "[Example](https://example.com)"
// Actual: Returns nothing or throws an error
```

Also affects autolinks:

```js
const autolink = {
  type: 'link',
  url: 'https://example.com',
  children: [{ type: 'text', value: 'https://example.com' }]
}

// Expected: "<https://example.com>"
// Actual: Broken
```

### Expected behavior

Links should be properly formatted as markdown:
- Regular links: `[text](url)`
- Links with titles: `[text](url "title")`
- Autolinks: `<url>`
- Links with special characters in URLs should use angle brackets: `<url with spaces>`

### System Info

- remark version: 15.0.1
- Node version: Latest

This is blocking our entire markdown generation pipeline. Any documents with links are now completely unusable.

---
Repository: /testbed
