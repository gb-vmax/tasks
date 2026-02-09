# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where line breaks and text content are being handled incorrectly. It seems like the parser is inverting the logic for when to process text versus when to break, causing unexpected behavior in the output.

### Reproduction

When parsing MDX content with specific constructs, the parser appears to be making incorrect decisions about whether to continue processing text or break at certain points. This manifests in one of two ways:

1. Text that should be processed is being skipped
2. Break points that should trigger are being ignored

Additionally, there seems to be an off-by-one error when iterating through construct lists, which could lead to accessing undefined array elements or missing the last item in the list.

### Expected behavior

The parser should correctly identify when to process text content versus when to break at specific code points. All items in construct lists should be properly evaluated without going out of bounds.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is causing some MDX documents to fail parsing or produce incorrect output. Would appreciate any insights into what might be causing this!

---
Repository: /testbed
