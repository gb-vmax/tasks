# Bug Report

### Describe the bug

I'm experiencing an issue with destructuring assignments when using computed property names. The destructuring doesn't seem to work correctly when the property key is computed dynamically.

### Reproduction

```js
const key = 'value';
const obj = {
  [key]: 42
};

// Destructuring with computed property
const { [key]: result } = obj;
console.log(result); // Expected: 42, but behavior is incorrect
```

Another example:

```js
function test() {
  const prop = 'data';
  const source = { data: 'hello' };
  
  const { [prop]: extracted } = source;
  return extracted;
}

console.log(test()); // Should return 'hello'
```

### Expected behavior

When destructuring objects with computed property names (using bracket notation like `[key]`), the values should be correctly extracted from the source object. The computed key should be evaluated and used to access the corresponding property.

### Additional context

This seems to affect destructuring patterns with dynamic/computed keys. Static property names work fine, but as soon as I use the bracket notation for computed properties, things break.

---
Repository: /testbed
