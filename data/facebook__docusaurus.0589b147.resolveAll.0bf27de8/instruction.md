# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain GFM (GitHub Flavored Markdown) features are not being processed correctly. It seems like some resolvers are being skipped during the parsing phase, causing incomplete or incorrect rendering of markdown content.

### Reproduction

```js
// Example markdown that fails to parse correctly
const markdown = `
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |

~~strikethrough text~~

- [ ] Task item
`;

// When parsing this markdown, some GFM features don't render properly
const result = parse(markdown);
// Expected: proper table, strikethrough, and task list rendering
// Actual: some features are missing or malformed
```

### Expected behavior

All GFM features (tables, strikethrough, task lists, etc.) should be properly parsed and rendered. The resolvers should process all constructs exactly once to ensure correct output.

### Additional context

This appears to affect multiple GFM features simultaneously. Sometimes the output is completely missing certain elements that should be present in the final AST.

---
Repository: /testbed
