# Bug Report

### Describe the bug

I'm encountering an issue with the MDX parser where node positions are being incorrectly set during parsing. It appears that the `startNode` method is modifying the parser's `end` position before creating a new node, which causes the node to be initialized with `this.end` instead of `this.start`.

### Reproduction

When parsing MDX content, nodes created via `startNode()` are getting initialized with incorrect position values. The parser's internal state is being mutated before the node is created, leading to nodes that have their start position set to the end position.

```js
// Example MDX content that triggers the issue
const mdxContent = `
# Hello World

Some content here
`;

// Parse the content - nodes will have incorrect position tracking
const result = compile(mdxContent);
```

### Expected behavior

The `startNode` method should create a new node with the current `start` position without modifying the parser's `end` position. Nodes should accurately track their starting position in the source text for proper source mapping and error reporting.

### Additional context

This seems to affect source map generation and could potentially break tooling that relies on accurate position information from the AST. The node's starting position should reflect where it actually begins in the source, not where it ends.

---
Repository: /testbed
