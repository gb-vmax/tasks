# Bug Report

### Describe the bug

I'm encountering an issue with the remark compiler where the order of operations in the `opener` function seems to have changed. When creating AST nodes, the `enter` function is now being called with arguments in the wrong order - it's receiving `token` first and then `create(token)`, but it should be the other way around.

This is causing nodes to be entered into the stack incorrectly during markdown parsing.

### Reproduction

```js
// When processing markdown tokens
const processor = remark();
const ast = processor.parse('# Hello world');

// The opener function creates and enters nodes
// But the enter call now has swapped arguments:
// enter.call(this, token, create(token))
// instead of:
// enter.call(this, create(token), token)
```

The issue manifests when parsing any markdown content - the AST structure gets corrupted because nodes are being entered with incorrect parameters.

### Expected behavior

The `enter` function should be called with the created node first, followed by the token:
```js
enter.call(this, create(token), token);
```

This ensures that the AST node is properly added to the stack before any additional processing happens.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
