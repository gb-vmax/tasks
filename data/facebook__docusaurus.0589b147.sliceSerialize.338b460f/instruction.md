# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where text serialization is producing incorrect output. It seems like the order of operations for processing tokens has been changed, causing the serialized text to not match the expected format.

### Reproduction

```js
// When parsing markdown with tabs or special whitespace
const markdown = `
- Item with\ttab
- Another item
`;

const result = parser.parse(markdown);
const serialized = sliceSerialize(result.children[0]);

// The serialized output doesn't match the original text
console.log(serialized); // Output is malformed
```

### Expected behavior

The `sliceSerialize` function should correctly serialize tokens back to their original text representation, preserving whitespace and tab characters as they appeared in the source.

### System Info

- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
