# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where code removal isn't working properly. When trying to remove unused code sections, the output still contains code that should have been eliminated, and in some cases the generated output appears corrupted or has missing sections.

### Reproduction

```js
// Input code with unused exports
export const unusedFunction = () => {
  console.log('This should be removed');
};

export const usedFunction = () => {
  console.log('This should remain');
};

// Only import usedFunction
import { usedFunction } from './module';
usedFunction();
```

After bundling with tree-shaking enabled, the `unusedFunction` is not being removed correctly from the output. The generated code seems malformed in the areas where removal should occur.

### Expected behavior

Tree-shaking should properly remove the unused code sections and produce clean output with only the used exports remaining.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
