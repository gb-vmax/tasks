# Bug Report

### Describe the bug

I'm experiencing issues with SystemJS exports when using multiple export names for the same variable. It seems like the wrong export name is being used in the generated code.

### Reproduction

```js
// Input code
const foo = 'value';
export { foo, foo as bar };
```

When this gets transpiled to SystemJS format, the export is using the wrong name from the export names list. Instead of using the first export name, it's picking a different one.

### Expected behavior

The SystemJS export should use the first export name (`foo`) from the list of export names associated with the variable. The generated code should look something like:

```js
exports("foo", foo)
```

But instead it's using the wrong index from the export names array.

### Additional context

This affects any scenario where a variable is exported multiple times with different names. The export name selection logic seems to be off.

---
Repository: /testbed
