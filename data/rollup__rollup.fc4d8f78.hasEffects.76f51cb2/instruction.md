# Bug Report

### Describe the bug

I'm encountering an issue where functions marked with `@__PURE__` annotations are being treated as having side effects instead of being properly optimized away during tree-shaking. This is causing unnecessary code to be included in the final bundle.

### Reproduction

```js
// utils.js
export const pureFunction = /*@__PURE__*/ () => {
  return { value: 42 };
};

export const usedFunction = () => {
  return "used";
};

// main.js
import { usedFunction } from './utils.js';

console.log(usedFunction());
```

When bundling this code, `pureFunction` should be completely removed from the output since it's marked as pure and never used. However, it's still appearing in the bundled output.

### Expected behavior

Functions annotated with `@__PURE__` comments that are not used should be tree-shaken and removed from the final bundle. The annotation should tell the bundler that the function has no side effects and can be safely eliminated if unused.

### Additional context

This seems to have started happening recently. Previously, pure annotations were working correctly and unused pure functions were being removed as expected. Now they're being kept in the bundle which is increasing the final bundle size unnecessarily.

---
Repository: /testbed
