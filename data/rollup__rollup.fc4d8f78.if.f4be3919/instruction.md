# Bug Report

### Describe the bug

After a recent update, I'm encountering an issue with ES module exports where expressions assigned to exported constants are no longer being included in the output. The export declarations are generated, but the actual assignment/initialization code is missing.

### Reproduction

When bundling code that exports constants with expressions, like:

```js
export const myValue = someExpression();
export const anotherValue = computedResult;
```

The generated output only includes the constant declaration without the assignment:

```js
const myValue;
const anotherValue;
export { myValue, anotherValue };
```

Instead of the expected:

```js
const myValue = someExpression();
const anotherValue = computedResult;
export { myValue, anotherValue };
```

### Expected behavior

The exported constants should be properly initialized with their expressions. The finalizer should generate both the declaration AND the assignment for exports that have an expression value.

### Additional context

This seems to affect any ES module output where exports have associated expressions. The exports themselves are declared but they're essentially uninitialized, which breaks any code that depends on these exported values.

---
Repository: /testbed
