# Bug Report

### Describe the bug

I'm experiencing an issue with the `instanceof` operator in binary expressions. When using `instanceof` in my code, it seems like the right-hand side is not being handled correctly, which causes unexpected behavior in the bundled output.

### Reproduction

```js
class MyClass {}
const obj = new MyClass();

// This instanceof check behaves unexpectedly
if (obj instanceof MyClass) {
  console.log('This should work');
}
```

The code compiles but the `instanceof` operation doesn't work as expected in the output bundle. It seems like the symbol path for `Symbol.hasInstance` is being incorrectly applied to operators that are NOT `instanceof`.

### Expected behavior

The `instanceof` operator should correctly check if an object is an instance of a class by properly calling the `Symbol.hasInstance` method when it exists on the constructor. Other binary operators should not have this path included.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
