# Bug Report

### Describe the bug

I'm encountering an issue with the remark parser where it seems to be calling the wrong handler functions when processing markdown nodes. The parser appears to be using `unknown` handlers when it should be using registered handlers, and vice versa.

### Reproduction

```js
const processor = remark();

// Register a custom handler for a specific node type
processor.use(function() {
  this.Compiler = function(tree) {
    // Handler should be called for registered node types
    // but unknown handler is being invoked instead
  }
});

const result = processor.processSync('# Hello World');
// Wrong handler is being executed
```

### Expected behavior

When a handler is registered for a specific node type, that handler should be called when processing nodes of that type. The `unknown` handler should only be invoked for unregistered node types.

Currently it seems like the logic is inverted - registered handlers are being treated as unknown and unknown types are being treated as registered.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
