# Bug Report

### Describe the bug

I'm experiencing an issue with markdown generation where extra newlines are being added at the end of the output when they shouldn't be. The behavior seems to be inverted - newlines are being appended in cases where the content already ends with a newline character.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [{ type: 'text', value: 'Hello world' }]
    }
  ]
}

const result = toMarkdown(tree)
// Expected: "Hello world\n"
// Actual: "Hello world\n\n" (double newline)
```

When converting a markdown AST to a string, if the result already ends with a newline character (charCode 10 or 13), an additional newline is being appended. This causes double newlines in the output.

### Expected behavior

The function should only add a trailing newline if the result doesn't already end with one. Currently it seems to be doing the opposite - adding a newline when one already exists.

### Additional context

This affects any markdown content that naturally ends with a newline, resulting in unwanted extra blank lines in the generated output.

---
Repository: /testbed
