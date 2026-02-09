# Bug Report

### Describe the bug

I'm experiencing an issue with the remark processor where it's not correctly dispatching to the right handler functions. When processing markdown nodes, the handler lookup seems to be broken and either calls the wrong handler or falls back to the unknown handler even when a valid handler is registered.

### Reproduction

```js
import {remark} from 'remark'

const processor = remark()
  .use(function() {
    return function(tree) {
      // Try to process a node with a registered handler
      // The handler is not being called correctly
    }
  })

processor.process('# Hello\n\nWorld')
```

When processing markdown with custom handlers registered for specific node types, the handlers are not being invoked correctly. Instead, it seems like the lookup mechanism is checking the wrong object properties.

### Expected behavior

The processor should correctly identify the node type and dispatch to the appropriate registered handler. If a handler is registered for a specific node type (like 'heading', 'paragraph', etc.), it should be called when that node type is encountered.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have broken the entire handler dispatch system. Any markdown processing that relies on custom handlers is affected.

---
Repository: /testbed
