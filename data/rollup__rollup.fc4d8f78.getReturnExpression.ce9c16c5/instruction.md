# Bug Report

### Describe the bug

I'm experiencing an issue where function return types are not being correctly tracked after the first call. It seems like the return expression analysis is returning incorrect results on subsequent accesses.

### Reproduction

```js
function getValue() {
  return { data: 'test' };
}

const result1 = getValue();
const result2 = getValue();

// First call works correctly
// But subsequent calls return unexpected type information
```

The problem appears to be related to how return expressions are cached and retrieved. On the first evaluation, the correct return type is computed, but on subsequent evaluations, an unknown/default return expression is used instead of the cached value.

### Expected behavior

The return expression should be consistently tracked across multiple accesses. Once computed, the cached return expression should be returned on subsequent calls, not replaced with a default/unknown value.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
