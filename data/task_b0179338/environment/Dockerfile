FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/docs

cat > /home/user/docs/api_endpoints.txt << 'EOF'
[GET] /api/users - Retrieve list of all users
[POST] /api/users - Create a new user
[DELETE] /api/users/{id} - Remove a user by ID
[GET] /api/products - List all products
[POST] /api/products - Create a new product
[PUT] /api/products/{id} - Update a product by ID
[DELETE] /api/products/{id} - Remove a product by ID
[GET] /api/orders - List all orders
[POST] /api/orders - Place a new order
[GET] /api/orders/{id} - Retrieve a specific order
[PUT] /api/orders/{id} - Update an existing order
[GET] /api/users/{id} - Retrieve a specific user
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
