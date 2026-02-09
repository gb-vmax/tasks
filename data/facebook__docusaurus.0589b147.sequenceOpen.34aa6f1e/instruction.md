# Bug Report

### Describe the bug
Container directives with exactly 3 colons (`:::`) are not being parsed correctly. The parser rejects valid container directive syntax that should be accepted according to the directive specification.

### Reproduction
```markdown
:::note
This is a note
:::
```

When trying to parse this markdown with container directives, the directive is not recognized and fails to parse. The same issue occurs with any container directive using the standard three-colon syntax.

### Expected behavior
Container directives with three colons should be parsed successfully. The syntax `:::name` is the standard way to open a container directive and should be recognized by the parser.

### Additional context
This affects all container directives regardless of the directive name used (note, warning, tip, etc.). The parser seems to require more than 3 colons, but the spec indicates that 3 colons is the minimum valid syntax for container directives.

---
Repository: /testbed
