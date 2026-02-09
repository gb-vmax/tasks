# Bug Report

### Describe the bug

When generating bundle output with both `intro` and other content, the intro text is not being properly separated from the rest of the code. There's no blank line between the intro and the main bundle content, which causes formatting issues.

### Reproduction

```js
import { rollup } from 'rollup';

const bundle = await rollup({
  input: 'src/main.js',
  // ... other config
});

await bundle.generate({
  format: 'es',
  intro: '/* This is intro text */'
});

// Expected output:
// /* This is intro text */
//
//
// [main bundle content]

// Actual output:
// /* This is intro text */
// [main bundle content]
```

### Expected behavior

The intro should be followed by two newlines (blank line) to properly separate it from the main bundle content, similar to how outro is handled.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
