# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where the tokenizer creation logic seems to be broken. When processing MDX content, the parser fails to properly initialize tokenizers, which causes parsing errors or unexpected behavior.

### Reproduction

```js
// Create a parser with initial state
const parser = parse3(options);
const tokenCreator = parser.create4(initialState);

// This fails when 'from' parameter is provided
const tokenizer = tokenCreator(fromValue);

// Also fails when 'from' is undefined/null
const defaultTokenizer = tokenCreator();
```

### Expected behavior

The tokenizer should be created correctly regardless of whether the `from` parameter is provided or not. The parser should handle both cases gracefully and return a properly initialized tokenizer.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is blocking MDX content from being parsed correctly in my project. Any help would be appreciated!

---
Repository: /testbed
