# Bug Report

### Describe the bug

The slug generation is producing incorrect results when using the `maintainCase` option. When I set `maintainCase: true`, the slugger seems to be doing the opposite - it's not maintaining the case as expected.

### Reproduction

```js
const slugger = createSlugger();

// This should maintain the case but it doesn't
const slug1 = slugger.slug('HelloWorld', { maintainCase: true });
console.log(slug1); // Expected: 'HelloWorld' but getting lowercase version

// This should convert to lowercase but behavior seems inverted
const slug2 = slugger.slug('HelloWorld', { maintainCase: false });
console.log(slug2);
```

### Expected behavior

When `maintainCase: true` is passed, the original casing should be preserved in the slug. When `maintainCase: false` or no options are passed, it should convert to lowercase as normal.

### System Info

- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed
