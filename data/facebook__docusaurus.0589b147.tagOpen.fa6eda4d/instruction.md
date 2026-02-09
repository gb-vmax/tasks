# Bug Report

### Describe the bug

HTML tags in markdown are not being parsed correctly. It seems like certain valid HTML tags are being rejected or not recognized properly during tokenization.

### Reproduction

```js
const markdown = `
<div>content</div>
<span>text</span>
<custom-element>data</custom-element>
`;

// Parse the markdown
const result = remark().parse(markdown);
```

When parsing markdown with HTML tags, some tags that should be valid are not being recognized. This appears to affect tags with alphanumeric characters in their names.

### Expected behavior

All valid HTML tags should be properly tokenized and parsed. Tags like `<div>`, `<span>`, and custom elements should all be recognized as valid HTML within the markdown content.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
