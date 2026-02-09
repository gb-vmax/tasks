# Bug Report

### Describe the bug

When trying to process markdown files with `format: 'md'` option, the MDX processor is incorrectly applying the MDX plugin to plain markdown files. This causes plain markdown content to be processed as MDX, which leads to unexpected behavior when the markdown contains syntax that should be valid in markdown but gets interpreted as MDX syntax.

### Reproduction

```js
const processor = createProcessor({ format: 'md' });

// Try to process plain markdown
const result = await processor.process('# Hello\n\nThis is plain markdown');

// The markdown gets processed with MDX syntax rules instead of plain markdown
```

### Expected behavior

When `format: 'md'` is specified, the processor should treat the content as plain markdown and NOT apply the MDX plugin. The MDX plugin should only be applied when the format is NOT 'md' (e.g., when it's 'mdx' or undefined).

Currently it seems like the logic is inverted - plain markdown files are being processed with MDX syntax when they shouldn't be.

### Additional context

This affects any workflow that needs to process both MDX and plain markdown files separately. The format option exists specifically to distinguish between these two cases, but it's not working as documented.

---
Repository: /testbed
