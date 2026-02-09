# Bug Report

### Describe the bug

I'm experiencing an issue with object destructuring patterns in generated code. When using object patterns with multiple properties, there seems to be an extra comma appearing after the last property in the destructured object.

### Reproduction

```js
// Given an object pattern with multiple properties like:
const { a, b, c } = obj;

// The generated output includes a trailing comma:
const { a, b, c, } = obj;
```

This is causing syntax issues in environments that don't support trailing commas in object patterns, and the generated code looks malformed.

### Expected behavior

Object destructuring patterns should not have a trailing comma after the last property. The output should be:
```js
const { a, b, c } = obj;
```

instead of:
```js
const { a, b, c, } = obj;
```

### Additional context

This appears to affect all object patterns regardless of the number of properties. Single property patterns seem fine, but anything with 2+ properties shows this behavior.

---
Repository: /testbed
