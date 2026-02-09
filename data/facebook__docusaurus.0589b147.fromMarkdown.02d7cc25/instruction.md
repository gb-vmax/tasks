# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where the input is being processed in the wrong order. It seems like the preprocessing and postprocessing steps are happening at the wrong stages of the pipeline, which is causing unexpected behavior when parsing markdown content.

### Reproduction

```js
import { fromMarkdown } from 'remark';

const markdown = `
# Hello World

This is a test document.
`;

const result = fromMarkdown(markdown, 'utf8', options);
// The parsed output doesn't match expected structure
```

### Expected behavior

The markdown should be preprocessed first, then parsed, then postprocessed before being passed to the compiler. Currently it appears the processing order has been changed which breaks the parsing pipeline.

### Additional context

This seems to affect how the encoding parameter is passed through the pipeline as well. The preprocessing step should receive the encoding information but it's not being properly threaded through.

---
Repository: /testbed
