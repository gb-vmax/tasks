# Bug Report

### Describe the bug

I'm encountering an issue with the markdown serializer where extra newlines are being added to the output in situations where they shouldn't be. The generated markdown now has unexpected trailing newlines even when the content already ends with one.

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
console.log(result)
// Expected: "Hello world\n"
// Actual: "Hello world\n\n" (double newline)
```

When converting markdown AST to string, the output now contains duplicate newlines at the end. This seems to happen regardless of whether the content already ends with a newline character or not.

### Expected behavior

The serializer should only add a trailing newline when the result doesn't already end with one. Currently it appears to be adding newlines in cases where they already exist, leading to double newlines in the output.

### Additional context

This is affecting our markdown generation pipeline where we're getting extra blank lines at the end of generated files. The issue appeared recently and is causing formatting inconsistencies.

---
Repository: /testbed
