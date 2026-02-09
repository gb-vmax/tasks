# Bug Report

### Describe the bug

Object destructuring with computed property keys is not working correctly. When destructuring objects with computed properties, the values are not being properly extracted and remain undefined.

### Reproduction

```js
const obj = {
  [Symbol.for('key')]: 'value',
  regular: 'test'
};

const { [Symbol.for('key')]: computed, regular } = obj;

console.log(computed); // Expected: 'value', Actual: undefined
console.log(regular);  // Expected: 'test', Actual: 'test'
```

Also happens with dynamic computed keys:

```js
const key = 'dynamic';
const data = {
  [key]: 'data'
};

const { [key]: result } = data;
console.log(result); // Expected: 'data', Actual: undefined
```

### Expected behavior

Destructuring with computed property keys should extract the correct values from the object, just like regular property destructuring does.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
