# Bug Report

### Describe the bug

Link references in markdown are not being parsed correctly. When using reference-style links, the parser seems to be checking the wrong condition for inactive label starts, causing valid link references to be rejected.

### Reproduction

```markdown
[link text][ref]

[ref]: https://example.com
```

When parsing this markdown, the link reference is not being recognized properly. The parser appears to be inverting the logic for checking whether a label start is inactive, which causes it to reject valid references.

### Expected behavior

The markdown should parse correctly and create a proper link element. Reference-style links should work as they did in previous versions.

### Additional context

This seems to affect all reference-style links where the label start is active. The issue is in the label end tokenization logic where it checks the `_inactive` property.

---
Repository: /testbed
