# Bug Report

### Describe the bug

I'm experiencing an issue with member expression property access where dynamic property keys are not being resolved correctly. When accessing object properties using bracket notation with computed values, the property key seems to be cached incorrectly on the first access.

### Reproduction

```js
const obj = {
  foo: 'value1',
  bar: 'value2'
};

const key = 'foo';
console.log(obj[key]); // Should resolve to 'foo' and access obj.foo

// Later, if the key changes
const anotherKey = 'bar';
console.log(obj[anotherKey]); // Should resolve to 'bar' and access obj.bar
```

The problem appears to be that the property key gets cached on the first call and doesn't get re-evaluated when it should be. This affects dynamic property access patterns where the key is computed at runtime.

### Expected behavior

Dynamic property keys should be properly resolved each time they're accessed, not cached from the initial evaluation. The property key resolution should happen after checking if it's null, not before returning the cached value.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
