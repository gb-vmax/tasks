# Bug Report

### Describe the bug

After a recent update, the test generation is producing invalid JavaScript code that causes syntax errors when running test suites. The generated test file includes references to undefined variables like `__testStats` even when there are no tests or suites defined.

### Reproduction

When generating tests from an empty or minimal test suite configuration:

```js
const suites = [];
const generated = generate(suites);
// Generated code includes:
// beforeEach(() => { __testStats.executed++; });
// But __testStats is never defined because there are no tests
```

This results in a `ReferenceError: __testStats is not defined` when the generated test file is executed.

### Expected behavior

The generated test code should only include references to `__testStats` when it's actually defined (i.e., when there are tests present). For empty test suites, the generated code should not attempt to increment or reference statistics variables that don't exist.

### Additional context

This appears to affect test suites that have:
- No tests defined (`totalTests === 0`)
- Empty suites arrays
- Suites with only nested empty suites

The code generation seems to be adding the `beforeEach` hook that increments `__testStats.executed` unconditionally, but only conditionally defining the `__testStats` variable itself.

---
Repository: /testbed
