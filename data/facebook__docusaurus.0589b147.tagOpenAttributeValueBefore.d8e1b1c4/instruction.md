# Bug Report

### Describe the bug

HTML tags with attributes are not being parsed correctly in markdown content. When an HTML tag contains an attribute with an equals sign (like `class="something"`), the parser rejects it as invalid.

### Reproduction

```js
const markdown = '<div class="container">content</div>';
// Parser throws error or fails to recognize the tag
```

Another example:
```markdown
<span id="test">Hello</span>
```

The parser should recognize these as valid HTML tags but instead treats them as plain text or fails to parse them.

### Expected behavior

HTML tags with attributes should be parsed correctly. Standard HTML attribute syntax like `attribute="value"` should be recognized as valid.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
