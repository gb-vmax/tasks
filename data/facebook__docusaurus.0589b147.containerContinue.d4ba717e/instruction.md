# Bug Report

### Describe the bug

I'm experiencing issues with MDX document parsing where nested container structures are not being handled correctly. The parser seems to be losing track of the proper container state when processing continued containers.

### Reproduction

```js
// MDX content with nested containers
const mdxContent = `
> Quote block
> 
> Nested content
> - List item
> - Another item
`;

// Parse the content
const result = await compile(mdxContent);
```

When parsing MDX documents with nested block-level containers (like blockquotes containing lists, or nested blockquotes), the container state appears to be getting mixed up. This causes the parser to incorrectly associate container states with their constructs.

### Expected behavior

The parser should maintain the correct relationship between container constructs and their states throughout the parsing process, especially when handling continuation of nested containers.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

Has anyone else encountered this? It seems to affect documents with any kind of nested block-level structures.

---
Repository: /testbed
