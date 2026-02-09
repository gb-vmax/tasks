# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where content is not being processed correctly. It seems like the parser is getting stuck or not properly handling text content in certain cases.

### Reproduction

```js
const markdown = `
This is some text
with multiple lines
that should be parsed
`;

const result = remark.parse(markdown);
// Parser appears to hang or produce unexpected output
```

When trying to parse even simple markdown text with line breaks, the parser doesn't seem to complete properly or produces malformed AST nodes.

### Expected behavior

The markdown parser should correctly process text content across multiple lines and return a proper AST structure with all text nodes linked together.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems like it might be a regression as similar markdown was parsing fine in earlier versions. Any help would be appreciated!

---
Repository: /testbed
