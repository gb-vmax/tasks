# Bug Report

### Describe the bug

I'm experiencing an issue with variable declarations in MDX files. When I declare variables without initializing them, the generated code appears to be malformed. It seems like the order of operations got mixed up somehow.

### Reproduction

```js
// In an MDX file
export let myVariable;
```

When this gets processed, the generated JavaScript output doesn't look right. The variable identifier is missing from the declaration, and it's trying to access properties on `null`/`undefined`.

### Expected behavior

Variable declarations without initializers should generate valid JavaScript like:
```js
let myVariable;
```

Instead, the current output seems to be missing the variable name and attempting to write the initializer even when it doesn't exist.

### Additional context

This appears to have started happening recently. Variable declarations with initializers (like `let x = 5`) seem to work fine, but uninitialized declarations are broken.

---
Repository: /testbed
