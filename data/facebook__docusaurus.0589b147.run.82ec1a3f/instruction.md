# Bug Report

### Describe the bug

I'm experiencing an issue with the trough pipeline execution in the remark vendor code. When running a pipeline with multiple middleware functions, the execution flow seems to be incorrect - it appears that the callback is being invoked too early, before all middleware functions have been processed.

### Reproduction

```js
const pipeline = trough();

pipeline.use(function(value, next) {
  console.log('Middleware 1:', value);
  next(null, value + 1);
});

pipeline.use(function(value, next) {
  console.log('Middleware 2:', value);
  next(null, value + 1);
});

pipeline.run(0, function(err, result) {
  console.log('Final result:', result);
  // Expected: 2
  // Actual: might not execute all middleware
});
```

### Expected behavior

The pipeline should execute all registered middleware functions in sequence, with each middleware receiving the output from the previous one. The final callback should only be invoked after all middleware has completed processing.

### System Info
- remark version: 15.0.1
- Node version: Latest LTS

The logic for determining when to call the final callback vs. continuing to the next middleware seems off. This is affecting markdown processing workflows that rely on multiple transformation steps.

---
Repository: /testbed
