# Bug Report

### Describe the bug

I'm experiencing an issue with the slug generation when using the `createSlugger()` function. The `maintainCase` option seems to be inverted - when I set `maintainCase: true`, the slugs are being converted to lowercase, and when I set `maintainCase: false`, the case is being preserved.

### Reproduction

```js
const slugger = createSlugger();

// Expected: "Hello-World" (case maintained)
// Actual: "hello-world" (case not maintained)
const slug1 = slugger.slug("Hello World", { maintainCase: true });

// Expected: "hello-world" (case not maintained)  
// Actual: "Hello-World" (case maintained)
const slug2 = slugger.slug("Hello World", { maintainCase: false });
```

### Expected behavior

When `maintainCase: true` is passed, the original casing should be preserved in the slug. When `maintainCase: false` or no option is passed, the slug should be converted to lowercase.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
