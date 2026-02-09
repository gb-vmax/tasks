# Bug Report

### Describe the bug
I'm experiencing an issue with image and link URL handling in MDX files. When using images or links with destination URLs, the URL is not being properly assigned to the node. It seems like the URL is being set on the wrong property or the wrong node in the stack.

### Reproduction
```mdx
![Alt text](https://example.com/image.png)

[Link text](https://example.com/page)
```

When parsing MDX content with images or links that have resource destination strings, the URL doesn't appear in the expected location in the resulting AST. The `url` property on the node is undefined or missing, even though the destination string is clearly present in the source.

### Expected behavior
The parser should correctly extract the URL from the resource destination string and assign it to the appropriate node property. Images and links should have their destination URLs accessible in the AST for further processing.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to have started happening recently. The URL extraction logic seems to be affected but I'm not sure what changed.

---
Repository: /testbed
