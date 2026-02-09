# Bug Report

### Describe the bug

I'm experiencing an issue with text extraction from markdown AST nodes. When processing nodes with multiple children, the extracted text appears to be missing the first child's content entirely.

### Reproduction

```js
const ast = {
  type: 'paragraph',
  children: [
    { type: 'text', value: 'First' },
    { type: 'text', value: 'Second' },
    { type: 'text', value: 'Third' }
  ]
};

const result = toString(ast);
console.log(result); // Expected: "FirstSecondThird"
                     // Actual: "SecondThird"
```

The first element in any collection of child nodes seems to be skipped during processing.

### Expected behavior

All child nodes should be processed and their text content should be included in the output string. The first child should not be omitted.

### Additional context

This seems to affect any markdown node with multiple children - paragraphs, lists, etc. Single-child nodes work fine, but as soon as there are 2+ children, the first one gets dropped.

---
Repository: /testbed
