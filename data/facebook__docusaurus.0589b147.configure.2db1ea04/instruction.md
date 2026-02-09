# Bug Report

### Describe the bug

I'm experiencing an issue with MDX processing where extensions are not being applied correctly. It seems like the configuration is not being merged in the right order, causing some extensions to be ignored or overridden unexpectedly.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const options = {
  remarkPlugins: [plugin1, plugin2],
  rehypePlugins: [plugin3]
}

const result = await compile('# Hello', options)
```

When using multiple extensions/plugins, the later ones in the array don't seem to take effect. The first extension works fine, but subsequent ones are either skipped or applied incorrectly.

### Expected behavior

All extensions in the array should be processed and applied in order. Each plugin should be able to modify the content as expected.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
