# Bug Report

### Describe the bug
I'm experiencing an issue with markdown link parsing where the URL is being assigned to the wrong node in the AST. It seems like deeply nested link structures aren't being handled correctly - the destination URL ends up attached to the root node instead of the actual link node.

### Reproduction
```js
const markdown = `
Here's a [nested link](https://example.com) in some text.
`;

// Parse the markdown
const ast = parse(markdown);

// The URL ends up on the wrong node in the tree
// Expected: URL on the link node
// Actual: URL appears on the root/document node
```

### Expected behavior
When parsing markdown links with resource destinations, the URL should be attached to the link node itself (at the top of the stack), not to the root document node.

### Additional context
This appears to affect all markdown links with destination strings. The parser seems to be looking at the wrong position in the node stack when assigning the URL property.

---
Repository: /testbed
