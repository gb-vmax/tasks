# Bug Report

### Describe the bug

The `waitForInputPlugin` is displaying "waiting for input" messages at the wrong time. It's showing the waiting message when the input specifier is successfully resolved instead of when it's missing/unresolved.

### Reproduction

When running rollup with the waitForInputPlugin:

1. Set up a configuration that uses `waitForInputPlugin()`
2. Provide an input specifier that resolves successfully
3. The plugin incorrectly displays "waiting for input [specifier]..." even though the input is already available

The expected behavior is that the waiting message should only appear when an input specifier cannot be resolved (returns null), not when it successfully resolves.

### Expected behavior

The plugin should:
- Display "waiting for input..." messages only when `this.resolve(specifier)` returns `null`
- Not display waiting messages when the specifier is successfully resolved
- Avoid duplicate messages for the same specifier

### Additional context

This seems to be causing confusion during the build process as it shows waiting messages for inputs that are already present and ready to be processed.

---
Repository: /testbed
