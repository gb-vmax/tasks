# Bug Report

### Describe the bug

I'm seeing an issue with the `debugger` statement generation in the AST code generator. When generating code for `DebuggerStatement` nodes, there's a problem with how the semicolon is being handled - it appears that the semicolon is always being written regardless of the `semicolon` property value.

### Reproduction

```js
const node = {
  type: 'DebuggerStatement',
  semicolon: false
}

// Generate code from this AST node
// Expected output: "debugger"
// Actual output: "debugger;"
```

The issue is that even when `node.semicolon` is explicitly set to `false`, the semicolon is still being added to the output. This breaks scenarios where you want to generate code without automatic semicolon insertion.

### Expected behavior

When `semicolon` is set to `false` on a `DebuggerStatement` node, the generated code should be `"debugger"` without the trailing semicolon. The semicolon should only be added when the property is not explicitly set to `false`.

### Additional context

This affects code generation for AST transformations where precise control over semicolon placement is needed. The current behavior doesn't respect the `semicolon` property on the node.

---
Repository: /testbed
