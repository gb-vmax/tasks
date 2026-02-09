# Bug Report

### Describe the bug

I'm experiencing an issue with markdown heading parsing where headings with `#` characters in the text content are being cut off prematurely. The parser seems to stop processing the heading text when it encounters a `#` symbol within the heading itself.

### Reproduction

```markdown
# This is a heading with # symbol in it
## Another heading with ## multiple # symbols
```

When parsing the above markdown, the headings are not being processed correctly. The text after the `#` character within the heading content is being truncated or ignored.

### Expected behavior

The parser should treat `#` characters within the heading text as regular text content, not as special characters. The entire heading text should be captured, including any `#` symbols that appear after the initial heading marker.

For example:
- `# This is a heading with # symbol in it` should parse the full text "This is a heading with # symbol in it"
- `## Another heading with ## multiple # symbols` should parse the full text "Another heading with ## multiple # symbols"

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
