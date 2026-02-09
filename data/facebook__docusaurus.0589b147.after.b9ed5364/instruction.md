# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where links with defined labels are not being processed correctly. When I have a reference-style link with a label that's already defined, the parser seems to be handling the fallback logic incorrectly.

### Reproduction

```markdown
[link text][label]

[label]: https://example.com
```

When parsing this markdown, the link is not being recognized properly even though the label is clearly defined. It seems like the parser is taking the wrong code path when deciding whether to accept or reject the link syntax.

### Expected behavior

The parser should correctly identify that the label is defined and process the reference-style link accordingly. Links with defined labels should be parsed successfully, while links without defined labels should fall back to the appropriate alternative handling.

### Additional context

This appears to affect both resource-style links (with parentheses) and reference-style links (with square brackets). The issue manifests when the label has already been defined earlier in the document - the parser's decision logic for handling these cases seems reversed.

---
Repository: /testbed
