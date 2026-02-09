# Bug Report

### Describe the bug
I'm experiencing an issue with ATX heading parsing where the hash symbol (`#`) is not being handled correctly within heading text. When a heading contains a `#` character in its content, the parser seems to treat it incorrectly, causing the heading text to be truncated or parsed improperly.

### Reproduction
```markdown
# Heading with # symbol inside
## Another heading with ## multiple hashes
### Testing #hashtag support
```

When parsing these headings, the content after the `#` symbol within the heading text is not being processed as expected. The parser appears to be exiting prematurely when encountering hash symbols that are part of the actual heading content rather than the heading syntax itself.

### Expected behavior
The parser should correctly distinguish between:
1. Hash symbols that define the heading level (at the start)
2. Hash symbols that are part of the heading text content

Headings containing `#` characters within their text should be parsed completely, with all content preserved.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have broken recently. Any heading with a hash symbol in the text is now being cut off incorrectly.

---
Repository: /testbed
