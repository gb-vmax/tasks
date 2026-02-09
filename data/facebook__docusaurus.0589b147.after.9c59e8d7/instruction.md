# Bug Report

### Describe the bug

Setext headings (underlined headings using `===` or `---`) are not being parsed correctly. The markdown parser seems to reject valid setext heading syntax that should be accepted.

### Reproduction

```js
const markdown = `
Heading
===

Another heading
---
`;

// Parser fails to recognize these as valid setext headings
const result = remark.parse(markdown);
```

When trying to parse standard setext-style headings, they are being treated as invalid or not recognized at all. This affects both `===` (h1) and `---` (h2) style underlines.

### Expected behavior

Setext headings should be properly recognized and parsed into heading nodes. The underline syntax is a standard markdown feature and should work as documented.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
