# Bug Report

### Describe the bug

I'm encountering an issue with the middleware pipeline where calling `.use()` with a valid function throws an unexpected error. It seems like the validation logic is inverted - it's rejecting functions when it should be accepting them.

### Reproduction

```js
const pipeline = trough()

// This should work but throws an error
pipeline.use(function myMiddleware(file, next) {
  // middleware logic
  next()
})
```

The error thrown is:
```
TypeError: Expected `middelware` to be a function, not function myMiddleware(file, next) { ... }
```

### Expected behavior

The `.use()` method should accept function arguments without throwing an error. The pipeline should be chainable and return the pipeline instance to allow for method chaining like:

```js
trough()
  .use(middleware1)
  .use(middleware2)
  .run(...)
```

### Additional context

This appears to have started happening recently. The error message itself is confusing since it's complaining that a function is not a function. Also noticed that the method is returning the middleware instead of the pipeline, which breaks chaining.

---
Repository: /testbed
