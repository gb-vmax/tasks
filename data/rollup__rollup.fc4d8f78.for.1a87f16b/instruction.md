# Bug Report

### Describe the bug

I'm encountering an issue with cached getters when using `cacheObjectGetters()` utility. After the first access, subsequent calls to the getter property return a function reference instead of the computed value.

### Reproduction

```js
const obj = {
  get computedValue() {
    return 42;
  }
};

cacheObjectGetters(obj, ['computedValue']);

console.log(obj.computedValue); // Expected: 42, Got: 42 (first call works)
console.log(obj.computedValue); // Expected: 42, Got: [Function: get computedValue]
```

### Expected behavior

The cached getter should return the computed value (42) on all subsequent accesses, not the getter function itself. The caching mechanism should replace the getter with the actual value after the first call.

### Additional context

This seems to have broken recently. The first access works fine and returns the expected value, but any subsequent access to the property returns what appears to be the original getter function instead of the cached value.

---
Repository: /testbed
