# Bug Report

### Describe the bug

HTML closing tags with alphanumeric characters are not being parsed correctly. After a recent change, closing tags that contain letters or numbers (like `</div>`, `</h1>`, `</span>`) are not being recognized properly.

### Reproduction

```markdown
<div>Some content</div>
```

When parsing the above markdown with HTML, the closing tag `</div>` is not being processed correctly. The parser seems to stop recognizing valid closing tag names.

This also affects other tags:
```markdown
<h1>Header</h1>
<p>Paragraph</p>
<span>Text</span>
```

None of the closing tags are working as expected.

### Expected behavior

The parser should correctly recognize and process HTML closing tags that contain alphanumeric characters. Tags like `</div>`, `</h1>`, `</p>`, etc. should all be properly parsed.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
