# Bug Report

### Describe the bug

I'm encountering an error when trying to use MDX processor methods after freezing a processor. The error message says I should "Call `[method]` on a frozen processor" but this doesn't make sense - I thought frozen processors shouldn't allow method calls?

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkMdx)
  .use(remarkRehype)
  .use(rehypeStringify)

// Freeze the processor
const frozenProcessor = processor.freeze()

// This should throw an error but doesn't
frozenProcessor.use(somePlugin)
```

### Expected behavior

When calling methods like `use()` on a frozen processor, it should throw an error preventing the operation. Instead, it seems like the validation is inverted - it's allowing operations on frozen processors when it should be blocking them.

The error message also seems confusing, suggesting to "Call `use` on a frozen processor" when that's exactly what shouldn't be allowed.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
