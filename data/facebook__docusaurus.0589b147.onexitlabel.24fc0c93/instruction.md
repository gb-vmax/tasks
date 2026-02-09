# Bug Report

### Describe the bug

I'm experiencing an issue with link parsing where the link text/children are not being properly set. When parsing markdown links, the link node ends up with its original children instead of the parsed fragment children.

### Reproduction

```js
const markdown = '[link text](https://example.com)'
const ast = parse(markdown)

// Expected: link node should have children from the parsed label
// Actual: link node children remain unchanged
console.log(ast.children[0].children) // Shows wrong children
```

### Expected behavior

When parsing a markdown link like `[some text](url)`, the link node's children should be populated with the parsed content from the label (the text between the square brackets). Currently it seems like the children are not being updated correctly.

### Additional context

This appears to affect standard markdown links. The link structure is created but the actual link text content isn't being transferred properly from the label fragment to the link node.

---
Repository: /testbed
