# Bug Report

### Describe the bug

I'm experiencing an issue with code fence parsing in markdown. When I use fenced code blocks with language identifiers, the language information is not being stored correctly on the resulting AST node.

### Reproduction

```js
const markdown = '```javascript\nconsole.log("test")\n```';
const result = remark.parse(markdown);

// Expected: result should have a 'lang' property set to 'javascript'
// Actual: the 'lang' property is undefined or missing
console.log(result.children[0].lang); // undefined
console.log(result.children[0].info); // shows 'javascript' instead
```

### Expected behavior

The code fence node should have a `lang` property containing the language identifier (e.g., 'javascript', 'python', etc.). This is how it worked in previous versions and matches the expected AST structure for code blocks.

### System Info
- remark version: 15.0.1

This seems to have started happening recently. The language info appears to be getting stored in the wrong property on the node.

---
Repository: /testbed
