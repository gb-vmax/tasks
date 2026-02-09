# Bug Report

### Describe the bug

I'm encountering an issue with paragraph nodes in the markdown parser. When creating or manipulating paragraph elements, I'm getting unexpected behavior where the children array appears to be immutable and modifications to it fail silently or throw errors.

### Reproduction

```js
// Create a paragraph node
const para = paragraph2();

// Try to add children to the paragraph
para.children.push({
  type: 'text',
  value: 'Hello world'
});

// This fails - children array cannot be modified
```

The paragraph node's children array seems to be frozen/immutable, which prevents adding or modifying child nodes dynamically. This breaks the expected behavior where we should be able to build up the AST by adding children to paragraph nodes.

### Expected behavior

Should be able to modify the children array of paragraph nodes just like other node types. Adding child nodes to paragraphs should work the same way as it does for other container elements.

### Additional context

This seems to affect specifically paragraph nodes - other node types like `strong` still allow children to be added normally. Not sure when this started happening but it's blocking our markdown processing pipeline.

---
Repository: /testbed
