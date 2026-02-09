# Bug Report

### Describe the bug

I'm encountering an issue where JavaScript files outside of `node_modules` are not being transpiled correctly by webpack. This seems to be affecting custom components and plugins that should be processed through babel-loader.

### Reproduction

When I have a project structure like this:

```
my-docusaurus-site/
├── src/
│   └── components/
│       └── MyComponent.jsx
└── node_modules/
```

The `MyComponent.jsx` file is being excluded from transpilation even though it's not in `node_modules`. This causes build errors when using modern JavaScript syntax that needs to be transpiled.

### Expected behavior

Files outside of `node_modules` (except for those in the client directory) should be transpiled by babel-loader. Only files within `node_modules` should be excluded from transpilation (with exceptions for docusaurus packages and libraries that need transpiling).

### Additional context

This seems to have broken after a recent change. Previously, my custom components were being transpiled correctly, but now they're being skipped by the babel-loader, leading to syntax errors in older browsers.

---
Repository: /testbed
