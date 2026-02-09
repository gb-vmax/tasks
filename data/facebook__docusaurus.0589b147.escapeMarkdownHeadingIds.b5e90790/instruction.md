# Bug Report

### Describe the bug

The `escapeMarkdownHeadingIds` function is not properly escaping heading IDs in markdown content. When I have headings with custom IDs using the `{#custom-id}` syntax, they are not being escaped correctly.

### Reproduction

```js
import { escapeMarkdownHeadingIds } from '@docusaurus/utils';

const markdown = `
# My Heading {#custom-id}
## Another Heading {#another-id}
`;

const result = escapeMarkdownHeadingIds(markdown);
console.log(result);
// Expected: Headings with {#...} to be escaped as \{#...\}
// Actual: The {# syntax is not escaped at all
```

### Expected behavior

Headings with custom ID syntax like `{#custom-id}` should be escaped to `\{#custom-id\}` to prevent them from being processed as heading IDs when needed.

### System Info
- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed
