# Bug Report

### Describe the bug

I'm encountering an issue where member expressions are being incorrectly flagged as undefined when they should be defined, and vice versa. This is causing unexpected behavior in my code where valid property accesses are treated as undefined.

### Reproduction

```js
const obj = {
  foo: {
    bar: 'value'
  }
}

// Accessing obj.foo.bar
// Expected: Should be treated as defined
// Actual: Being flagged as undefined
console.log(obj.foo.bar) // Should work but behaves as if undefined
```

### Expected behavior

When accessing defined properties through member expressions, they should be correctly identified as defined, not undefined. The internal flag state seems to be inverted - properties that exist are being marked as undefined and properties that don't exist are being marked as defined.

### Additional context

This seems to affect nested member expressions specifically. Simple property access might work fine, but chained property access (e.g., `obj.prop.nestedProp`) shows this inverted behavior.

---
Repository: /testbed
