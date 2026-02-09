# Bug Report

### Describe the bug

I've noticed that the indentation in generated route files is inconsistent. When looking at the output, nested code blocks appear to have incorrect spacing - they seem to be off by one space compared to what they should be.

### Reproduction

When routes are generated, the indentation of nested elements doesn't align properly. For example:

```js
// Expected indentation (2 spaces per level):
{
  path: '/docs',
  component: Component,
  routes: [
    {
      path: '/docs/intro',
      component: Intro
    }
  ]
}

// Actual indentation (inconsistent spacing):
{
 path: '/docs',
 component: Component,
 routes: [
   {
     path: '/docs/intro',
     component: Intro
   }
 ]
}
```

The first level uses 1 space instead of 2, and subsequent newlines within the same block have 3 spaces instead of 2.

### Expected behavior

All indentation levels should use consistent 2-space indentation throughout the generated route configuration files.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
