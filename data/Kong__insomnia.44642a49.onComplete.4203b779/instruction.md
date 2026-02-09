# Bug Report

### Describe the bug

When using the plugin prompt API, the returned value includes leading/trailing whitespace that wasn't present in previous versions. This is causing issues with plugins that expect trimmed input values.

### Reproduction

```js
// In a plugin
const value = await context.app.prompt('Enter a value', {
  defaultValue: 'test'
});

// User enters "  hello  " (with spaces)
console.log(value); // Expected: "hello", Actual: "  hello  "
```

The prompt dialog is returning values with whitespace intact instead of trimming them like it used to.

### Expected behavior

The prompt should automatically trim whitespace from user input before returning the value, especially for text inputs. This was the previous behavior and many plugins rely on it.

### Additional context

This seems to affect all input types. For number inputs, it would also be helpful if the value was normalized (e.g., converting "  123.00  " to "123").

---
Repository: /testbed
