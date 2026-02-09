# Bug Report

### Describe the bug

The `<head>` element in MDX files is not being transformed to `<Head>` component anymore. When I use `<head>` tags in my MDX content, they remain as lowercase `<head>` instead of being converted to the `<Head>` component.

### Reproduction

Create an MDX file with a `<head>` element:

```mdx
---
title: My Page
---

<head>
  <meta name="description" content="My page description" />
</head>

# My Content
```

The `<head>` element stays as `<head>` instead of being transformed to `<Head>`.

### Expected behavior

The `<head>` element should be automatically transformed to `<Head>` component so that meta tags and other head elements are properly handled by Docusaurus.

Previously this was working fine, but now the transformation doesn't happen and the head content doesn't get injected into the page's `<head>` section.

---
Repository: /testbed
