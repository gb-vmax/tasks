# Bug Report

### Describe the bug

I'm encountering an issue with directive attribute parsing where invalid syntax is being accepted when it shouldn't be. Specifically, directives with malformed closing braces are not being rejected properly.

### Reproduction

```markdown
:directive{key="value"
```

The parser accepts this directive even though it's missing the closing `}`. This should fail parsing but instead it's treated as valid.

Also noticed similar behavior with other malformed attribute blocks:

```markdown
:directive{key="value" extra-text-here
```

This also gets parsed without errors when it should be rejected.

### Expected behavior

The parser should reject directives that don't have proper closing braces for attribute blocks. Any directive with an unclosed `{` or invalid characters after the attributes should fail to parse correctly.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This seems like a regression as I'm pretty sure this used to work correctly before. The parser is being too lenient with malformed input.

---
Repository: /testbed
