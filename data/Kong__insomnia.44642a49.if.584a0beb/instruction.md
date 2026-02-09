# Bug Report

### Describe the bug
The `Variable.cast()` method is broken and not returning any values. When trying to cast values using a Variable instance, it always returns `undefined` regardless of the input.

### Reproduction
```js
const variable = new Variable({
  key: 'myVar',
  value: 'test',
  type: 'string'
});

// This returns undefined instead of the casted value
const result = variable.cast('hello');
console.log(result); // Expected: 'hello', Actual: undefined

// Same issue with other types
const numVar = new Variable({
  key: 'numVar',
  value: 123,
  type: 'number'
});

const numResult = numVar.cast('456');
console.log(numResult); // Expected: 456, Actual: undefined
```

### Expected behavior
The `cast()` method should return the value coerced to the variable's type. For example:
- String type should convert values to strings
- Number type should convert to numbers
- Boolean type should convert to booleans

### System Info
- insomnia-sdk version: latest
- The issue appeared after a recent update to the variables module

---
Repository: /testbed
