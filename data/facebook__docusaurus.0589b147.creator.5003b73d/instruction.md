# Bug Report

### Describe the bug

I'm encountering an issue with the markdown parser where tokenization seems to be broken. When parsing markdown content, the parser appears to be passing incorrect arguments to the tokenizer creation function, causing unexpected behavior or errors.

### Reproduction

```js
const parser = remark.parse();
const result = parser.parse('# Hello World\n\nSome text here.');
```

When attempting to parse markdown content, the tokenizer receives arguments in the wrong order, which breaks the parsing functionality.

### Expected behavior

The parser should correctly tokenize and parse markdown content without errors. The tokenizer should receive the proper arguments in the correct order to function as intended.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
