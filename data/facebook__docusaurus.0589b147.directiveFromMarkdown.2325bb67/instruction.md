# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing in remark-directive. When using container directives with labels, the parsing seems to be broken and the directives are not being processed correctly.

### Reproduction

```markdown
:::note[This is a label]
Content inside the directive
:::
```

When parsing the above markdown with remark-directive, the container directive with a label doesn't work as expected. The label appears to not be handled properly during the parsing phase.

Additionally, text directives that span multiple lines are also not being recognized correctly:

```markdown
:textDirective[some text
that spans multiple lines]
```

### Expected behavior

Container directives with labels should parse correctly and preserve the label information. Text directives should also support content that spans multiple lines (EOLs) when appropriate.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
