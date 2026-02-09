# Bug Report

### Describe the bug

I'm experiencing an issue with redirect file generation in the client-redirects plugin. The redirect files are being created at incorrect paths, which causes the redirects to not work properly.

When setting up redirects, the generated HTML files end up in the wrong directory structure. It seems like the file path is being duplicated in some cases, resulting in paths that don't match the expected redirect source.

### Reproduction

Set up a redirect configuration like:

```js
redirects: [
  {
    from: '/old-page',
    to: '/new-page',
  },
]
```

After building the site, the redirect file gets created at an unexpected location. The path structure doesn't match what's specified in the `from` field, and the redirect doesn't trigger when navigating to `/old-page`.

### Expected behavior

The redirect file should be generated at the correct path based on the `from` configuration and the `trailingSlash` setting. When a user navigates to the old URL, they should be redirected to the new URL.

### Additional context

This affects both cases with and without trailing slashes. The redirect files either end up in the wrong directory or with incorrect nesting that prevents them from being served correctly by static hosting providers.

---
Repository: /testbed
