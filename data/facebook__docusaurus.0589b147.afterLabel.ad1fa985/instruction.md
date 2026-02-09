# Bug Report

### Describe the bug

I'm experiencing an issue with directive text parsing where attributes are not being processed correctly. It seems like the parser is skipping attribute blocks when they should be parsed.

### Reproduction

```markdown
:directive[label]{attr="value"}
```

When parsing the above directive text, the attributes block `{attr="value"}` is not being recognized or processed as expected. The directive label works fine, but anything after it in curly braces gets ignored.

### Expected behavior

The parser should attempt to parse the attributes block (the part in curly braces) after the label. The attributes should be extracted and available in the directive node.

### Additional context

This appears to affect only text directives (the inline `:directive` syntax). I haven't tested whether container or leaf directives are affected by the same issue.

- remark-directive version: 3.0.0

---
Repository: /testbed
