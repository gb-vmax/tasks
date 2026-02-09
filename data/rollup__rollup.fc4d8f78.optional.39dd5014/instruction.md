# Bug Report

### Describe the bug

I'm experiencing an issue with optional chaining behavior in member expressions. When using the optional chaining operator (`?.`), it seems to be inverted - properties that should be treated as optional are being treated as required, and vice versa.

### Reproduction

```js
const obj = {
  foo: {
    bar: 'value'
  }
}

// This should safely access nested properties
const result1 = obj?.foo?.bar  // Expected to work with optional chaining
const result2 = obj.foo.bar    // Expected to work without optional chaining

// But the behavior seems reversed
```

When I mark a member expression as optional, it behaves as if it's NOT optional, and when I don't use optional chaining, it behaves as if it IS optional. This is causing unexpected behavior in my code where safe property access fails and unsafe access succeeds.

### Expected behavior

Optional chaining (`?.`) should allow safe access to potentially undefined properties without throwing errors. Non-optional member access should work normally for defined properties.

### Additional context

This seems to have started happening recently. The optional flag on member expressions appears to be getting inverted somehow.

---
Repository: /testbed
