# Bug Report

### Describe the bug

I'm experiencing an issue with container directives that have labels. When parsing markdown with container directives, the label exit handler seems to be broken and the parser doesn't properly close the label node.

### Reproduction

```markdown
:::note[This is a label]
Some content here
:::
```

When this gets parsed, the label node structure appears to be malformed. The exit handler for the container label isn't working as expected, which causes the AST to be incomplete or incorrectly structured.

### Expected behavior

The container directive with a label should be parsed correctly, with the label node properly opened and closed in the AST. The `exitContainerLabel` function should properly exit the label token when called.

### Additional context

This seems to affect any container directive that uses the label syntax (the part in square brackets). Container directives without labels appear to work fine.

---
Repository: /testbed
