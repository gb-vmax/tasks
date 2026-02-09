# Bug Report

### Describe the bug

HTML text tokenization is broken - the parser fails to process inline HTML elements. When trying to parse markdown content that contains inline HTML tags, the parsing seems to hang or produce no output.

### Reproduction

```js
const markdown = `This is some text with <span>inline HTML</span> content.`;

// Try to parse the markdown
const result = remark.parse(markdown);
// Parser appears to hang or fail silently
```

Also happens with other inline HTML elements:

```js
const markdown = `Text with <strong>bold HTML</strong> here.`;
// Same issue - parsing doesn't complete
```

### Expected behavior

The parser should successfully tokenize and parse markdown content containing inline HTML elements. The HTML text should be properly recognized and included in the AST.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
