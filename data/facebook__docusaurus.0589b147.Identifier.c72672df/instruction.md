# Bug Report

### Describe the bug

I'm encountering an issue with identifier code generation where the `state.write` method is being called with arguments in the wrong order. This causes the generated code to have incorrect output.

### Reproduction

```js
// When processing an Identifier node
const identifierNode = {
  type: 'Identifier',
  name: 'myVariable'
}

// The generator processes this node
GENERATOR.Identifier(identifierNode, state)

// Expected: state.write('myVariable', identifierNode)
// Actual: state.write is called twice with swapped arguments on second call
```

### Expected behavior

The `Identifier` generator should only call `state.write` once with the identifier name as the first argument and the node as the second argument. Currently it appears to be calling `state.write` a second time with the arguments reversed (node first, then name), which produces malformed output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
