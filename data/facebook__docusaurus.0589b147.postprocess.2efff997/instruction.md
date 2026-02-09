# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where the postprocessing step appears to be malfunctioning. After parsing MDX content, the returned events seem incorrect or incomplete, causing downstream processing to fail or produce unexpected results.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

Some content here with **bold** text.
`

const result = await compile(mdxContent)
// The compiled output is malformed or events are not properly processed
```

### Expected behavior

The MDX content should be properly parsed and postprocessed, returning valid events that can be compiled into the expected output. The postprocessing step should complete successfully and return the fully processed event stream.

### Additional context

This seems to be related to the event postprocessing logic. The parsing completes but the final output suggests that the subtokenization loop isn't working as intended. It's possible the loop termination condition or return value is incorrect.

---
Repository: /testbed
