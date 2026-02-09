# Bug Report

### Describe the bug

I'm encountering an issue with catch block scoping where variables declared in catch clauses are not being handled correctly. It seems like the scope hierarchy is getting mixed up - catch parameter scopes are being created with the wrong body scope type, and the parent scope relationship appears to be incorrect.

### Reproduction

```js
try {
  throw new Error('test');
} catch (error) {
  // Variables and references inside catch block
  // are not resolving to the correct scope
  const localVar = error.message;
  console.log(localVar);
}
```

When analyzing code with try-catch blocks, the scope chain seems broken. The catch parameter scope should have a `CatchBodyScope` but it's getting a `FunctionBodyScope` instead, and the parent scope reference is pointing to the wrong level in the hierarchy.

### Expected behavior

- Catch blocks should create a proper `CatchBodyScope` for their body
- The parameter scope should correctly reference its immediate parent scope
- Variables declared within catch blocks should be properly scoped and accessible

### Additional context

This affects any code that uses try-catch blocks with parameter bindings. The scope resolution is completely broken for these cases, which can lead to incorrect variable resolution and potentially wrong analysis results.

---
Repository: /testbed
