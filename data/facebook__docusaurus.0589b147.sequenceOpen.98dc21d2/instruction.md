# Bug Report

### Describe the bug

Container directives are not being parsed correctly. When trying to use container directives with the standard three-colon syntax `:::`, they're not being recognized properly.

### Reproduction

```markdown
:::note
This is a container directive
:::
```

The parser fails to recognize this as a valid container directive even though it follows the spec with three colons.

### Expected behavior

Container directives with three colons should be parsed correctly. The syntax `:::name` should create a proper container directive node in the AST.

### Additional context

This seems to affect all container directives regardless of the directive name used. Both built-in and custom directive names fail to parse when using the three-colon syntax.

---
Repository: /testbed
