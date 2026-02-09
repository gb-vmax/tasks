# Bug Report

### Describe the bug

I'm encountering an issue with markdown link parsing where the URL destination in links is not being extracted correctly. When parsing markdown with links, the resulting AST seems to have incorrect or missing URL values.

### Reproduction

```js
const markdown = '[link text](https://example.com)';
const ast = parseMarkdown(markdown);

// The link node's url property is not set correctly
console.log(ast.children[0].url); // Expected: 'https://example.com'
```

This affects both inline links and reference-style links. The link text parses fine, but the destination URL ends up being wrong or undefined.

### Expected behavior

The parser should correctly extract and set the URL from the link destination string. The `url` property on link nodes should contain the actual destination URL from the markdown source.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
