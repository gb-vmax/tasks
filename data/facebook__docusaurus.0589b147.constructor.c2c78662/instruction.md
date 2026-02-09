# Bug Report

### Describe the bug

I'm encountering an issue with the remark processor where it seems like plugins aren't being applied correctly. When I try to use the processor with transformers, I'm getting unexpected behavior - it looks like the transformers aren't being executed in the right order or at all.

### Reproduction

```js
const processor = new Processor();

// Add some transformers
processor.use(somePlugin);
processor.use(anotherPlugin);

// Try to process markdown
const result = processor.processSync('# Hello World');

// Transformers don't seem to be applied correctly
```

### Expected behavior

The processor should properly initialize and execute all registered transformers in the correct order. Each plugin should be able to transform the AST as expected.

### Additional context

This seems to have started happening recently. I'm not sure if this is related to how the processor initializes its internal state, but the transformer pipeline doesn't seem to be working as it did before.

---
Repository: /testbed
