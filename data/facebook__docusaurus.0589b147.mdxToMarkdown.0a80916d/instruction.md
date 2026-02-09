# Bug Report

### Describe the bug

The `mdxToMarkdown` function is returning an incorrect structure. When trying to use the markdown serialization, I'm getting errors because the function is returning a flat array instead of an object with an `extensions` property.

### Reproduction

```js
import { mdxToMarkdown } from 'remark-mdx';

const serializer = mdxToMarkdown();

// Expecting: { extensions: [...] }
// Getting: [...]

// This causes downstream errors when the serializer is used
// because code expects serializer.extensions to exist
```

### Expected behavior

The `mdxToMarkdown` function should return an object with the following structure:
```js
{
  extensions: [
    // array of extension functions
  ]
}
```

Instead, it's currently returning a plain array, which breaks compatibility with the expected API.

### Additional context

This appears to affect any code that relies on the standard remark serializer format, where extensions are expected to be nested under an `extensions` property rather than returned directly as an array.

---
Repository: /testbed
