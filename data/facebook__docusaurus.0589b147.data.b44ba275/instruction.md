# Bug Report

### Describe the bug

I'm encountering an issue with inline code parsing in markdown. When using backticks for inline code that contains certain characters, the parser seems to get stuck or produce incorrect output.

### Reproduction

```js
const markdown = '`code with null character\0 inside`';
// Parser fails to properly tokenize this

const markdown2 = '`some code` `more code`';
// Adjacent inline code blocks also behave unexpectedly
```

The issue appears when:
1. Inline code contains null characters or special byte values
2. Multiple inline code segments are used in sequence

### Expected behavior

The parser should correctly handle inline code blocks regardless of their content, including null characters and other special values. Each backtick-delimited section should be properly tokenized as separate code text segments.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started recently, possibly after some changes to the tokenization logic. The inline code parsing doesn't complete properly in these cases.

---
Repository: /testbed
