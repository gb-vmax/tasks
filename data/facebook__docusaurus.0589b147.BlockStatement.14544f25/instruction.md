# Bug Report

### Describe the bug

When using MDX with code blocks that contain multiple statements, the first statement in the block is not being rendered in the output. Only statements after the first one appear in the generated code.

### Reproduction

```mdx
export function example() {
  const first = 1;
  const second = 2;
  const third = 3;
  return first + second + third;
}
```

When this MDX is processed, the generated output is missing the first statement (`const first = 1;`), resulting in:

```js
export function example() {
  const second = 2;
  const third = 3;
  return first + second + third;  // ReferenceError: first is not defined
}
```

### Expected behavior

All statements within a block should be included in the generated output, including the first statement. The code should execute without errors.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is causing runtime errors in our MDX documentation where the first variable declaration or import statement in function bodies is missing from the compiled output.

---
Repository: /testbed
