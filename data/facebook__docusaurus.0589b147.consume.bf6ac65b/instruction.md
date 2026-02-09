# Bug Report

### Describe the bug
I'm experiencing incorrect position tracking when parsing markdown content with line endings. The offset calculation appears to be wrong, causing the parser to report incorrect character positions in the source text.

### Reproduction
```js
const processor = remark();
const result = processor.parse('# Heading\n\nSome text');

// Check the position information for nodes
// The offset values are incorrect for content after line breaks
```

When parsing markdown with newlines (especially CRLF line endings), the position tracking gets messed up. The `offset` field in the position data doesn't match the actual character positions in the source string.

### Expected behavior
The position information should accurately reflect the character offsets in the original markdown source, accounting for different line ending types (LF vs CRLF).

### Additional context
This seems to affect any markdown parsing that involves line breaks. The column and line numbers might be correct, but the offset calculation is definitely off. This breaks tools that rely on accurate source positions for things like syntax highlighting or error reporting.

---
Repository: /testbed
