# Bug Report

### Describe the bug

I'm encountering an issue with text extraction from markdown AST nodes where the output appears to be missing the first element when processing arrays of nodes. The extracted text seems to be shifted or incomplete.

### Reproduction

```js
// When processing an array of markdown nodes
const nodes = [
  { type: 'text', value: 'First' },
  { type: 'text', value: 'Second' },
  { type: 'text', value: 'Third' }
];

// Expected output: "FirstSecondThird"
// Actual output: appears to be missing "First"
```

### Expected behavior

When extracting text from a collection of markdown nodes, all elements should be included in the final output in the correct order. The first element should not be skipped or lost during processing.

### Additional context

This seems to affect any markdown structure with multiple child nodes. The first piece of content is consistently missing from the extracted text output.

---
Repository: /testbed
