# Bug Report

### Describe the bug

When using `MDXLayout` component in MDX files, the layout component is not being applied correctly. The wrapper property seems to be getting renamed incorrectly, causing the layout to not render as expected.

### Reproduction

```mdx
export const MDXLayout = MyCustomLayout

# My Content

This should be wrapped in MyCustomLayout but it's not working.
```

When the MDX file is processed, the `MDXLayout` export should be available as `wrapper` in the components object, but it appears the value is not being mapped correctly.

### Expected behavior

The `MDXLayout` component should be properly renamed to `wrapper` and applied to wrap the MDX content. The layout component should receive the page content as children and render correctly.

### Additional context

This seems to have broken recently. The MDX content renders but the custom layout wrapper is not being applied. Other component mappings work fine, it's specifically the `MDXLayout` -> `wrapper` mapping that's having issues.

---
Repository: /testbed
