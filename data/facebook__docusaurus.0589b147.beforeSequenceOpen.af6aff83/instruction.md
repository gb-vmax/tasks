# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX where the indentation/prefix calculation seems to be broken. When I have code blocks in my MDX files, they're not being parsed correctly - it appears the parser is checking for the wrong event type when determining the initial prefix length.

### Reproduction

```mdx
Some text before

```js
function example() {
  console.log('hello');
}
```

More text after
```

When processing this MDX content, the code fence parsing doesn't work as expected. The issue seems related to how the parser calculates the initial prefix length - it's looking at the wrong previous event type.

### Expected behavior

Code fences should be parsed correctly regardless of their position in the document. The parser should properly identify line prefixes when determining indentation for code blocks.

### Additional context

This appears to have started happening recently. The code fence tokenizer seems to be checking for `"codeFenced"` type in the event tail when it should be checking for `"linePrefix"` type to correctly calculate indentation.

---
Repository: /testbed
