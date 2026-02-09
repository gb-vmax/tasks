# Bug Report

### Describe the bug

I'm encountering an issue with block statement handling where the deoptimization behavior seems incorrect. When working with code that doesn't have a `'use asm'` directive as the first statement, the entire block is being deoptimized when it shouldn't be.

### Reproduction

```js
// This block should NOT be deoptimized
{
  const x = 1;
  const y = 2;
  console.log(x + y);
}

// This block SHOULD be deoptimized
{
  'use asm';
  // asm.js code
}
```

### Expected behavior

Only blocks that start with a `'use asm'` directive should be deoptimized. Regular blocks without this directive should be optimized normally.

Currently it seems like the logic is inverted - blocks WITHOUT `'use asm'` are being deoptimized, while blocks WITH `'use asm'` are being optimized (which is backwards).

### Additional context

This affects code generation and optimization passes. The bundle output shows that normal blocks are being treated as if they contain asm.js code, leading to suboptimal output.

---
Repository: /testbed
