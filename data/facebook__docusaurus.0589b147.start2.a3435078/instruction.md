# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where text content is not being processed correctly. It seems like the parser is incorrectly handling the decision between text and non-text content, causing content to be skipped or processed in the wrong order.

### Reproduction

```mdx
# Hello World

This is some text content that should be parsed normally.

More text here.
```

When parsing this MDX content, the text sections are not being handled as expected. The parser appears to be making incorrect decisions about whether content should be treated as text or non-text constructs.

### Expected behavior

The parser should correctly identify and process text content, calling the appropriate handlers based on whether the code point is at a break or not. Text content should flow normally and be rendered properly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently. The text parsing logic might have been inadvertently changed.

---
Repository: /testbed
