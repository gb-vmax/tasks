# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where custom `fromMarkdownExtensions` are not being applied correctly. It seems like the extensions I'm configuring aren't being picked up during the markdown-to-MDAST conversion process.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'
import { fromMarkdown } from 'mdast-util-from-markdown'

// Register a custom fromMarkdown extension
unified()
  .use(remarkParse)
  .data('fromMarkdownExtensions', [myCustomExtension])
  .parse(markdownContent)
```

When I try to parse markdown with custom `fromMarkdownExtensions` registered via the `data` method, the extensions don't seem to be applied. The parsed output is missing the transformations that my custom extension should provide.

### Expected behavior

Custom `fromMarkdownExtensions` registered through `data('fromMarkdownExtensions')` should be properly passed to the `fromMarkdown` function and applied during parsing.

### Additional context

This appears to have started recently. I have both `micromarkExtensions` and `fromMarkdownExtensions` configured, and while `micromarkExtensions` seems to work fine, the `fromMarkdownExtensions` are being ignored.

---
Repository: /testbed
