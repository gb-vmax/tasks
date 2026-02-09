# Bug Report

### Describe the bug

I'm encountering an issue with markdown definition parsing where the parser seems to be exiting the "definition" token before it's properly processed. This causes the definition structure to be malformed in the resulting AST.

### Reproduction

```js
const markdown = `
[foo]: /url "title"

This is a reference to [foo].
`;

const result = remark.parse(markdown);
// The definition node structure is incorrect
// The exit is called too early before the definition is fully tokenized
```

### Expected behavior

The definition should be fully tokenized (including label, destination, and title) before the "definition" token is exited. The current behavior exits the definition token immediately in the `start` function, which breaks the expected token structure.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
