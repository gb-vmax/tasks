# Bug Report

### Describe the bug

I'm encountering an issue when parsing markdown content with specific encoding options. When I pass both a value and an encoding parameter to the markdown parser, it seems like the encoding isn't being handled correctly and the parser fails or produces unexpected results.

### Reproduction

```js
const markdown = '# Hello World\n\nThis is a test.';
const result = fromMarkdown(markdown, 'utf8', { /* options */ });
// Parser throws an error or produces incorrect output
```

The issue occurs when:
1. Calling the markdown parser with a string value
2. Specifying an encoding (like 'utf8')
3. Passing additional options as the third parameter

### Expected behavior

The parser should correctly process the markdown content with the specified encoding and options. The encoding parameter should be properly handled and passed through the preprocessing pipeline.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have broken recently, as the same code was working in earlier versions. Any help would be appreciated!

---
Repository: /testbed
