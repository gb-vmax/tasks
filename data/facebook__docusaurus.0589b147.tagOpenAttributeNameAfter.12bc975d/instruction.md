# Bug Report

### Describe the bug
HTML attributes with equal signs are not being parsed correctly in markdown. When an HTML tag has an attribute with an `=` sign, the parser seems to get stuck in an infinite loop or doesn't properly transition to parsing the attribute value.

### Reproduction
```markdown
<div class="test">content</div>
<img src="image.png" alt="description">
<a href="https://example.com">link</a>
```

When parsing HTML tags with attributes that have values (using the `=` sign), the parser doesn't correctly move to the attribute value parsing state. This affects any inline HTML in markdown documents.

### Expected behavior
HTML tags with attributes should be parsed correctly, with the parser properly transitioning from the attribute name to the attribute value when it encounters an `=` sign.

### System Info
- remark version: 15.0.1
- Node version: latest

---
Repository: /testbed
