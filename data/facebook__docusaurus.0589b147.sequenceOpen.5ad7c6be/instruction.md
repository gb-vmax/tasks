# Bug Report

### Describe the bug

Container directives with the standard three-colon syntax (`:::`) are not being recognized properly. When trying to use a container directive with exactly three colons, it fails to parse.

### Reproduction

```markdown
:::note
This is a note
:::
```

The above syntax should work for container directives but it's not being parsed correctly. It seems like the parser is expecting more than three colons now.

### Expected behavior

Container directives should work with exactly three colons (the standard syntax). The parser should recognize `:::` as a valid container directive opener and process the content accordingly.

### Additional context

This appears to have started recently. The same markdown syntax was working before. Container directives are a standard feature and the three-colon syntax is widely used in documentation.

---
Repository: /testbed
