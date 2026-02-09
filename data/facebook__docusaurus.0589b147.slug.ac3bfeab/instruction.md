# Bug Report

### Describe the bug

The slug generation behavior seems to have changed and is now producing unexpected results. When creating slugs with the `maintainCase` option, the casing is being inverted from what's expected.

### Reproduction

```js
const slugger = createSlugger();

// Expected: 'Hello-World' (with maintainCase: true)
// Actual: 'hello-world'
const slug1 = slugger.slug('Hello World', { maintainCase: true });

// Expected: 'hello-world' (with maintainCase: false)
// Actual: 'Hello-World'
const slug2 = slugger.slug('Hello World', { maintainCase: false });
```

### Expected behavior

- When `maintainCase: true` is set, the original casing should be preserved in the slug
- When `maintainCase: false` is set, the slug should be lowercased
- The behavior should match what was working in previous versions

### System Info

- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. The slug generation is working but the case handling is backwards from what the option suggests.

---
Repository: /testbed
