# Bug Report

### Describe the bug

I'm encountering an issue where exported default functions are incorrectly being treated as if they're only used in function call contexts, even when they're being used in other ways (like being assigned to variables or passed as values).

### Reproduction

```js
// input.js
export default function myFunction() {
  console.log('test');
}

// consumer.js
import myFunction from './input.js';
const funcRef = myFunction; // Not a function call - just a reference
funcRef();
```

The bundler seems to be misidentifying how `myFunction` is being used. It appears to always consider default exported functions as "only used in function calls" regardless of how they're actually being referenced in the code.

### Expected behavior

The bundler should correctly detect that the function is being used as a value/reference (not just called), and handle the tree-shaking and optimization accordingly. Functions that are assigned to variables, passed as arguments, or otherwise used as values should not be flagged as "only function call used".

### Additional context

This seems to affect default exported function declarations specifically. Named exports and variable declarator functions appear to work correctly.

---
Repository: /testbed
