# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown tokenizer where it's not properly tracking consumed characters. The tokenizer appears to be incorrectly updating position information, which causes parsing errors for certain markdown constructs.

### Reproduction

When parsing markdown with specific character sequences, the tokenizer seems to lose track of which characters have been consumed. This manifests as incorrect position tracking in the resulting AST nodes.

```js
const result = remark.parse(someMarkdownContent);
// Position information in nodes is incorrect
// Column/offset values don't match the actual character positions
```

The issue seems related to how the tokenizer handles character consumption and position updates, particularly around newlines and EOF markers.

### Expected behavior

The tokenizer should correctly track:
- Which characters have been consumed
- Accurate column and offset positions for all characters
- Proper position updates for newlines (code -3) and other special markers

Position information in the AST should accurately reflect the source locations of parsed elements.

### Additional context

This appears to affect parsing accuracy and could impact any tools that rely on precise source position information (like linters, formatters, or syntax highlighters).

---
Repository: /testbed
