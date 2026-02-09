# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where the parser hangs or behaves unexpectedly when processing certain content that ends with a null character. The parser seems to get stuck and doesn't properly terminate.

### Reproduction

```js
const processor = remark();

// This causes the parser to hang/not terminate properly
const content = "Some markdown content\n";
const result = processor.parse(content);
```

When parsing markdown that has specific flow constructs followed by EOF, the parser doesn't return control properly and appears to continue processing indefinitely or returns undefined instead of completing the parse.

### Expected behavior

The parser should properly handle the end of input and return the parsed result. When encountering a null character (EOF), it should cleanly exit the parsing flow and return the AST.

### System Info
- remark version: 15.0.1
- Node version: Latest LTS

---
Repository: /testbed
