# Bug Report

### Describe the bug

I'm experiencing an issue with the remark parser where it's not properly handling unknown node types. When the parser encounters a node type that doesn't have a registered handler, it seems to be doing the opposite of what it should - calling the handler when it shouldn't and not calling it when it should.

### Reproduction

```js
const processor = remark();

// Register a custom handler for a specific node type
processor.use(function() {
  this.Compiler = function(tree) {
    // Process tree with custom handlers
  }
});

// When processing markdown with unknown node types,
// the parser behavior is inverted - unknown handlers
// are called when they shouldn't be, and vice versa
const result = processor.processSync('# Some markdown');
```

### Expected behavior

When a node type has a registered handler, that handler should be called. When a node type doesn't have a registered handler, the `unknown` fallback handler should be called instead. Currently this logic appears to be reversed.

### System Info

- remark version: 15.0.1
- Node.js version: Latest

---
Repository: /testbed
