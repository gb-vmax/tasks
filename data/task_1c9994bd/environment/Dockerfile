FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

cat > /home/user/api_response.json << 'EOF'
{
  "users": [
    {
      "id": 3,
      "username": "bsmith",
      "email": "bsmith@example.com",
      "status": "active",
      "profile": {
        "first_name": "Bob",
        "last_name": "Smith",
        "department": "Marketing"
      },
      "created_at": "2024-03-10"
    },
    {
      "id": 7,
      "username": "ajones",
      "email": "ajones@example.com",
      "status": "inactive",
      "profile": {
        "first_name": "Alice",
        "last_name": "Jones",
        "department": "Sales"
      },
      "created_at": "2023-11-22"
    },
    {
      "id": 12,
      "username": "mwilliams",
      "email": "mwilliams@example.com",
      "status": "active",
      "profile": {
        "first_name": "Maria",
        "last_name": "Williams",
        "department": "Engineering"
      },
      "created_at": "2024-01-05"
    },
    {
      "id": 5,
      "username": "tlee",
      "email": "tlee@example.com",
      "status": "active",
      "profile": {
        "first_name": "Tom",
        "last_name": "Lee",
        "department": "HR"
      },
      "created_at": "2023-08-19"
    },
    {
      "id": 19,
      "username": "kpatel",
      "email": "kpatel@example.com",
      "status": "suspended",
      "profile": {
        "first_name": "Kiran",
        "last_name": "Patel",
        "department": "Engineering"
      },
      "created_at": "2024-02-28"
    },
    {
      "id": 1,
      "username": "jdoe",
      "email": "jdoe@example.com",
      "status": "active",
      "profile": {
        "first_name": "John",
        "last_name": "Doe",
        "department": "Engineering"
      },
      "created_at": "2024-01-15"
    }
  ]
}
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
