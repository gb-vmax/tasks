# Bug Report

### Describe the bug

I'm experiencing an issue with inline code parsing in markdown. It seems like backticks are not being handled correctly, especially when there are multiple backticks or escaped characters involved.

### Reproduction

When trying to parse markdown with inline code blocks, the parser is producing unexpected results:

```js
// This markdown string doesn't parse correctly
const markdown = '`code`';

// Also having issues with escaped backticks
const markdown2 = '\\`not code\\`';
```

The inline code detection seems to be inverted - text that should be treated as code isn't being recognized, and text that shouldn't be code is being wrapped in code blocks.

### Expected behavior

- Single backticks should create inline code spans
- Escaped backticks should not trigger code block detection
- The parser should correctly identify the start and end of inline code segments

### System Info
- remark version: 15.0.1
- Node version: Latest

This is breaking our markdown rendering pipeline. Any help would be appreciated!

---
Repository: /testbed
