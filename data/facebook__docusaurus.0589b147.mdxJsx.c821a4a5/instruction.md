# Bug Report

### Describe the bug

I'm encountering an issue with the MDX parser where it's throwing an error about expecting a proper `acorn` instance, even when I'm passing in a valid acorn parser with both `parse` and `parseExpressionAt` methods.

### Reproduction

```js
import * as acorn from 'acorn';
import { mdxJsx } from 'remark-mdx';

const parser = mdxJsx({
  acorn: acorn,
  acornOptions: {
    ecmaVersion: 2020
  }
});

// Error: Expected a proper `acorn` instance passed in as `options.acorn`
```

### Expected behavior

The parser should accept a valid acorn instance without throwing an error. The acorn object I'm passing has both required methods (`parse` and `parseExpressionAt`), so it should be recognized as a proper acorn instance.

### Additional context

This seems to have started happening recently. The error message suggests that the validation logic might be inverted - it's rejecting valid acorn instances instead of accepting them.

---
Repository: /testbed
