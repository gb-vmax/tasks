# Bug Report

### Describe the bug

When loading a version fails in the docs plugin, the error is silently swallowed instead of being propagated. This causes the build to continue even when there are critical errors during version loading, which can lead to incomplete or broken documentation builds.

### Reproduction

```js
// In docusaurus.config.js, set up a docs plugin with invalid version configuration
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        // Configure with a version that will fail to load
        versions: {
          current: {
            path: '/nonexistent/path',
          },
        },
      },
    ],
  ],
};
```

Steps to reproduce:
1. Configure the docs plugin with a version that has an invalid path or configuration
2. Run the build
3. The error message appears in the console but the build continues
4. The build completes "successfully" but the version data is missing

### Expected behavior

When a version fails to load, the error should be thrown and the build should fail immediately. The current behavior hides critical errors and allows broken builds to complete, making it difficult to catch configuration issues in CI/CD pipelines.

The error log message appears but the build doesn't stop, which is confusing and can lead to deploying incomplete documentation.

---
Repository: /testbed
