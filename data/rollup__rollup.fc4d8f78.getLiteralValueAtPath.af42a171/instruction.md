# Bug Report

### Describe the bug

I'm experiencing an issue with conditional expressions where the literal value evaluation seems to be inverted when both branches have different values. The bundler appears to be returning the wrong truthy/falsy value in certain cases.

### Reproduction

```js
const result = someCondition ? truthyValue : falsyValue;
```

When the bundler tries to determine the literal value of a conditional expression where:
- The consequent and alternate branches have different literal values
- Both values can be cast to boolean
- The condition cannot be statically determined

The evaluated result appears to be inverted - when it should return a truthy value it returns falsy, and vice versa.

This is affecting tree-shaking and dead code elimination in my builds, as the bundler is making incorrect assumptions about which code paths are reachable.

### Expected behavior

The bundler should correctly identify whether a conditional expression evaluates to a truthy or falsy value, and use this information for proper optimization and tree-shaking.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
