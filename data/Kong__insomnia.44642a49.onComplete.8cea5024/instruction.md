# Bug Report

### Describe the bug
When using the `app.prompt()` plugin API with validation and transform options, the prompt dialog doesn't apply transformations to the input value before resolving. The transform function is being ignored even when provided in the options.

### Reproduction
```js
const result = await context.app.prompt('Enter value', {
  defaultValue: 'test',
  transform: (value) => value.toUpperCase(),
  validate: (value) => {
    if (!value) return 'Value required';
  }
});

// Expected: result should be uppercase
// Actual: result is returned as-is without transformation
console.log(result); // prints 'test' instead of 'TEST'
```

### Expected behavior
When a `transform` option is provided to `app.prompt()`, the returned value should be the transformed value. The transformation should be applied after validation passes but before the promise resolves.

### Additional context
This affects plugin developers who need to normalize or format user input from prompts. The validation works fine, but there's no way to transform the input before it's returned to the caller.

---
Repository: /testbed
