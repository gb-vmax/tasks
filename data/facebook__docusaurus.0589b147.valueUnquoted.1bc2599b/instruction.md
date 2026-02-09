# Bug Report

### Describe the bug

I'm experiencing an issue with parsing unquoted attribute values in directives. When an unquoted attribute value contains a `>` character, it's being consumed as part of the value instead of being rejected or handled properly. This is causing unexpected parsing behavior.

### Reproduction

```markdown
:directive[text]{attr=value>extra}
```

When parsing the above directive, the `>` character in the unquoted attribute value should not be allowed or should terminate the value, but instead it appears to be consumed as part of the attribute value itself.

### Expected behavior

Unquoted attribute values containing `>` should either:
1. Be rejected (similar to how `<`, `=`, `"`, `'`, and backticks are handled)
2. Cause the attribute value to terminate at that point

The current behavior allows `>` to be part of unquoted attribute values, which seems inconsistent with how other special characters are treated.

### Additional context

This affects directive parsing when users accidentally or intentionally include angle brackets in unquoted attribute values. The parser should handle this consistently with other reserved/special characters.

---
Repository: /testbed
