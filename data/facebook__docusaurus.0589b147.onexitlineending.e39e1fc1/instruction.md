# Bug Report

### Describe the bug

I'm experiencing an issue with line ending handling in MDX content. It seems like hard breaks and regular line endings are being processed incorrectly, causing unexpected behavior in the rendered output.

When I have content with hard breaks (double spaces at the end of a line), they're not being preserved correctly. The parser appears to be treating them the same as regular line endings or vice versa.

### Reproduction

```mdx
This is a line with a hard break  
This should be on a new line but close to the previous one

This is a normal paragraph
with a regular line break that should stay together
```

The hard break (two spaces after "hard break") should create a `<br>` element, but instead it's being treated like a normal line ending. Similarly, regular line endings in paragraphs seem to be handled inconsistently.

### Expected behavior

- Hard breaks (lines ending with two spaces) should create `<br>` elements
- Regular line endings within paragraphs should be preserved as spaces
- The position tracking for these tokens should be accurate

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The line ending logic might have gotten inverted somehow?

---
Repository: /testbed
