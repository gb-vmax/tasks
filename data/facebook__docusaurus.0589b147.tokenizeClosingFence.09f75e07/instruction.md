# Bug Report

### Describe the bug

Container directives with closing fences that have the same number of colons as the opening fence are not being parsed correctly. The parser seems to reject valid closing fences when they should be accepted.

### Reproduction

```markdown
:::note
Some content here
:::
```

The above should be a valid container directive, but the closing fence `:::` (3 colons) is not being recognized when the opening fence also has 3 colons. It appears the parser is requiring the closing fence to have MORE colons than the opening fence, rather than an equal or greater number.

### Expected behavior

A container directive should close properly when the closing fence has the same number of colons as the opening fence. According to the directive syntax spec, a closing fence needs at least as many markers as the opening fence, not strictly more.

For example:
- `:::note` opened with 3 colons should close with `:::` (3 colons) ✓
- `::::note` opened with 4 colons should close with `::::` (4 colons) or more ✓

Currently only the second case with MORE colons seems to work.

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
