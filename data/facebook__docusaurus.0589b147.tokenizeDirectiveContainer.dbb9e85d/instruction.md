# Bug Report

### Describe the bug

Container directives with exactly 3 colons are not being parsed correctly. When I use `:::` to create a container directive, it's being rejected instead of recognized as valid syntax.

### Reproduction

```markdown
:::note
This should be a valid container directive
:::
```

The parser is treating this as invalid even though triple colons should be the minimum valid sequence for container directives according to the directive syntax specification.

### Expected behavior

Container directives with exactly 3 colons should be parsed successfully. Both the opening `:::` and closing `:::` sequences should be recognized as valid delimiters.

Currently it seems like the parser requires MORE than 3 colons, but the spec indicates that 3 should be the minimum.

### Additional context

This affects any container directive using the standard `:::` syntax. Workaround is to use 4+ colons (e.g., `::::`) but this shouldn't be necessary.

---
Repository: /testbed
