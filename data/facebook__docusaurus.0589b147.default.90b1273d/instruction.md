# Bug Report

### Describe the bug

After a recent update, the remark-directive plugin appears to be broken. When trying to use directives in markdown documents, they're not being processed correctly. The plugin seems to export a function that returns the transformer instead of exporting the transformer directly.

### Reproduction

```js
import remarkDirective from 'remark-directive';
import { unified } from 'unified';
import remarkParse from 'remark-parse';

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)
  .use(remarkStringify);

const markdown = '::note\nThis is a note\n::';
const result = processor.processSync(markdown);
// Directives are not being transformed
```

### Expected behavior

The directive syntax should be parsed and transformed correctly. The plugin should work as a standard remark plugin without requiring additional function calls.

### Additional context

This seems to have started happening in version 3.0.0. The export structure changed and now the default export appears to be a function that needs to be called to get the actual plugin, rather than being the plugin itself. This breaks compatibility with how remark plugins are typically used.

---
Repository: /testbed
