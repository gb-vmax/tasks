# Bug Report

### Describe the bug

I'm experiencing an issue with markdown heading ID escaping when the heading is at the end of a file without a trailing newline. The `escapeMarkdownHeadingIds` function doesn't properly escape heading IDs in this scenario.

### Reproduction

```js
const markdown = `# Heading {#custom-id}`;
const escaped = escapeMarkdownHeadingIds(markdown);
// Expected: "# Heading \\{#custom-id}"
// Actual: "# Heading {#custom-id}" (not escaped)
```

This also affects headings that appear at the end of content blocks:

```js
const markdown = `Some content\n\n## Another heading {#id}`;
const escaped = escapeMarkdownHeadingIds(markdown);
// The heading ID is not being escaped
```

### Expected behavior

All markdown headings with custom IDs (using the `{#id}` syntax) should have their braces properly escaped, regardless of whether they're followed by a newline or appear at the end of the content.

### Additional context

This seems to be related to how the regex pattern matches headings. Headings at the end of files or content blocks without trailing newlines are not being matched correctly.

---
Repository: /testbed
