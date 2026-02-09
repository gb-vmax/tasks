# Bug Report

### Describe the bug

I'm encountering an issue with the MDX processor where successful file processing is being treated as an error. When I try to compile MDX content, the promise gets rejected even though the compilation succeeds.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

async function processMdx() {
  try {
    const result = await compile('# Hello World')
    console.log('Success:', result)
  } catch (error) {
    console.log('Error caught:', error)
  }
}

processMdx()
```

### Expected behavior

The promise should resolve successfully when MDX compilation completes without errors. Instead, it's being rejected even though there's no actual error.

### Additional context

This seems to affect the core processor logic. The compiled output is generated correctly but the promise handling appears to be inverted - successes are treated as failures and vice versa.

---
Repository: /testbed
