# Bug Report

### Describe the bug

I'm experiencing an issue with MDX link parsing where the URL destination is being assigned to the wrong node in the AST. When processing markdown links with resource destinations, the URL appears to be set on an incorrect parent node instead of the actual link node.

### Reproduction

```markdown
[Link text](https://example.com)
```

When parsing the above markdown link, the `url` property gets assigned to the wrong element in the stack. It seems like the parser is looking at `stack.length - 2` instead of `stack.length - 1`, causing the URL to be set on a parent node rather than the link node itself.

### Expected behavior

The URL should be correctly assigned to the link node (the current top of the stack), not to its parent. The link should parse correctly with the URL attached to the proper AST node.

### Additional context

This appears to be happening in the `onexitresourcedestinationstring` function during MDX compilation. The link text parses fine, but the destination URL ends up in the wrong place in the AST structure.

---
Repository: /testbed
