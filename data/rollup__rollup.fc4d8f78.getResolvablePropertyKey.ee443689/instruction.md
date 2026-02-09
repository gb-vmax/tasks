# Bug Report

### Describe the bug

I'm encountering an issue with member expression property access in computed vs non-computed scenarios. It seems like the property resolution is getting mixed up between computed and non-computed member expressions.

### Reproduction

```js
const obj = {
  foo: 'bar',
  baz: 'qux'
}

// Non-computed property access (dot notation)
obj.foo  // Expected: resolves 'foo', but appears to be doing something unexpected

// Computed property access (bracket notation)
obj['baz']  // Expected: resolves 'baz', but behavior seems swapped
```

When I use dot notation to access properties, the resolution doesn't work as expected. Similarly, bracket notation seems to be resolving incorrectly. It's like the two modes got their logic reversed somehow.

### Expected behavior

- `obj.foo` should resolve the property name `'foo'` correctly
- `obj['baz']` should resolve the computed property `'baz'` correctly

The property key resolution should work consistently regardless of whether I'm using computed (bracket) or non-computed (dot) notation.

### System Info
- Rollup version: latest
- Node version: 18.x

This might be related to recent changes in how member expressions are analyzed. Any help would be appreciated!

---
Repository: /testbed
