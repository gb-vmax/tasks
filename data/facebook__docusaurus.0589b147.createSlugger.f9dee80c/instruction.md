# Bug Report

### Describe the bug

The `maintainCase` option in the slugger utility is not working as expected. When I set `maintainCase: true`, the slug output is being lowercased instead of maintaining the original casing. Conversely, when I set `maintainCase: false` or don't provide the option, the casing is being preserved.

### Reproduction

```js
import {createSlugger} from '@docusaurus/utils';

const slugger = createSlugger();

// Expected: "My-Heading" but getting "my-heading"
console.log(slugger.slug("My Heading", {maintainCase: true}));

// Expected: "my-heading" but getting "My-Heading"  
console.log(slugger.slug("My Heading", {maintainCase: false}));
```

### Expected behavior

When `maintainCase: true` is passed, the slug should preserve the original casing of the input string. When `maintainCase: false` or no option is provided, it should convert to lowercase as usual.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems like the behavior got inverted somehow. It's affecting my documentation where I need to maintain specific casing for technical terms in the URLs.

---
Repository: /testbed
