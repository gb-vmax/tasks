# Bug Report

### Describe the bug
When parsing markdown links with resource destinations, the URL is not being correctly assigned to the resulting node. Instead of the link working properly, the destination string appears to be going to the wrong location or property.

### Reproduction
```js
// Parse markdown with a link that has a destination URL
const markdown = '[link text](https://example.com "title")';
const result = parse(markdown);

// The URL is not accessible where expected
console.log(result.url); // undefined or incorrect
```

### Expected behavior
The resource destination string should be properly assigned to the link node's URL property so that links can be correctly processed and rendered.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
