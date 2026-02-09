# Bug Report

### Describe the bug

I'm experiencing an issue with document parsing where containers are being exited in the wrong order. When processing nested containers, it seems like the exit callbacks are being called after the stack has already been truncated, which causes the wrong container states to be accessed during cleanup.

### Reproduction

```js
// Create a document with nested containers
const doc = `
> outer quote
> > inner quote
> > more inner content
> back to outer
`;

// Parse the document
const result = parse(doc);
```

When parsing documents with multiple levels of nested block quotes or lists, the container exit logic doesn't properly handle the stack state. The stack gets modified before all exit callbacks complete, leading to incorrect container state references.

### Expected behavior

Container exit callbacks should be called with the correct container state preserved. The stack should only be truncated after all necessary exit operations have completed for containers being closed.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
