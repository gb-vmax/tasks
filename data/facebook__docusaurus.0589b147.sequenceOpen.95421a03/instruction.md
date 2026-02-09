# Bug Report

### Describe the bug

Container directives with exactly 3 colons (`::: directive`) are not being parsed correctly. The parser rejects valid container directive syntax that should be accepted according to the spec.

### Reproduction

```markdown
::: note
This is a container directive with 3 colons
:::
```

When trying to parse this markdown with remark-directive, the container directive is not recognized and fails to parse. The directive should be valid with exactly 3 colons, but it seems like the minimum requirement check is off by one.

### Expected behavior

Container directives should work with 3 or more colons. The example above with `:::` should be parsed as a valid container directive.

### Additional context

This affects all container directives - note, warning, tip, etc. The issue appears to be in the sequence validation logic where it's checking the minimum number of colons required.

---
Repository: /testbed
