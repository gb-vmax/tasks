# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with property enumeration on exported objects. Properties that should be enumerable are no longer showing up when iterating over objects or using methods like `Object.keys()`.

### Reproduction

```js
// Create an object with exported properties
const myObject = {};
__export(myObject, {
  prop1: () => 'value1',
  prop2: () => 'value2'
});

// These should work but don't
console.log(Object.keys(myObject)); // Expected: ['prop1', 'prop2'], Got: []
for (let key in myObject) {
  console.log(key); // Nothing is printed
}
```

### Expected behavior

Properties added via `__export` should be enumerable by default, allowing them to be discovered through standard enumeration methods like `Object.keys()`, `for...in` loops, etc.

### Additional context

This seems to have started happening after the latest changes. The properties are still accessible directly (e.g., `myObject.prop1` works), but they don't appear in enumerations anymore which breaks some of our tooling that relies on discovering available properties dynamically.

---
Repository: /testbed
