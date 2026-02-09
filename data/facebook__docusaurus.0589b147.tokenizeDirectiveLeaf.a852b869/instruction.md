# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing in remark-directive. When using leaf directives with labels (the `[label]` syntax), the parser seems to be checking for the wrong character code and fails to properly recognize the label syntax.

### Reproduction

```js
const markdown = ':directive[label text]{attr="value"}'

// Parser fails to correctly identify and parse the label portion
// The directive is not processed as expected
```

When trying to parse a leaf directive that includes a label in square brackets, the label is not being recognized correctly. It appears the parser is looking for the wrong bracket character.

### Expected behavior

The parser should correctly identify and process leaf directives with labels. The syntax `:directive[label]{attributes}` should be properly parsed with the label content extracted.

### Additional context

This affects any markdown content using leaf directives with the label syntax. The directive either fails to parse entirely or the label portion is not captured correctly.

---
Repository: /testbed
