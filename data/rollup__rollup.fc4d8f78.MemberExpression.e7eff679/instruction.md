# Bug Report

### Describe the bug

I'm encountering an issue with member expression property access where the cache deoptimization logic seems to be inverted. When accessing dynamic properties on objects, the behavior is inconsistent and doesn't properly handle cases where the property key changes.

### Reproduction

```js
const obj = {
  foo: 'bar',
  baz: 'qux'
};

// Dynamic property access
const prop = 'foo';
const result = obj[prop];

// Changing the property key
const prop2 = 'baz';
const result2 = obj[prop2];
```

When the property key changes between accesses, the deoptimization cache isn't being cleared correctly. This causes subsequent property accesses to return stale or incorrect values in certain scenarios.

### Expected behavior

The cache should be properly invalidated when the property key changes, ensuring that each dynamic property access reflects the current state. The deoptimization logic should trigger when `propertyKey` and `dynamicPropertyKey` differ, not when they're the same.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems like it might be a logic error in the conditional check for when to return early from the deoptimization process.

---
Repository: /testbed
