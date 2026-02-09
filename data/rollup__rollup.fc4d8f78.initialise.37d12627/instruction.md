# Bug Report

### Describe the bug

I'm experiencing an issue where block statements are being incorrectly deoptimized in certain scenarios. It seems like the compiler is treating normal code blocks as if they need to be deoptimized, which is causing unexpected behavior in the generated output.

### Reproduction

```js
function test() {
  {
    const x = 1;
    const y = 2;
    return x + y;
  }
}
```

When bundling code with regular block statements (not containing 'use asm' directives), the blocks are being deoptimized when they shouldn't be. This appears to affect any code that uses block scoping without special directives.

### Expected behavior

Only block statements that actually contain a 'use asm' directive at the beginning should be deoptimized. Regular block statements should be optimized normally.

### Additional context

This seems to have started happening recently. The deoptimization is being applied too broadly, affecting performance of the bundled output. I noticed this when comparing bundle sizes and runtime behavior before and after a recent update.

---
Repository: /testbed
