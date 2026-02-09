# Bug Report

### Describe the bug

I'm encountering an issue with unary expression optimization in the bundler. When `includeChildrenRecursively` is set to `true`, the bundler appears to be returning cached literal values instead of properly evaluating them, which leads to incorrect output in the generated bundle.

### Reproduction

```js
// Input code with unary expressions
const value = !someCondition;
const negated = -someNumber;

// When bundling with tree-shaking enabled, the unary expressions
// are not being evaluated correctly in certain contexts
```

The problem seems to occur specifically when:
1. Unary expressions are used in the code
2. The bundler attempts to optimize literal values
3. `includeChildrenRecursively` is true during the evaluation phase

### Expected behavior

Unary expressions should be evaluated correctly regardless of whether `includeChildrenRecursively` is true or false. The cached literal value should only be returned when it's safe to do so, and the evaluation logic should properly handle both cases.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues in production builds where the output doesn't match the expected behavior. Any help would be appreciated!

---
Repository: /testbed
