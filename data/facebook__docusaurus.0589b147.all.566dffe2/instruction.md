# Bug Report

### Describe the bug

I'm encountering an issue with the `mdast-util-to-string` utility where it seems to be skipping elements when converting markdown AST nodes to strings. The output is missing content that should be included.

### Reproduction

```js
const mdast = {
  type: 'paragraph',
  children: [
    { type: 'text', value: 'Hello' },
    { type: 'text', value: ' ' },
    { type: 'text', value: 'World' }
  ]
};

const result = toString(mdast);
console.log(result); // Expected: "Hello World", but getting incomplete output
```

When processing arrays of child nodes, it appears that the first element is being skipped or the iteration is off by one somehow. This results in incomplete string conversion.

### Expected behavior

All child nodes should be processed and concatenated into the final string output. No elements should be skipped during the conversion.

### System Info
- mdast-util-to-string version: 4.0.0
- Node.js version: Latest

---
Repository: /testbed
