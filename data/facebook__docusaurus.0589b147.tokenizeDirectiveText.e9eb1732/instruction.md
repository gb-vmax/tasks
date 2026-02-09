# Bug Report

### Describe the bug

I'm encountering an issue with inline directive parsing where the syntax validation seems to be checking characters in the wrong order. Specifically, when using inline directives with certain character combinations, they're being rejected when they should be valid, or accepted when they should be invalid.

### Reproduction

```markdown
:directive[label]{attributes}
```

When parsing inline directives, the character validation after the directive name appears to be backwards. The parser is checking for `[` when it should check for `:`, and vice versa, causing incorrect parsing behavior.

### Expected behavior

The parser should correctly validate the character sequence following a directive name. Characters should be checked in the proper order to ensure valid directive syntax is accepted and invalid syntax is properly rejected.

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
