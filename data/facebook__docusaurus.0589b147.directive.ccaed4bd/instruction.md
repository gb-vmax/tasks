# Bug Report

### Describe the bug

After a recent update, directive syntax parsing seems broken. Container and leaf directives (like `:::note` blocks) are no longer being recognized in markdown files, while inline text directives (like `:icon:`) still work fine.

### Reproduction

```markdown
:::note
This is a container directive
:::

::leaf-directive

:text-directive:
```

When parsing the above markdown:
- Text directives (`:text-directive:`) are processed correctly
- Container directives (`:::note`) are not recognized
- Leaf directives (`::leaf-directive`) are not recognized

### Expected behavior

All three types of directives should be parsed and processed correctly. Both container and leaf block directives should be recognized alongside text directives.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
