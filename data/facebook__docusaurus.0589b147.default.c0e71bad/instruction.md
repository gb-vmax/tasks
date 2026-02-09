# Bug Report

### Describe the bug

After a recent update, the remark-mdx plugin is no longer being exported correctly. When trying to import and use the plugin, I'm getting errors about the default export being undefined or not a function.

### Reproduction

```js
import remarkMdx from 'remark-mdx';
import { unified } from 'unified';
import remarkParse from 'remark-parse';

const processor = unified()
  .use(remarkParse)
  .use(remarkMdx);

// This throws an error - remarkMdx is not a function
processor.process('# Hello');
```

### Expected behavior

The plugin should be importable and usable as a default export like before. The processor should be able to use the plugin without any errors.

### Additional context

This seems to have broken after some refactoring. The export statement looks wrong - it's exporting an arrow function that returns `remarkMdx300` instead of just exporting `remarkMdx300` directly like it did before.

---
Repository: /testbed
