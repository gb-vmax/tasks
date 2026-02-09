# Bug Report

### Describe the bug

I'm experiencing an issue with MDX processing where empty strings are no longer being accepted as valid input values. After a recent update, passing an empty string causes the processor to reject it, even though empty strings should be valid MDX content.

### Reproduction

```js
const { compile } = require('@mdx-js/mdx');

// This now fails but should work
const result = await compile('');
```

When trying to compile an empty string, the value is rejected instead of being processed as valid (albeit empty) MDX content.

### Expected behavior

Empty strings should be treated as valid input. An empty MDX file or string is a legitimate use case and should compile successfully to an empty output.

### Additional context

This appears to have started happening recently. Previously, empty strings were handled correctly and would compile without issues. This is breaking existing code that sometimes needs to process empty content.

---
Repository: /testbed
