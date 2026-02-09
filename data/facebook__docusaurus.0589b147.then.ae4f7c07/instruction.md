# Bug Report

### Describe the bug

I'm encountering an issue with MDX processing where valid falsy values (like `0`, `false`, empty strings) are being rejected and causing errors. The processor seems to be treating these legitimate values as invalid, which breaks certain use cases.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

// This throws an error but shouldn't
const result = await compile('', { /* options */ })

// Similarly, processing that returns falsy values fails
const content = `
export const count = 0
{count}
`
await compile(content)
```

### Expected behavior

The MDX compiler should accept falsy values like `0`, `false`, and empty strings as valid outputs. These are legitimate JavaScript values and shouldn't trigger errors. Only actual error conditions should result in errors being thrown.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started after a recent change to the middleware wrapping logic. Previously these cases worked fine.

---
Repository: /testbed
