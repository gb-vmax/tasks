# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where phrasing content (inline elements like emphasis, links, etc.) inside container elements is not being processed correctly. The parser seems to be ignoring or incorrectly handling inline markdown syntax within certain container blocks.

### Reproduction

```js
const markdown = `
**bold text** inside a container

*italic text* with [a link](https://example.com)
`;

// Parse the markdown
const result = parse(markdown);

// Expected: bold, italic, and link nodes should be properly created
// Actual: phrasing content is not being recognized or processed
```

When I try to parse markdown with inline formatting inside container elements, the inline elements either don't get parsed at all or the structure comes out wrong.

### Expected behavior

Inline markdown syntax (bold, italic, links, code spans, etc.) should be properly parsed and converted to their respective AST nodes when they appear inside container elements.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
