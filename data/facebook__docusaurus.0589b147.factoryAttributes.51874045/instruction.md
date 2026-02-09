# Bug Report

### Describe the bug
I'm encountering an issue with directive attribute parsing where certain characters are not being handled correctly. Specifically, when using the pipe character (`|`) in attribute values, the parsing behavior seems incorrect.

### Reproduction
```markdown
:::directive{attribute=value|other}
content
:::
```

When parsing directives with attribute values containing a pipe character, the parser doesn't recognize it properly. The attribute value gets cut off or the directive fails to parse as expected.

### Expected behavior
The pipe character should be allowed in attribute values and parsed correctly. The full attribute value including the pipe should be captured.

### Additional context
This appears to be related to character code validation in the attribute parsing logic. The parser seems to be treating certain valid characters as invalid terminators for attribute values.

---
Repository: /testbed
