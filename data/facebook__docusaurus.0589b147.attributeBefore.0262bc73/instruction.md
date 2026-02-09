# Bug Report

### Describe the bug

I'm encountering an issue with MDX tag parsing where attributes with certain characters are not being recognized properly. It seems like valid attribute names that start with specific characters are being rejected even though they should be allowed according to the MDX specification.

### Reproduction

```mdx
<Component attribute={value} />
```

When using attributes with names that start with certain valid characters, the parser throws an error saying it expected "a character that can start an attribute name" even though the character should be valid.

This appears to be happening specifically with attribute names in JSX-like tags within MDX content. The parser seems to be incorrectly validating which characters can start an attribute name.

### Expected behavior

The parser should accept all valid attribute name starting characters as defined by the MDX/JSX specification. Attribute names should be parsed correctly without throwing unexpected errors about invalid starting characters.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
