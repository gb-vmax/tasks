# Bug Report

### Describe the bug

The `escapeMarkdownHeadingIds` function is incorrectly escaping heading IDs that start with 7 or more `#` characters. According to Markdown spec, headings only go from `#` (h1) to `######` (h6), so lines with 7+ `#` characters shouldn't be treated as headings and their `{#id}` syntax should not be escaped.

### Reproduction

```js
const content = `
# Valid heading {#id1}
###### Also valid {#id2}
####### Not a heading {#should-not-escape}
######## Also not a heading {#also-should-not-escape}
`;

const result = escapeMarkdownHeadingIds(content);
// Currently escapes {#should-not-escape} and {#also-should-not-escape}
// but these lines are not valid markdown headings
```

### Expected behavior

Lines with 7 or more `#` characters should not be treated as markdown headings, and their `{#id}` syntax should remain unescaped. Only lines starting with 1-6 `#` characters should have their heading IDs escaped.

The function should only escape `{#id}` in actual markdown headings (h1-h6), not in text that happens to start with many `#` symbols.

---
Repository: /testbed
