# Bug Report

### Describe the bug

MDX files are not being parsed correctly - the remarkMdx plugin is being applied to regular Markdown files instead of MDX files. This causes standard `.md` files to be processed as if they were `.mdx` files, leading to unexpected parsing behavior.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

// Try to compile a regular markdown file
const result = await compile('# Hello World', {
  format: 'md'
})

// The markdown is incorrectly processed with MDX syntax enabled
// This can cause issues with certain markdown constructs
```

### Expected behavior

When `format` is set to `'md'`, the processor should treat the content as plain Markdown and NOT apply the `remarkMdx` plugin. The MDX plugin should only be used when the format is `'mdx'` or `'detect'` (and MDX syntax is detected).

Currently it seems like the logic is inverted - MDX processing is being applied to markdown files when it shouldn't be.

### Additional context

This also affects the `passThrough` options in `remarkRehypeOptions` - they're not being properly merged/passed through, which can cause additional issues with custom node types.

---
Repository: /testbed
