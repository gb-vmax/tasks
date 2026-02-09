# Bug Report

### Describe the bug

I'm experiencing incorrect position tracking when parsing markdown with emphasis/attention markers. The column, offset, and buffer index calculations appear to be wrong, leading to corrupted position data in the AST nodes.

### Reproduction

```js
const remark = require('remark');
const parse = remark.parse;

// Parse markdown with emphasis
const ast = parse('This is **bold** text');

// Check the position data of the emphasis node
console.log(ast.children[0].children[1].position);
```

The position information for the emphasis markers shows incorrect offset and _bufferIndex values. The offset seems to be accumulating incorrectly (using column value instead of the actual offset), and _bufferIndex is being decremented when it should be incremented.

### Expected behavior

Position tracking should accurately reflect the actual character positions in the source markdown. The offset should increment by the actual offset amount, and _bufferIndex should track the buffer position correctly.

### Additional context

This affects any markdown parsing that involves emphasis markers (`*`, `_`, etc.) and makes it difficult to accurately map AST nodes back to their source positions. The issue is in the `movePoint` function which is used during attention tokenization.

---
Repository: /testbed
