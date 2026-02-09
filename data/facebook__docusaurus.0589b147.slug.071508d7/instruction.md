# Bug Report

### Describe the bug

The slug generation behavior seems to have inverted. When I explicitly set `maintainCase: true` in the options, the slugs are being converted to lowercase instead of maintaining the original case. Similarly, when I set `maintainCase: false` or don't provide options at all, the case is being preserved when it shouldn't be.

### Reproduction

```js
const slugger = createSlugger();

// This should maintain case but doesn't
const slug1 = slugger.slug('MyTitle', { maintainCase: true });
console.log(slug1); // Expected: 'MyTitle', Actual: 'mytitle'

// This should lowercase but doesn't
const slug2 = slugger.slug('AnotherTitle', { maintainCase: false });
console.log(slug2); // Expected: 'anothertitle', Actual: 'AnotherTitle'

// Default behavior (no options) should also lowercase
const slug3 = slugger.slug('DefaultTitle');
console.log(slug3); // Expected: 'defaulttitle', Actual: 'DefaultTitle'
```

### Expected behavior

- When `maintainCase: true` is specified, the original case should be preserved in the slug
- When `maintainCase: false` is specified or no options are provided, the slug should be converted to lowercase (default behavior)

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
