# Bug Report

### Describe the bug

The `createRedirects` option in the client redirects plugin is generating redirects with inverted `from` and `to` values. When I configure redirects using the `createRedirects` function, the redirect goes in the opposite direction than expected.

### Reproduction

```js
// In docusaurus.config.js
{
  plugins: [
    [
      '@docusaurus/plugin-client-redirects',
      {
        createRedirects(existingPath) {
          if (existingPath.includes('/docs/')) {
            return [existingPath.replace('/docs/', '/documentation/')];
          }
          return undefined;
        },
      },
    ],
  ],
}
```

With this configuration:
- I expect `/documentation/getting-started` to redirect TO `/docs/getting-started`
- But instead `/docs/getting-started` redirects TO `/documentation/getting-started` (backwards!)

### Expected behavior

When `createRedirects` returns an array of paths for a given `existingPath`, those returned paths should redirect TO the `existingPath`, not the other way around. The redirect direction should be: `returnedPath` → `existingPath`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
