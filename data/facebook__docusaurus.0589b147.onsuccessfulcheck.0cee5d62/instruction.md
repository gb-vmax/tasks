# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where it seems to be skipping the restore operation in certain scenarios. After some investigation, it appears that the `onsuccessfulcheck` callback is not properly restoring the parser state when it should.

### Reproduction

```js
// When parsing markdown with specific constructs that trigger successful checks
const parser = createTokenizer(/* ... */);

// The parser state is not being restored correctly
// This causes subsequent parsing operations to use incorrect state
```

The issue manifests when:
1. A construct check succeeds
2. The parser state should be restored
3. But the restore operation is being skipped due to an additional condition check

### Expected behavior

The `onsuccessfulcheck` callback should always restore the parser state when a check succeeds, regardless of any additional properties on the info object. The current implementation seems to be adding a conditional check that prevents restoration in valid scenarios.

### System Info
- remark version: 15.0.1
- Parser: createTokenizer

This is causing parsing inconsistencies where the tokenizer state gets out of sync with the expected state after successful construct checks.

---
Repository: /testbed
