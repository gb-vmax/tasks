# Bug Report

### MDX parsing order causing unexpected behavior

I've encountered an issue with MDX processing where the order of operations seems to be causing problems with how content is being parsed.

### Reproduction

When using MDX with ESM imports and JSX components together with markdown content, the output doesn't match what's expected. It seems like the markdown processing is happening at the wrong point in the pipeline.

```mdx
import { Component } from './component'

# Hello World

<Component />

Some **markdown** text here
```

The markdown elements and JSX components aren't being processed in the correct sequence, leading to malformed output.

### Expected behavior

The MDX parser should process the content in the right order so that:
1. ESM imports are handled first
2. Markdown syntax is converted properly
3. JSX components are rendered correctly

All elements should be processed in a consistent and predictable order regardless of how they're mixed in the document.

### Additional context

This seems related to how the different MDX extensions are being combined. The processing order appears to have changed, which is affecting the final output structure.

---
Repository: /testbed
