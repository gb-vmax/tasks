# Bug Report

### Describe the bug

I'm experiencing an issue with the suggested variable name logic for external modules. When multiple imports suggest different names with the same frequency, the behavior seems inconsistent - the suggested name doesn't match what I'd expect based on which name was suggested most commonly.

### Reproduction

```js
// Given an external module with multiple imports suggesting names
const externalModule = new ExternalModule(...);

// Suggest 'foo' twice
externalModule.suggestName('foo');
externalModule.suggestName('foo');

// Suggest 'bar' twice  
externalModule.suggestName('bar');

// Expected: suggestedVariableName should be 'foo' (first to reach count of 2)
// Actual: suggestedVariableName is 'bar'
```

The issue appears when two or more names are suggested the same number of times. Instead of keeping the first name that reached the highest count, it gets replaced by subsequent names with equal counts.

### Expected behavior

When multiple names have the same suggestion count, the first name to reach that count should be preferred and kept as the `suggestedVariableName`. The current behavior seems to always prefer the most recently suggested name when counts are tied.

### Additional context

This affects how external imports are named in the generated bundle, potentially causing inconsistent naming across builds when import orders vary.

---
Repository: /testbed
