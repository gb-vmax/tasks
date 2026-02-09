# Bug Report

### Describe the bug

The `escapeMarkdownHeadingIds` function is not correctly processing markdown headings that span multiple lines or have content after the heading ID syntax. It seems to only capture the first character after the `#` symbols instead of the entire heading line.

### Reproduction

```js
const content = `
# My Heading {#custom-id}
Some content here

## Another Heading {#another-id}
More content
`;

const escaped = escapeMarkdownHeadingIds(content);
// The heading text after the first character is lost
```

When trying to escape heading IDs in markdown content, the function appears to truncate headings or not process them fully. This affects documents with custom heading IDs that need to be escaped.

### Expected behavior

The function should process the entire heading line, not just the first character after the hash symbols. All heading content should be preserved while properly escaping the `{#` syntax to prevent MDX parsing issues.

### System Info
- Package: @docusaurus/utils
- Using the `escapeMarkdownHeadingIds` utility function

---
Repository: /testbed
