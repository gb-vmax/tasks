# Bug Report

### Describe the bug

I'm experiencing an issue with navbar item translations in the classic theme. When I have nested navbar items (dropdown menus), the sub-items are not being translated correctly. Instead of using their own labels for translation lookup, they seem to be using the parent item's label.

### Reproduction

```js
// In my i18n translation file, I have:
{
  "item.label.Products": "Produits",
  "item.label.Product A": "Produit A",
  "item.label.Product B": "Produit B"
}

// My navbar config:
{
  type: 'dropdown',
  label: 'Products',
  items: [
    { label: 'Product A', to: '/product-a' },
    { label: 'Product B', to: '/product-b' }
  ]
}
```

### Expected behavior

The dropdown items should translate to "Produit A" and "Produit B" respectively, but they're showing up as "Products" (the parent label translation) or not translating at all.

The parent navbar item translates fine, but all the sub-items under it are broken.

### System Info
- Docusaurus version: latest
- Theme: @docusaurus/theme-classic

---
Repository: /testbed
