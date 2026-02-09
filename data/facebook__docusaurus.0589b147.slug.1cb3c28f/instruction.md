# Bug Report

### Describe the bug

When using the slugger with `maintainCase: true` option, the generated slugs are being converted to lowercase instead of preserving the original case. The `maintainCase` option seems to be doing the opposite of what it should.

### Reproduction

```js
import {createSlugger} from '@docusaurus/utils';

const slugger = createSlugger();

// This should preserve the case but returns lowercase
const slug = slugger.slug('MyTitle', {maintainCase: true});
console.log(slug); // Expected: 'MyTitle', Actual: 'mytitle'

// This should convert to lowercase but preserves case
const slug2 = slugger.slug('AnotherTitle', {maintainCase: false});
console.log(slug2); // Expected: 'anothertitle', Actual: 'AnotherTitle'
```

### Expected behavior

When `maintainCase: true` is passed, the slug should preserve the original casing of the input string. When `maintainCase: false` or no option is provided, it should convert to lowercase as usual.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
