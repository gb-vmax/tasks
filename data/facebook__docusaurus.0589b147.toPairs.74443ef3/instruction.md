# Bug Report

### Describe the bug

I'm encountering an issue with the `toPairs` function when processing find and replace tuples. When I pass a single tuple (not wrapped in an array), it's not being handled correctly and the function seems to be treating it differently than expected.

### Reproduction

```js
// This should work but doesn't behave as expected
const result = toPairs([/pattern/, 'replacement']);

// Expected: Should recognize this as a single tuple and wrap it
// Actual: The tuple is not being processed correctly
```

The issue appears when passing a single tuple directly instead of an array of tuples. The function should detect whether the input is a single tuple or a list of tuples and handle both cases appropriately.

### Expected behavior

When passing a single tuple like `[/pattern/, 'replacement']`, the function should:
1. Detect that this is a single tuple (not a list of tuples)
2. Wrap it in an array automatically
3. Process it correctly

The current logic for detecting whether we have a single tuple or a list of tuples doesn't seem to be working right.

### Additional context

This is related to the find-and-replace functionality in remark-gfm. The function is supposed to normalize the input by ensuring we always work with a list of tuples, even if a single tuple is provided.

---
Repository: /testbed
