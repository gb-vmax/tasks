# Bug Report

### Describe the bug

I'm experiencing an issue with MDX document parsing where the container state tracking appears to be broken. When processing nested containers in MDX documents, the parser seems to lose track of the container state, which causes parsing errors or unexpected behavior.

### Reproduction

```js
// MDX content with nested containers
const mdxContent = `
> Blockquote level 1
> > Blockquote level 2
> > Content here
> Back to level 1
`

// Parse the MDX
const result = compile(mdxContent)
```

When parsing documents with nested block-level containers (like nested blockquotes, lists, or other container elements), the parser doesn't properly maintain the container state stack.

### Expected behavior

The parser should correctly track both the construct and its associated container state when continuing through nested containers. Nested structures should parse correctly and maintain proper state throughout the parsing process.

### Additional context

This seems related to how the document continuation logic handles the state stack. The container state information appears to be getting lost during the parsing flow, which breaks proper handling of nested block structures.

---
Repository: /testbed
