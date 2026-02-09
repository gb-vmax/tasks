# Bug Report

### Describe the bug

I'm experiencing a stack overflow error when using conditional expressions in my code. The build process crashes with a "Maximum call stack size exceeded" error, but only when processing certain files that contain ternary operators.

### Reproduction

```js
// This causes the build to crash
const result = condition ? valueA : valueB;

// Also happens with nested conditionals
const nested = a ? (b ? c : d) : e;
```

The error occurs during the tree-shaking/bundling phase. It seems to happen specifically when the bundler tries to process and optimize conditional expressions.

### Expected behavior

The code should build successfully without crashing. Conditional expressions should be processed normally during the bundling phase.

### System Info
- Rollup version: latest
- Node version: 18.x

The build was working fine before, but started failing recently. I suspect it might be related to how annotations are being removed from the AST nodes.

---
Repository: /testbed
