# Bug Report

### Describe the bug

After a recent update, redirect pages are not being generated correctly. The redirect functionality appears to be broken - when navigating to a redirect URL, the page either doesn't load properly or shows an error.

### Reproduction

Set up a redirect in your Docusaurus config:

```js
{
  plugins: [
    [
      '@docusaurus/plugin-client-redirects',
      {
        redirects: [
          {
            from: '/old-page',
            to: '/new-page',
          },
        ],
      },
    ],
  ],
}
```

When you navigate to `/old-page`, the redirect page template fails to render correctly. The page may show template errors or fail to redirect to the target URL.

### Expected behavior

The redirect page should be generated with the correct template data and automatically redirect users from the old URL to the new URL, preserving any search parameters and anchors if configured.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
