# Bug Report

### Describe the bug

When parsing HTML tags in markdown with quoted attribute values, the parser is not working correctly. It seems like quoted attributes (using `"` or `'`) are not being properly recognized and parsed.

### Reproduction

```markdown
<div class="example">content</div>
<span id='test'>text</span>
```

When processing markdown that contains HTML tags with quoted attribute values, the parser doesn't handle them as expected. The attribute values enclosed in quotes should be parsed correctly but they're being rejected or mishandled.

### Expected behavior

HTML tags with quoted attribute values should be parsed correctly. Both single and double quotes should work for wrapping attribute values like:
- `<div class="test">`
- `<span id='example'>`

The parser should properly recognize the opening quote, consume the attribute value content, and then match the closing quote.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
