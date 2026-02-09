# Bug Report

### Describe the bug

I'm experiencing an issue where MDX parsing seems to hang indefinitely or enter an infinite loop when processing certain content. The application becomes unresponsive and never completes the parsing operation.

### Reproduction

```js
import { compile } from '@mdx-js/mdx';

const mdxContent = `
# Hello World

Some content here with **bold** text.
`;

// This call never completes and hangs indefinitely
const result = await compile(mdxContent);
```

### Expected behavior

The MDX content should be parsed and compiled successfully without hanging. The compile function should return the processed result in a reasonable amount of time.

### Additional context

This seems to have started happening recently. The parsing appears to get stuck during the postprocessing phase. When I try to compile even simple MDX documents, the process just hangs and never returns.

Any help would be appreciated!

---
Repository: /testbed
