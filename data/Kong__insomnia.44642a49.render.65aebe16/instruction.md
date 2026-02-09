# Bug Report

### Describe the bug

I'm experiencing an issue with template rendering where the output seems to be cached and doesn't update when the underlying context or variables change. After making changes to request variables or environment values, the rendered templates still show the old values instead of the updated ones.

### Reproduction

```js
// Set up a template with a variable
const template = "{{ myVar }}";

// First render with initial value
const context = { myVar: "initial" };
const result1 = render(template, context);
console.log(result1); // Outputs: "initial"

// Update the context variable
context.myVar = "updated";
const result2 = render(template, context);
console.log(result2); // Expected: "updated", but still outputs: "initial"
```

### Expected behavior

Each time a template is rendered, it should reflect the current state of the context variables. Changes to environment variables, request variables, or any other context data should be immediately reflected in subsequent renders.

### Additional context

This seems to have started happening recently. The templates appear to be using cached results even when the input data has changed. This is particularly problematic when:
- Switching between different environments
- Updating variables during a request chain
- Making multiple requests with dynamic values

The issue affects both simple variable substitutions and more complex template expressions.

---
Repository: /testbed
