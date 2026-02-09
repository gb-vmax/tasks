# Bug Report

### Describe the bug

When using the `createSlugger()` function to generate slugs for headings or other content, duplicate slugs are not being handled correctly. Each call to `slug()` returns the same value even when the input is identical, instead of appending a counter suffix like `-1`, `-2`, etc.

### Reproduction

```js
const slugger = createSlugger();

const slug1 = slugger.slug('Hello World');
const slug2 = slugger.slug('Hello World');

console.log(slug1); // Expected: 'hello-world'
console.log(slug2); // Expected: 'hello-world-1', Actual: 'hello-world'
```

The slugger is supposed to keep track of previously generated slugs and automatically append a counter when duplicates are encountered, but it's not working as expected.

### Expected behavior

The slugger should maintain state across multiple calls and generate unique slugs by appending incrementing numbers when the same input is provided multiple times:
- First call: `hello-world`
- Second call: `hello-world-1`
- Third call: `hello-world-2`

This is important for generating unique IDs for table of contents or anchor links where multiple headings might have the same text.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
