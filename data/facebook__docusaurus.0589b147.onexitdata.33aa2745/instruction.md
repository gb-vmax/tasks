# Bug Report

### Describe the bug

I'm experiencing an issue with text content ordering in markdown parsing. When parsing markdown with certain text patterns, the content appears to be reversed or in the wrong order.

### Reproduction

```js
// Parse markdown with text content
const result = remark().parse('some text content');

// The text appears in reversed order
// Expected: "some text content"
// Actual: content appears backwards
```

I noticed this when processing markdown documents - the text within nodes seems to be concatenated in the wrong direction, causing the final output to have reversed text.

### Expected behavior

Text content should maintain its original order when parsed. The parser should append new text to the end of existing content, not prepend it.

### System Info
- remark version: 15.0.1

Has anyone else encountered this? It seems like the text serialization might be happening in reverse.

---
Repository: /testbed
