# Bug Report

### Describe the bug

I'm experiencing an issue with remark parsing when using plugins that add micromark or mdast extensions. The parser seems to be ignoring the extensions registered via plugins and always using empty arrays instead.

### Reproduction

```js
import {remark} from 'remark'
import remarkGfm from 'remark-gfm'

const processor = remark()
  .use(remarkGfm)
  .use(() => {
    // Register some custom extensions
    this.data('micromarkExtensions', [/* custom extensions */])
    this.data('fromMarkdownExtensions', [/* custom extensions */])
  })

const result = processor.processSync('~~strikethrough~~')
// Expected: strikethrough should be parsed correctly
// Actual: extensions are not being applied
```

### Expected behavior

When plugins register micromark or mdast extensions using `data()`, those extensions should be passed to the `fromMarkdown` function and used during parsing. The parser should respect the extensions added by plugins like `remark-gfm`.

### Additional context

This appears to have started recently. The extensions registered through the plugin system are not being picked up anymore, which breaks functionality for any plugins that rely on extending the markdown syntax.

---
Repository: /testbed
