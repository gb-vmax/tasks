# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing where headings that contain certain characters are not being processed correctly. The parser seems to get stuck in an infinite loop or doesn't properly exit when it encounters specific character sequences.

### Reproduction

```js
// Parsing ATX headings with hash symbols in the content
const markdown = '### Heading with # symbol'

// The parser doesn't handle this correctly and may loop indefinitely
```

When trying to parse markdown headings that contain `#` characters within the heading text itself, the parser behaves unexpectedly. It appears the tokenizer is not properly handling the exit condition.

### Expected behavior

The parser should correctly process ATX headings that contain `#` symbols or other special characters in the heading text, and should properly exit the tokenization process without getting stuck.

### System Info
- remark version: 15.0.1
- Node.js version: Latest

---
Repository: /testbed
