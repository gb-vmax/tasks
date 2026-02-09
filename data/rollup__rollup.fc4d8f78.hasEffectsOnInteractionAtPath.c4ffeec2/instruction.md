# Bug Report

### Describe the bug

I'm experiencing an issue where property access on function objects is not being handled correctly during tree-shaking analysis. When accessing properties on functions (like `.bind`, `.call`, `.apply`, or custom properties), the bundler is incorrectly treating these as function calls and analyzing their side effects.

### Reproduction

```js
function myFunction() {
  console.log('test');
}

// Accessing a property on the function
const boundFn = myFunction.bind(null);

// Or accessing other properties
const fnName = myFunction.name;
const fnLength = myFunction.length;
```

The bundler appears to be analyzing these property accesses as if they were function invocations, which leads to incorrect tree-shaking behavior. Properties on function objects should be accessible without triggering the function call analysis path.

### Expected behavior

Property access on function objects (e.g., `.bind()`, `.name`, `.length`, or any custom properties) should be handled separately from function invocations. The bundler should only analyze function call effects when the function is actually being called, not when its properties are being accessed.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
