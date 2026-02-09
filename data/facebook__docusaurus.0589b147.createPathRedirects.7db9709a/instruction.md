# Bug Report

### Describe the bug

The `createRedirects` option in the client redirects plugin is creating redirects with swapped `from` and `to` paths. When I configure redirects, they end up pointing in the opposite direction - the source becomes the destination and vice versa.

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
            return [
              existingPath.replace('/docs/', '/documentation/'),
            ];
          }
          return undefined;
        },
      },
    ],
  ],
}
```

When I navigate to `/documentation/getting-started`, I expect it to redirect to `/docs/getting-started`. Instead, it tries to redirect from `/docs/getting-started` to `/documentation/getting-started`, which is backwards.

### Expected behavior

The redirect should go FROM the path returned by `createRedirects` TO the existing path, not the other way around. In my example, accessing `/documentation/getting-started` should redirect to `/docs/getting-started`.

### System Info

- Docusaurus version: 2.x
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
