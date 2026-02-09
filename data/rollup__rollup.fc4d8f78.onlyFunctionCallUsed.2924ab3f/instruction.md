# Bug Report

### Describe the bug

I'm encountering an issue where function declarations that are exported as default exports are not being properly analyzed for their usage patterns. It seems like the code is checking for `AssignmentExpression` parent nodes but then trying to access properties that don't exist on that node type.

### Reproduction

```js
// main.js
export default function myFunction() {
  return 42;
}

// consumer.js
import myFunction from './main.js';

// Only used as function call
const result = myFunction();
```

When bundling this code, the function usage detection appears to fail and the optimization that should apply to functions only used as calls doesn't work correctly.

### Expected behavior

The bundler should correctly identify that `myFunction` is only used as a function call and apply the appropriate optimizations. The parent node type check should properly handle `ExportDefaultDeclaration` nodes.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
