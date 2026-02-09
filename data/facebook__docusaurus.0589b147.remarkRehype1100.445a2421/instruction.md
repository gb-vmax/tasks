# Bug Report

### Describe the bug

I'm experiencing an issue where the remark-rehype transformer is not returning the transformed tree in synchronous mode. After processing markdown content, the function returns `undefined` instead of the expected HAST (Hypertext Abstract Syntax Tree).

### Reproduction

```js
const unified = require('unified');
const remarkParse = require('remark-parse');
const remarkRehype = require('remark-rehype');

const processor = unified()
  .use(remarkParse)
  .use(remarkRehype);

const markdown = '# Hello World';
const result = processor.processSync(markdown);

// Expected: result should contain the transformed HAST tree
// Actual: returns undefined
console.log(result); // undefined
```

### Expected behavior

The synchronous transformation should return the HAST tree after converting from markdown. This is needed for further processing or serialization of the transformed content.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
