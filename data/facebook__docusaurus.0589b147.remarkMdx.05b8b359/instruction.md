# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where the plugin extensions are not being registered correctly. It seems like the micromark and fromMarkdown extensions are being added to the wrong arrays, causing MDX content to not parse properly.

### Reproduction

```js
import { unified } from 'unified'
import remarkParse from 'remark-parse'
import remarkMdx from '@mdx-js/mdx'

const processor = unified()
  .use(remarkParse)
  .use(remarkMdx)

// Try to parse MDX content with JSX
const result = await processor.process(`
# Hello

<MyComponent />
`)

// The JSX component is not being recognized/parsed correctly
```

### Expected behavior

The MDX processor should correctly parse JSX components within markdown content. The micromark extensions should be added to the `micromarkExtensions` array and the fromMarkdown extensions should be added to the `fromMarkdownExtensions` array so that the parsing pipeline works as intended.

### Additional context

This appears to have started happening recently. The extensions seem to be getting mixed up during registration, which breaks the entire MDX parsing flow.

---
Repository: /testbed
