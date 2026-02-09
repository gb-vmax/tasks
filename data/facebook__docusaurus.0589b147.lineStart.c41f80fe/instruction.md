# Bug Report

### Describe the bug

I'm experiencing an issue with parsing markdown code blocks. When I have indented code blocks in my markdown, the parser seems to be incorrectly handling lazy continuation lines, causing code blocks to either be parsed incorrectly or not recognized at all.

### Reproduction

```js
const markdown = `
Some text

    indented code block
    second line of code

More text
`;

// Parse the markdown
const result = remark.parse(markdown);

// The code block is not being recognized correctly
```

### Expected behavior

The indented code block should be properly parsed and recognized as a code block node in the AST. All lines that are part of the indented code block should be included in the code block.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. The parser appears to be checking lazy continuation incorrectly, which affects how code blocks are being tokenized.

---
Repository: /testbed
