# Bug Report

### Describe the bug

After a recent update, variable type casting seems to be completely broken. When I try to get the value from a Variable object, it's returning `undefined` instead of the actual value.

### Reproduction

```js
const myVar = new Variable({
  key: 'testVar',
  value: 'hello world',
  type: 'string'
});

const result = myVar.cast('some value');
console.log(result); // Expected: 'some value', Actual: undefined
```

Also tried with nested variables:

```js
const innerVar = new Variable({
  key: 'inner',
  value: 42,
  type: 'number'
});

const outerVar = new Variable({
  key: 'outer',
  value: innerVar,
  type: 'number'
});

const result = outerVar.cast(innerVar);
console.log(result); // Expected: 42, Actual: undefined
```

### Expected behavior

The `cast` method should return the properly type-casted value, not `undefined`. This was working fine before and now it's breaking variable resolution in my requests.

### System Info
- insomnia-sdk version: latest
- Platform: macOS

---
Repository: /testbed
