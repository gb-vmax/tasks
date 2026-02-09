# Bug Report

### Describe the bug

I'm encountering an issue with ES module exports where the wrong variable name is being used in the generated code. When bundling modules with named exports that have expressions, the exported name is being used instead of the local name in the constant declaration.

### Reproduction

When you have a module with exports like this:

```js
export { foo as bar };
```

The generated output incorrectly uses the exported name in the declaration instead of the local name. This causes the wrong variable to be declared and breaks the module.

For example, if the local name is `foo` and it's exported as `bar`, the generated code should declare `const foo = ...` but instead it's declaring `const bar = ...`.

### Expected behavior

The bundler should generate code that declares the constant using the local variable name, not the exported name. The local name should be used in the declaration, and then the export statement should map the exported name to the local name.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
