# Bug Report

### Describe the bug

I'm encountering an issue with automatic semicolon insertion (ASI) in the MDX parser. When the parser attempts to insert a semicolon, the `onInsertedSemicolon` callback is being triggered even when semicolon insertion is not actually valid or possible.

### Reproduction

```js
// When parsing code where ASI should NOT apply
const parser = /* initialize parser with onInsertedSemicolon callback */

// The callback fires even when canInsertSemicolon() returns false
// This causes incorrect behavior in tooling that relies on accurate ASI detection
```

The callback is being invoked unconditionally before checking whether semicolon insertion is actually allowed at that position. This leads to false positives where the callback reports a semicolon was inserted when it actually wasn't.

### Expected behavior

The `onInsertedSemicolon` callback should only be called when a semicolon is actually inserted (i.e., when `canInsertSemicolon()` returns true). The callback should not fire if semicolon insertion is not valid at the current position.

### Additional context

This appears to affect any tooling or linting that depends on accurate semicolon insertion notifications from the parser. The callback is meant to notify when ASI occurs, but currently it's notifying even when ASI doesn't happen.

---
Repository: /testbed
