# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain nested content structures are not being processed correctly. The parser seems to be off by one when calculating positions for content boundaries, leading to incorrect parsing results.

### Reproduction

```js
const markdown = `
* List item with nested content
  
  Nested paragraph
  
  * Nested list item
`;

const result = remark().parse(markdown);
// The positions of nested elements are incorrect
// Content boundaries are shifted by one position
```

When parsing markdown with nested structures (like lists containing paragraphs and sublists), the position tracking gets misaligned. This causes the parser to either skip content or include extra characters that shouldn't be there.

### Expected behavior

The parser should correctly identify and process nested content boundaries. Position calculations for nested elements should accurately reflect their actual positions in the source markdown.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started after a recent update. The position tracking for nested content appears to be incrementing at the wrong point in the loop, causing an off-by-one error in the final output.

---
Repository: /testbed
