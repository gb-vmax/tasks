# Bug Report

### Describe the bug

I'm encountering an issue with object expression generation where the output appears to be incomplete or truncated. When processing MDX files with object expressions, the generated code seems to cut off mid-statement, resulting in invalid JavaScript syntax.

### Reproduction

When working with MDX content that contains object expressions with multiple properties:

```js
const obj = {
  prop1: 'value1',
  prop2: 'value2',
  prop3: 'value3'
}
```

The generated output gets corrupted and doesn't produce valid JavaScript. The object closing brace and proper formatting are missing from the output.

### Expected behavior

The object expression should be properly formatted with all properties, correct indentation, and proper closing braces. The generated JavaScript should be syntactically valid and complete.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
