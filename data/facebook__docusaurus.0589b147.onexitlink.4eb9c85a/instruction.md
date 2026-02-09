# Bug Report

### Describe the bug

I'm experiencing an issue with link parsing in markdown where regular links are being incorrectly converted to reference-type links. When I have a standard inline link like `[text](url)`, it's being treated as if it were a reference link instead of preserving the original link format.

### Reproduction

```js
// Parse a simple inline link
const markdown = '[Click here](https://example.com)';
const ast = parseMarkdown(markdown);

// Expected: link node with url property
// Actual: gets converted to Reference type incorrectly
console.log(ast.children[0].type); // Shows "Reference" instead of "link"
```

### Expected behavior

Standard inline links `[text](url)` should be parsed as regular link nodes with `url` and `title` properties intact, not converted to reference-style links. Reference links (like `[text][ref]` or `[text]`) should be the only ones getting the reference type treatment.

### Additional context

This seems to affect all inline links in my documents. The logic for determining whether a link is a reference or inline link appears to be inverted - it's doing the opposite of what it should be doing.

---
Repository: /testbed
