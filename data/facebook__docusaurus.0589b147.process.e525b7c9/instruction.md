# Bug Report

### Describe the bug

The processor is getting frozen before the processing actually starts, which prevents any modifications or subsequent processing calls. This causes issues when trying to reuse a processor instance or when the processing needs to modify the processor state.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkRehype)
  .use(rehypeStringify);

// First call works fine
await processor.process('# Hello');

// Second call fails because processor was frozen too early
await processor.process('# World');
```

The processor gets frozen immediately when `.process()` is called, but before the actual processing logic executes. This means the processor state is locked before it's actually needed, preventing legitimate modifications during the processing pipeline.

### Expected behavior

The processor should only be frozen after setting up the processing execution, not before. This would allow the processor to be used multiple times and let the processing pipeline make necessary state changes.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
