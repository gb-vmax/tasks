# Bug Report

### Describe the bug

I'm experiencing an issue with entity parsing where the offset calculation in the position tracking appears to be incorrect. The offset values being returned don't match what I would expect when parsing entities in MDX content.

### Reproduction

When parsing content with HTML entities, the position information (specifically the offset) seems off:

```js
// Parse content with entities
const content = "Hello &amp; world";
const result = parseEntities(content);

// The position offset tracking is incorrect
// Expected offsets to increment properly but they're not calculating correctly
```

The issue seems to be related to how the `now()` function calculates the offset - it's subtracting the same value twice instead of adding the point offset correctly.

### Expected behavior

The offset in position tracking should accurately reflect the character position in the source content. When parsing entities, the offset should be calculated as `index2 + point4.offset` (or 0 if point4 is undefined), not subtracted.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is causing issues with source maps and error reporting since the positions are incorrectly calculated.

---
Repository: /testbed
