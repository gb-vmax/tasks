# Bug Report

### Describe the bug

Object spread operations are not being handled correctly, causing issues with property access and prototype chain resolution. When using spread syntax in object literals, the properties seem to be treated incorrectly which leads to unexpected behavior.

### Reproduction

```js
const obj1 = { a: 1, b: 2 };
const obj2 = { ...obj1, c: 3 };

// Properties from spread are not accessible as expected
console.log(obj2.a); // Should be 1
console.log(obj2.b); // Should be 2
```

Also seeing weird behavior with `__proto__` property handling:

```js
const obj = {
  __proto__: null,
  foo: 'bar'
};

// Prototype chain seems incorrect
```

### Expected behavior

- Spread properties should be properly merged into the target object
- `__proto__` property should be handled correctly when used as a regular property vs special prototype setter
- Object property access should work normally after spread operations

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
