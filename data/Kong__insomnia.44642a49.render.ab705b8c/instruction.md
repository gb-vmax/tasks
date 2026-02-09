# Bug Report

### Describe the bug
After a recent update, template rendering with dynamic context values is not working correctly. When rendering templates that reference context properties that change between renders (like `iterationIndex` or environment-specific values), the output is cached incorrectly and returns stale values instead of the current ones.

### Reproduction
```js
// First render with iterationIndex = 0
const result1 = util.render('{{ _.iterationIndex }}');
console.log(result1); // Expected: "0", Got: "0" ✓

// Second render with iterationIndex = 1
const result2 = util.render('{{ _.iterationIndex }}');
console.log(result2); // Expected: "1", Got: "0" ✗
```

The same template string returns the cached result from the first render even though the context has changed.

### Steps to reproduce
1. Render a template that uses context variables (e.g., `iterationIndex`, environment variables)
2. Change the context values
3. Render the same template string again
4. Observe that the output doesn't reflect the updated context

### Expected behavior
Each render should evaluate the template with the current context values, not return cached results from previous renders with different context.

### Additional context
This seems to affect any template that uses the `util.render()` function when context properties change between invocations. The issue appears to be related to caching behavior that doesn't properly account for context changes.

---
Repository: /testbed
