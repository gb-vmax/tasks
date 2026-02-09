# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where the URL destination is not being set correctly on link nodes. When parsing markdown with links like `[text](url)`, the resulting AST node structure seems incorrect.

### Reproduction

```js
const ast = remark.parse('[example link](https://example.com)');
// The link node doesn't have the correct url property set
// Instead it appears to be trying to set 'destination' on the wrong node
```

When parsing markdown links, the URL from the resource destination is not being properly assigned to the link node. It looks like the parser is trying to access the wrong element in the stack when processing the link destination.

### Expected behavior

The link node should have its `url` property correctly set to the destination URL from the markdown. For a link like `[text](https://example.com)`, the resulting node should contain `url: 'https://example.com'`.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
