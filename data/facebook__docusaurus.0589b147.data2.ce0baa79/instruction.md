# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where line breaks in text content are not being handled correctly. After a recent update, it seems like the parser is consuming break characters when it shouldn't, which causes the text flow to behave unexpectedly.

### Reproduction

```mdx
This is some text content.
This should be on a new line.

But the line breaks are not being preserved correctly.
```

When parsing the above MDX content, the line breaks between text segments are being consumed incorrectly, leading to malformed output or unexpected text concatenation.

### Expected behavior

The parser should properly handle line breaks in text content without consuming the break characters prematurely. Text should flow naturally with line breaks preserved as intended in the source MDX.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
