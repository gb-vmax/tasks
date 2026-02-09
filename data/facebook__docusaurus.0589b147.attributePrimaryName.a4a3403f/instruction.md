# Bug Report

### Describe the bug

I'm encountering an issue with MDX attribute parsing where attribute names starting with certain characters are not being recognized correctly. It seems like the parser is rejecting valid attribute names that should be allowed according to JSX specifications.

### Reproduction

```mdx
<Component attribute="value" />
```

When trying to use attributes with specific character codes (particularly at boundary values), the parser crashes or fails to properly recognize the attribute name. This affects attributes that start with valid JSX identifier characters.

### Expected behavior

The parser should accept all valid JSX attribute name characters including letters, digits, `$`, and `_` at the start of attribute names. Attributes with character codes that are valid JSX identifiers should be parsed without errors.

### Additional context

This appears to be related to how the parser validates character codes in attribute names. The issue manifests when processing certain edge case characters that should be valid according to JSX naming rules but are being incorrectly filtered out during parsing.

---
Repository: /testbed
