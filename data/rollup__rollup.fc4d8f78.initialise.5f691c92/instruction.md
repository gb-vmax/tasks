# Bug Report

### Describe the bug

I'm experiencing an issue with sourcemap generation where the sourcemap locations appear to be incorrect for block statements. The mappings seem to be pointing to the wrong positions in the generated code.

### Reproduction

```js
function test() {
  'use asm';
  var x = 1;
  return x;
}
```

When I build code with block statements that contain directives like `'use asm'`, the sourcemap mappings are off. The generated sourcemap doesn't correctly map back to the original source positions.

### Expected behavior

Sourcemap locations should accurately point to the correct positions in both the original source and generated code. Block statements should have their opening brace position properly tracked in the sourcemap.

### Additional context

This seems to affect any code with block statements, but it's particularly noticeable when using directives at the beginning of blocks. The sourcemap viewer shows incorrect line/column positions when trying to debug the bundled output.

---
Repository: /testbed
