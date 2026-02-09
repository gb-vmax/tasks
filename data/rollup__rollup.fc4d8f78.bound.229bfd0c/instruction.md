# Bug Report

### Describe the bug

I'm experiencing an issue with member expression property access in my code. After a recent update, accessing properties on objects seems to behave in reverse - properties that should be accessible are reported as unbound, and vice versa.

### Reproduction

```js
const obj = {
  foo: {
    bar: 'value'
  }
}

// Accessing nested property
const result = obj.foo.bar

// Expected: Property access should work normally
// Actual: Property binding state appears inverted
```

When I try to access object properties, the binding mechanism seems to be inverted. Properties that are clearly defined and should be bound are being treated as if they're not bound, and this is causing unexpected behavior in my application.

### Expected behavior

Member expressions should correctly identify bound properties. When accessing `obj.foo.bar`, the property should be recognized as bound if it exists on the object.

### Additional context

This seems to have started happening recently. The issue manifests when dealing with nested object property access and the internal tracking of whether properties are bound or not appears to be flipped.

---
Repository: /testbed
