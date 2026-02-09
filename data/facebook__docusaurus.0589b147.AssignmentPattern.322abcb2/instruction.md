# Bug Report

### Describe the bug

When using default parameter values in function declarations, the generated code has the parameter and default value in the wrong order. Instead of generating `param = defaultValue`, it's generating `= param defaultValue`.

### Reproduction

```js
// Input MDX/JS with default parameter
function example(param = 'default') {
  return param;
}

// Or with destructuring
const fn = ({ name = 'test' } = {}) => {
  console.log(name);
}
```

After processing, the output has malformed syntax where the equals sign appears before the parameter name, resulting in invalid JavaScript that won't parse.

### Expected behavior

Default parameters should be rendered as `param = defaultValue` (parameter name first, then equals sign, then default value), which is valid JavaScript syntax.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
