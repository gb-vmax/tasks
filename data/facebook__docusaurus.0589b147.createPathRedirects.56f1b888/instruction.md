# Bug Report

### Describe the bug

The client redirects plugin is creating redirects with swapped `from` and `to` values. When using the `createRedirects` option, the redirects are being generated in reverse - the source path becomes the destination and the destination becomes the source.

### Reproduction

```js
// docusaurus.config.js
{
  plugins: [
    [
      '@docusaurus/plugin-client-redirects',
      {
        createRedirects(existingPath) {
          if (existingPath.includes('/docs/')) {
            return [
              existingPath.replace('/docs/', '/documentation/')
            ];
          }
          return undefined;
        },
      },
    ],
  ],
}
```

With the above configuration:
- Expected: `/documentation/intro` should redirect TO `/docs/intro`
- Actual: `/docs/intro` redirects TO `/documentation/intro` (backwards)

### Expected behavior

The `createRedirects` function should create redirects FROM the returned paths TO the existing path. In the example above, visiting `/documentation/intro` should redirect the user to `/docs/intro`, not the other way around.

The documentation states that `createRedirects` receives the existing path and should return old paths that should redirect to it, but the current behavior is inverted.

---
Repository: /testbed
