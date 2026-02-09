# Bug Report

### Describe the bug
HTML attributes with quoted values are not being parsed correctly. When an HTML tag has an attribute with a quoted value (like `class="foo"` or `id="bar"`), the parser is rejecting valid HTML that should be accepted.

### Reproduction
```markdown
<div class="container">content</div>
```

Or:

```markdown
<span id="test" data-value="123">text</span>
```

These valid HTML snippets are being treated as invalid and not parsed properly. The issue seems to occur specifically after closing quotes in attribute values.

### Expected behavior
Valid HTML with quoted attribute values should be parsed correctly. Tags like `<div class="foo">` should be recognized as valid HTML and processed accordingly.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
