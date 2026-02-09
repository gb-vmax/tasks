# Bug Report

### Describe the bug

I'm encountering an issue with the `strong` element transformation in remark-rehype where the `applyData` function seems to be receiving arguments in the wrong order. This is causing data attributes and other properties to be applied incorrectly to strong elements.

### Reproduction

```js
import {unified} from 'unified'
import remarkParse from 'remark-parse'
import remarkRehype from 'remark-rehype'

const processor = unified()
  .use(remarkParse)
  .use(remarkRehype)

const markdown = '**bold text**'
const result = processor.processSync(markdown)

// The strong element doesn't have the correct data applied
console.log(result)
```

When processing markdown with strong/bold text, the resulting HTML element structure appears to have data attributes misapplied or missing entirely.

### Expected behavior

Strong elements should be transformed correctly with all data attributes and properties properly applied to the resulting HTML element node.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
