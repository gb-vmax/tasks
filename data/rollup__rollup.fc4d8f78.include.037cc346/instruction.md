# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where code that should be included in the bundle is being incorrectly removed. This appears to be related to how block statements handle inclusion logic.

### Reproduction

```js
// module.js
export function foo() {
  if (true) {
    console.log('This should be included');
    sideEffect();
  }
}

function sideEffect() {
  globalState.value = 42;
}

// main.js
import { foo } from './module.js';
foo();
```

When bundling this code, the `sideEffect()` call and related code within the block statement gets removed even though it should be preserved due to the side effects.

### Expected behavior

All code with side effects inside block statements should be included in the final bundle, regardless of whether the block is being deoptimized or not. The bundler should not aggressively remove code that has observable effects.

### Additional context

This seems to have started happening recently. The tree-shaking is being too aggressive and removing code that should be kept based on the inclusion context.

---
Repository: /testbed
