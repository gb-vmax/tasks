# Bug Report

### Describe the bug
When parsing markdown definitions, the label parsing is not working correctly. The definition syntax `[label]: url "title"` is not being recognized properly, causing the parser to fail or produce incorrect output.

### Reproduction
```markdown
[foo]: /url "title"

This is a reference to [foo].
```

The definition is not being parsed correctly, and references to the label don't resolve as expected.

### Expected behavior
The definition should be properly parsed and the reference `[foo]` should link to `/url` with title "title".

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
