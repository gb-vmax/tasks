# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the output appears to have events in the wrong order. After processing, some events that should appear earlier in the sequence are showing up at the end instead.

### Reproduction

```js
const mdx = `
# Heading

Some content here
`;

const result = await compile(mdx);
// Events are processed but appear in unexpected order
// First event is moved to the end of the array
```

### Expected behavior

Events should maintain their original order after postprocessing. The first event in the events array should remain at the beginning, not be moved to the end.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
