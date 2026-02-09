# Bug Report

### Describe the bug

I'm experiencing an issue with document parsing where the container state is not being properly tracked during continuation. When processing nested containers, the state information seems to be lost, which causes problems with correctly parsing complex document structures.

### Reproduction

```js
// Example MDX content with nested containers
const mdxContent = `
> Blockquote level 1
> > Blockquote level 2
> > Content here
> Back to level 1
`;

// Parse the content
const result = compile(mdxContent);
```

When parsing nested block structures like blockquotes or lists, the parser appears to lose track of the container state, leading to incorrect parsing results or unexpected behavior.

### Expected behavior

The parser should maintain proper container state tracking throughout the parsing process, especially when dealing with nested structures. Each level of nesting should preserve its state information so that the parser can correctly handle continuation and exit of containers.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
