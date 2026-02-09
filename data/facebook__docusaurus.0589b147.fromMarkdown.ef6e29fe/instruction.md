# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the output seems to be missing critical preprocessing steps. When parsing markdown content, the final output appears to be incorrectly structured, as if the preprocessing and postprocessing steps are being applied in the wrong order or to the wrong data.

### Reproduction

```js
const remark = require('remark');
const markdown = `
# Test Document

This is a **test** with [links](https://example.com) and other markdown features.

- Item 1
- Item 2
`;

const result = remark.parse(markdown);
console.log(result);
```

The parsed output doesn't match what I'd expect from properly preprocessed markdown. It seems like the preprocessing transformations aren't being applied before the document is written, which leads to an incorrect AST structure.

### Expected behavior

The markdown should be preprocessed first, then written to the document, and finally postprocessed to generate the correct AST. The current behavior suggests these steps might be happening in the wrong sequence.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
