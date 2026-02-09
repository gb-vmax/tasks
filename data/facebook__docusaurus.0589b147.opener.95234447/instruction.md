# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the order of operations in the `opener` function seems to be causing problems with nested markdown structures. When parsing certain markdown documents with complex nesting (like lists within blockquotes or code blocks within lists), the resulting AST doesn't match the expected structure.

### Reproduction

```js
const markdown = `
> - Item 1
>   - Nested item
> - Item 2
`;

const result = remark().parse(markdown);
// The nested structure is malformed
```

Another example that shows the issue:

```js
const markdown = `
1. First item
   \`\`\`js
   code block
   \`\`\`
2. Second item
`;

const ast = remark().parse(markdown);
// Code block node appears in wrong position in the tree
```

### Expected behavior

The parser should correctly build the AST with proper parent-child relationships, regardless of the order in which nodes are entered and callbacks are invoked. The nested items should appear as children of their parent nodes in the correct positions.

### Additional context

This seems to affect any markdown with deep nesting where the context/state needs to be properly established before creating child nodes. The issue is particularly noticeable with lists, blockquotes, and code blocks that are nested within other structures.

---
Repository: /testbed
