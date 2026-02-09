# Bug Report

### Describe the bug

The `escapeMarkdownHeadingIds` function is not properly handling heading IDs that are already escaped. When a markdown heading contains `\\{#`, the function is supposed to prevent duplicate escaping, but it's currently not working as expected.

### Reproduction

```js
const content = `
# Heading with \\{#already-escaped}
## Another heading {#needs-escaping}
`;

const result = escapeMarkdownHeadingIds(content);
// The already-escaped heading gets incorrectly modified
```

### Expected behavior

When a heading ID is already escaped (contains `\\{#`), it should remain as `\\{#` and not be escaped again. The function should only escape unescaped `{#` patterns to `\\{#`.

For example:
- `# Heading {#id}` → `# Heading \\{#id}` (correctly escaped)
- `# Heading \\{#id}` → `# Heading \\{#id}` (should remain unchanged, already escaped)

### Additional context

This seems related to the logic that's supposed to prevent duplicate escaping. The replacement pattern for `\\\\{#` back to `\\{#` doesn't appear to be functioning correctly.

---
Repository: /testbed
