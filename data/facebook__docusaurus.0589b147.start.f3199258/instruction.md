# Bug Report

### Describe the bug
I'm experiencing an issue with blank line tokenization in the markdown parser. When processing markdown content with leading spaces before blank lines, the parser appears to enter an infinite loop or behaves incorrectly.

### Reproduction
```js
const markdown = `
Some text

    

More text
`;

// Parser hangs or produces unexpected output when processing
// blank lines that have leading whitespace
```

### Expected behavior
The parser should correctly handle blank lines regardless of whether they have leading whitespace or not. Blank lines with spaces should be tokenized the same way as completely empty lines.

### System Info
- remark-gfm version: 4.0.0
- Browser: N/A (Node.js environment)

### Additional context
This seems to affect parsing of code blocks and other structures that rely on blank line detection. The issue appears to be related to how the tokenizer handles the `markdownSpace` check for blank lines.

---
Repository: /testbed
