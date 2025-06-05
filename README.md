# Multi-Tenant B2B Backend for AISPORTS_COMPLEX_PARK

This project implements a schema-per-tenant architecture for a B2B SaaS application using Streamlit and PostgreSQL.

## Features

- Streamlit admin panel for onboarding tenants
- Schema-per-tenant with auto-migration
- Per-tenant analytics and dashboards
- Materialized view support for reporting
- Basic audit logging and usage tracking
- JWT-ready token infrastructure

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set your database URL as an environment variable:

```bash
export DATABASE_URL="postgresql+psycopg2://user:password@host:port/dbname"
```

3. Launch the apps:

```bash
streamlit run admin.py
streamlit run dashboard.py
```

## Test

Run the test script:

```bash
python test_db_connection.py
```

