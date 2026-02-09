# Bug Report

### Describe the bug

HTML tags with quoted attribute values are not being parsed correctly. When an HTML tag has attributes with quoted values followed by other attributes or the closing `>`, the parser fails to recognize the tag properly.

### Reproduction

```js
// This HTML should be parsed correctly but isn't
const markdown = '<div class="test" id="main">content</div>'

// Also fails with single quotes
const markdown2 = "<div class='test' id='main'>content</div>"

// Self-closing tags are also affected
const markdown3 = '<img src="image.jpg" alt="description" />'
```

### Expected behavior

HTML tags with quoted attribute values should be recognized and parsed correctly, regardless of whether they:
- Have multiple attributes
- Use single or double quotes
- Are self-closing tags (ending with `/>`)
- Have whitespace after the quoted value

The parser should handle these common HTML patterns that are valid in markdown.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
