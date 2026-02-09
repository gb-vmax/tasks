# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing where the label state doesn't exit properly. When processing directives with labels (like `:directive[label text]`), the parser seems to get stuck or behaves unexpectedly after encountering the closing bracket.

### Reproduction

```js
const directive = ':myDirective[some label text]'
// Parse the directive
// The stringType state is never properly exited
// This causes issues with subsequent parsing or state management
```

When parsing directives with labels, the internal state machine doesn't clean up correctly after processing the label content. This affects how the parser handles the rest of the document.

### Expected behavior

The parser should properly exit all state types when finishing label parsing. After consuming the closing brace `]`, both the string content state and the overall label type state should be exited in the correct order.

### Additional context

This appears to affect any directive that uses the label syntax with square brackets. The issue manifests when the closing bracket is encountered - the state transitions don't complete as expected.

---
Repository: /testbed
