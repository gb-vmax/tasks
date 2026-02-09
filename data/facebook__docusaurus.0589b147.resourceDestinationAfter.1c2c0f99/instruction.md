# Bug Report

### Describe the bug

I'm encountering an issue with markdown link parsing where inline links with destinations followed by whitespace or line endings are not being handled correctly. The parser seems to be inverting the logic for when to process whitespace versus when to end the resource parsing.

### Reproduction

```markdown
[link text](https://example.com "title")
```

When parsing markdown links with destinations that have titles (separated by whitespace), the tokenizer appears to be calling the wrong handler. Links that should be recognized as valid are being rejected, or the parser is attempting to process whitespace when it shouldn't.

This affects any markdown content with inline links that include:
- A URL followed by a space and a title
- Links with proper spacing between destination and title attributes

### Expected behavior

The markdown parser should correctly tokenize inline links with destinations followed by whitespace (for titles) or line endings. The `resourceDestinationAfter` function should properly detect when whitespace is present and handle it appropriately, allowing valid markdown links to be parsed correctly.

### System Info
- Using remark@15.0.1
- Affects markdown link tokenization

---
Repository: /testbed
