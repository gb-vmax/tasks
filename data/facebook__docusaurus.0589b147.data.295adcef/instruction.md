# Bug Report

### Describe the bug

I'm encountering an issue with markdown heading parsing where headings containing `#` characters in the text are being incorrectly truncated. The parser seems to be treating any `#` symbol within the heading content as a potential terminator, even when it's part of the actual heading text.

### Reproduction

```markdown
# This is a heading with # symbol inside
## Another heading with #hashtag content
### Heading with C# programming language
```

When parsing these headings, the text after the internal `#` character gets cut off or the heading is not recognized properly.

For example:
- `# This is a heading with # symbol inside` might only parse as `# This is a heading with `
- `### Heading with C# programming language` could be truncated at `C`

### Expected behavior

Headings should be able to contain `#` characters in their text content without being prematurely terminated. The parser should only treat `#` as a heading terminator when it's followed by appropriate whitespace or line ending, not when it's part of the heading content itself.

The full heading text including any `#` symbols should be preserved and parsed correctly.

### System Info
- Using remark@15.0.1
- Affects ATX-style headings (those starting with `#` symbols)

---
Repository: /testbed
