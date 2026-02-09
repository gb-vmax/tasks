# Bug Report

### Describe the bug

I'm experiencing an infinite recursion issue when building my Docusaurus site. The build process hangs and eventually crashes with a "Maximum call stack size exceeded" error.

### Reproduction

This happens when I have nested routes in my route configuration. The build process seems to get stuck in an infinite loop when processing routes that have subroutes.

Example route structure that triggers the issue:
```js
const routes = [
  {
    path: '/docs',
    component: DocsLayout,
    routes: [
      {
        path: '/docs/intro',
        component: IntroPage
      },
      {
        path: '/docs/tutorial',
        component: TutorialPage,
        routes: [
          {
            path: '/docs/tutorial/basics',
            component: BasicsPage
          }
        ]
      }
    ]
  }
]
```

When the site tries to process these routes during the build, it hangs indefinitely and eventually crashes.

### Expected behavior

The build should complete successfully and all nested routes should be properly flattened/processed without causing stack overflow errors.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently. Any help would be appreciated!

---
Repository: /testbed
