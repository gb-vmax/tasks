# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where custom micromark extensions aren't being applied correctly. It seems like the extensions configuration is being overridden or ignored during the markdown parsing process.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'
import { someCustomMicromarkExtension } from './my-extension'

const mdxSource = `
# Hello World

Some custom syntax that should be handled by my extension
`

const result = await compile(mdxSource, {
  remarkPlugins: [
    function() {
      const data = this.data()
      data.micromarkExtensions = data.micromarkExtensions || []
      data.micromarkExtensions.push(someCustomMicromarkExtension)
    }
  ]
})

// Custom syntax is not being parsed correctly
```

### Expected behavior

When micromark extensions are registered via the `data.micromarkExtensions` array, they should be properly passed to the `fromMarkdown` function and applied during parsing. The custom syntax should be recognized and transformed according to the extension's rules.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to have started happening recently. The extensions seem to be getting lost somewhere in the parsing pipeline.

---
Repository: /testbed
