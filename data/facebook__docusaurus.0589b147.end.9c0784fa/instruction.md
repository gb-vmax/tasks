# Bug Report

### Describe the bug

HTML tags in markdown text are not being parsed correctly. When using inline HTML elements, the closing `>` character is not being recognized properly, causing the parser to fail or produce unexpected output.

### Reproduction

```js
const markdown = `This is <span>inline HTML</span> text`;
const result = remark.parse(markdown);
// Parser fails to recognize the closing > of HTML tags
```

Also happens with self-closing tags:
```js
const markdown = `Line break here<br/>and continue`;
// The > character is not handled correctly
```

### Expected behavior

The parser should correctly identify and process the closing `>` character of HTML tags, allowing inline HTML to be parsed as valid markdown content.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
