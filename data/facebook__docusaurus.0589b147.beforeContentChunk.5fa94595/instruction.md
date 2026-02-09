# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX where the parser seems to be entering the `codeFlowValue` state at the wrong time. This is causing problems with how code content is being tokenized.

### Reproduction

```mdx
```js
console.log('test');
```
```

When parsing this fenced code block, the tokenizer appears to be handling the content chunks incorrectly. The `codeFlowValue` state is being entered before the content is actually processed, which disrupts the normal flow of tokenization.

### Expected behavior

The parser should:
1. Check if we're at a line ending
2. Process the content chunk
3. Enter the `codeFlowValue` state in the correct order

Currently it seems like the order of operations is wrong, causing the tokenizer to enter states prematurely.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

Has anyone else run into this? It's affecting how code blocks are being parsed in my MDX files.

---
Repository: /testbed
