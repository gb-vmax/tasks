# Bug Report

### Describe the bug

I'm experiencing intermittent failures when parsing MDX content. The parser seems to randomly fail or return null values during processing, which causes my application to crash or produce incorrect output.

### Reproduction

```js
// Parse MDX content multiple times
for (let i = 0; i < 10; i++) {
  const result = parseMDX(`
    # Hello World
    
    <Component />
  `);
  
  console.log(`Attempt ${i + 1}:`, result);
}
```

### Expected behavior

The MDX parser should consistently parse the same content and return valid results every time. Currently, it appears to:
- Sometimes throw an "Operation failed" error
- Sometimes return null instead of the parsed result
- Only work correctly on certain attempts

This makes the behavior completely unpredictable and breaks my build process.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
