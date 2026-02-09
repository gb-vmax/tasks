# Bug Report

### Describe the bug
When parsing MDX content with data tokens, the position information for text nodes is incorrect. The end position of text content is being set to the start position of the token instead of the end position, which breaks source mapping and position tracking.

### Reproduction
```js
// Parse some MDX content with text
const result = compile('Some text content here');

// Check the position of the text node
console.log(result.children[0].position);
// Expected: { start: { line: 1, column: 1 }, end: { line: 1, column: 25 } }
// Actual: { start: { line: 1, column: 1 }, end: { line: 1, column: 1 } }
```

The text node's end position is incorrectly set to match the start position, making it appear as if the content has zero length.

### Expected behavior
The position.end should point to the actual end of the text content, not the start. This is important for:
- Source maps
- Error reporting with correct line/column numbers
- Editor integrations that rely on accurate position data

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
