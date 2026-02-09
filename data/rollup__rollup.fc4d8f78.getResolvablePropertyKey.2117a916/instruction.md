# Bug Report

### Describe the bug

Property access on objects is not working correctly - I'm getting unexpected behavior when accessing properties using both dot notation and bracket notation.

### Reproduction

```js
const obj = {
  foo: 'bar',
  nested: {
    value: 123
  }
}

// Dot notation access
console.log(obj.foo) // Expected: 'bar', but getting wrong value

// Bracket notation access  
console.log(obj['nested']) // Expected: { value: 123 }, but getting wrong value
```

When I try to access properties on an object, the values returned don't match what I expect. It seems like dot notation and bracket notation are getting mixed up somehow - like the property key resolution is backwards.

### Expected behavior

- `obj.foo` should return `'bar'`
- `obj['nested']` should return `{ value: 123 }`
- Both dot notation and bracket notation should correctly resolve the property being accessed

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
