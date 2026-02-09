# Bug Report

### Describe the bug

I'm encountering an issue with update expressions (like `++` and `--`) in my code. It seems like the operators are not being handled correctly, causing unexpected behavior in the generated output.

### Reproduction

```js
let count = 0;
count++;

// or with decrement
let value = 10;
value--;
```

When bundling code that contains increment/decrement operators, the output doesn't work as expected. The operation seems to be using the wrong operator character.

### Expected behavior

Update expressions should correctly apply the increment (`++`) or decrement (`--`) operator to the variable. The bundled code should maintain the same behavior as the original code.

### Additional context

This appears to affect both prefix and postfix update expressions. The issue manifests when the code is processed and transformed during the bundling process.

---
Repository: /testbed
