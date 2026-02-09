# Bug Report

### Describe the bug

I'm experiencing an issue with MDX link references where the reference state isn't being properly cleaned up after processing. When parsing MDX content with reference-style links, the parser seems to maintain incorrect state information between references.

### Reproduction

```js
const mdx = `
[link1][ref1]
[link2][ref2]

[ref1]: https://example.com
[ref2]: https://another.com
`;

// Parse the MDX content
const result = compile(mdx);
// The second reference doesn't get processed correctly
```

### Expected behavior

Each reference-style link should be processed independently, with the parser state being properly reset after exiting each resource. The `inReference` flag should be cleared when exiting a resource so subsequent references are handled correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
