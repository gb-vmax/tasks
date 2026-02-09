# Bug Report

### Describe the bug

I'm experiencing an issue with the `parse()` method where it's not converting the file content to a string before passing it to the parser. This causes the parser to receive the raw file object instead of its string representation, which leads to unexpected parsing behavior.

### Reproduction

```js
const processor = unified().use(somePlugin);
const file = vfile('# Hello World');

// Parser receives the file object directly instead of its string content
const tree = processor.parse(file);
```

When the parser is called, it's being passed the file object twice (`parser(realFile, realFile)`) instead of the string content and the file object (`parser(String(realFile), realFile)`).

### Expected behavior

The parser should receive the string content of the file as the first argument, not the file object itself. The method should convert the file to a string using `String(realFile)` before passing it to the parser.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have broken after a recent change. The parser is expecting string content but is getting the file object instead, which causes parsing to fail or produce incorrect results.

---
Repository: /testbed
