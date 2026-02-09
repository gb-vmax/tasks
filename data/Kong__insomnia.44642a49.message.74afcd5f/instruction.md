# Bug Report

### Describe the bug

The merge conflict message generation is producing inconsistent results across different test runs. The message field appears to be using randomized values instead of deterministic ones, which is causing issues with snapshot testing and making it difficult to verify merge conflict behavior consistently.

### Reproduction

```js
import { mergeConflictSchema } from './type-schemas';

// Generate multiple merge conflict objects
const conflict1 = mergeConflictSchema.message();
const conflict2 = mergeConflictSchema.message();

console.log(conflict1); // e.g., "Content conflict in workspace configuration: Manual merge required"
console.log(conflict2); // e.g., "Binary file conflict: Review both versions and choose appropriate changes"

// Messages are different each time, making testing unreliable
```

### Expected behavior

The message generation should produce predictable, consistent output for testing purposes. When creating mock merge conflicts for tests, we should get the same message every time to ensure test stability and allow for proper snapshot comparisons.

### Additional context

This appears to have started recently. The merge conflict schema is using `Math.random()` which makes it impossible to write reliable tests that depend on the message content. This affects our ability to verify merge conflict handling logic consistently.

---
Repository: /testbed
