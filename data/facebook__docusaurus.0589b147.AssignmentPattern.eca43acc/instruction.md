# Bug Report

### Describe the bug

I'm encountering an issue with default parameter syntax in MDX files. When using default parameters in function declarations or arrow functions, the generated JavaScript output appears to be malformed with incorrect operator usage and reversed operand order.

### Reproduction

```js
// Input MDX with default parameters
function example(param = 'default') {
  return param;
}

const arrow = (value = 42) => value;
```

After processing through MDX, the generated output uses `==` (comparison operator) instead of `=` (assignment operator), and the left/right operands appear to be swapped.

### Expected behavior

Default parameter assignments should be preserved correctly in the output:
- Should use `=` for assignment, not `==` for comparison
- Parameter name should be on the left, default value on the right
- Example: `param = 'default'` not `'default' == param`

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken basic function parameter defaults which is pretty critical for JavaScript compatibility.

---
Repository: /testbed
