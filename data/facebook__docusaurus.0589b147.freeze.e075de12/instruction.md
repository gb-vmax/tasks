# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX processor where plugins/attachers are not being applied correctly. It seems like plugins that should be running are being skipped, and the processor is not transforming content as expected.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkMdx)
  .use(myCustomPlugin, { enabled: true })
  .freeze()

// The custom plugin doesn't seem to be applied
const result = processor.processSync(content)
```

When I configure a plugin with options and freeze the processor, the transformations from my plugins don't appear in the output. The content passes through unchanged even though the plugins should be modifying it.

### Expected behavior

All configured plugins should be properly initialized and their transformers should be applied when the processor is frozen. Plugins with `enabled: true` or no options should run normally.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
