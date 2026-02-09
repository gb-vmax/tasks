# Bug Report

### Describe the bug

The `createRedirects` option in the client-redirects plugin is not working correctly. When I provide a `createRedirects` function that returns redirect paths, the redirects are being created in the wrong direction - the "from" and "to" paths appear to be swapped.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
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
};
```

With the above config, I expect:
- Visiting `/documentation/intro` should redirect to `/docs/intro`

But instead:
- Visiting `/docs/intro` tries to redirect to `/documentation/intro` (backwards!)

### Expected behavior

The `createRedirects` function should create redirects FROM the returned paths TO the existing path. In the example above, the old path `/documentation/intro` should redirect to the new path `/docs/intro`.

### Additional context

This seems like the redirect direction got reversed somehow. The documentation clearly states that `createRedirects` should return the old paths that should redirect to the current path, but the behavior is inverted.

---
Repository: /testbed
