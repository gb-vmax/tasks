# Bug Report

### Describe the bug

HTML attribute values with quoted strings are not being parsed correctly. When an attribute value is quoted and contains the same quote character as the delimiter, the parser gets stuck in an infinite loop instead of properly closing the attribute value.

### Reproduction

```markdown
<div title="This is a "test" value">content</div>
```

Or with single quotes:

```markdown
<div title='It's a value'>content</div>
```

### Expected behavior

The parser should properly handle the closing quote of the attribute value and move to the next state. Currently it appears to stay in the same state indefinitely when encountering the closing quote marker.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
