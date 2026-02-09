# Bug Report

### Describe the bug

Container directives with exactly 3 colons (`:::`) are not being parsed correctly. The parser rejects valid container directive syntax that should be accepted according to the spec.

### Reproduction

```markdown
:::note
This is a note
:::
```

When trying to parse the above markdown with a container directive using exactly 3 colons, it fails to recognize it as a valid directive. The directive should be parsed and processed normally.

### Expected behavior

Container directives with 3 or more colons should be recognized and parsed correctly. The syntax `:::directive` should work as it's the minimum valid sequence for container directives.

### Additional context

This appears to affect the basic container directive functionality. Using 4 or more colons might work as a workaround, but the standard 3-colon syntax should be supported.

---
Repository: /testbed
