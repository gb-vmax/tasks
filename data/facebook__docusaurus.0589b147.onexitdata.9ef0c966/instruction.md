# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the position information for text nodes seems incorrect. After parsing markdown content, the `position.start` property of text nodes is being set to the end position instead of maintaining the correct start position.

### Reproduction

```js
const remark = require('remark');
const parsed = remark.parse('Some text content');

// Check the position of the text node
const textNode = parsed.children[0].children[0];
console.log(textNode.position);

// Expected: position.start should point to beginning of text
// Actual: position.start appears to be at the end
```

When parsing any markdown with text content, the position tracking gets messed up. The start position is being overwritten with the end position value.

### Expected behavior

The `position.start` should remain at the beginning of the text node and `position.end` should be at the end. Currently it looks like both are pointing to the same location (the end).

This is causing issues when trying to use the position information for source mapping or extracting the original text ranges.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
