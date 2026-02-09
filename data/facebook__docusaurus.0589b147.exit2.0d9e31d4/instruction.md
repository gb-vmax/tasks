# Bug Report

### Describe the bug

I'm experiencing an issue with markdown generation where the state stack is not being properly managed. When processing nested markdown structures, the stack appears to retain elements that should have been removed, causing incorrect output formatting.

### Reproduction

```js
// Process a simple markdown tree with nested elements
const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        { type: 'text', value: 'Hello' }
      ]
    }
  ]
}

const result = toMarkdown(tree)
// Stack state becomes inconsistent after processing
```

When converting markdown trees back to string format, the internal state stack doesn't get cleaned up correctly. This seems to happen particularly with deeply nested structures where multiple enter/exit calls occur.

### Expected behavior

The state stack should be properly balanced - each `enter()` call should have a corresponding stack pop when `exit()` is called. The final state should have an empty or minimal stack after processing is complete.

### System Info
- remark version: 15.0.1
- Node version: Latest

This is causing issues in our documentation pipeline where we're converting AST nodes back to markdown format. The output is sometimes malformed due to what appears to be leftover state from previous operations.

---
Repository: /testbed
