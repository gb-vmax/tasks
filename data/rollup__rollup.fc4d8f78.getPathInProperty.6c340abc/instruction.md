# Bug Report

### Describe the bug

Object destructuring with computed property names is not working correctly. When destructuring an object that uses computed properties, the values are not being properly extracted and remain undefined.

### Reproduction

```js
const obj = {
  [Symbol.for('key')]: 'value',
  computed: 'test'
};

const { [Symbol.for('key')]: extracted } = obj;
console.log(extracted); // Expected: 'value', Actual: undefined
```

Another example with dynamic keys:

```js
const key = 'dynamicKey';
const data = {
  [key]: 'some value'
};

const { [key]: result } = data;
console.log(result); // Expected: 'some value', Actual: undefined
```

### Expected behavior

Destructuring with computed property names should correctly extract the values from the source object. The extracted variables should contain the expected values, not undefined.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
