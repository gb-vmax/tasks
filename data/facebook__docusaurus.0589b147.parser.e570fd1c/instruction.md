# Bug Report

### Describe the bug

When using custom micromark extensions with MDX, the extensions are not being properly recognized or applied during parsing. The parser seems to be looking for extensions under the wrong data key, causing custom syntax extensions to be ignored.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'
import { remark } from 'remark'

// Add a custom micromark extension
const processor = remark()
  .data('micromarkExtensions', [myCustomExtension])
  .use(remarkMdx)

// Try to compile MDX with custom syntax
const result = await compile('# Custom syntax here', {
  remarkPlugins: [processor]
})

// Custom syntax is not parsed correctly
```

### Expected behavior

Custom micromark extensions registered via `data('micromarkExtensions')` should be applied during the markdown parsing phase. The parser should recognize and process custom syntax defined in these extensions.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

The extensions work fine in earlier versions but seem to have stopped working recently. It looks like the configuration might not be getting passed through correctly to the fromMarkdown function.

---
Repository: /testbed
