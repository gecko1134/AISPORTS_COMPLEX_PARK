from sqlalchemy import text

def create_tenant_schema(engine, tenant_id: str, Base):
    with engine.connect() as conn:
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {tenant_id}"))
        conn.execute(text(f"SET search_path TO {tenant_id}"))
        Base.metadata.create_all(bind=conn)
        conn.execute(text("RESET search_path"))

def refresh_summary(engine, tenant_id: str):
    with engine.connect() as conn:
        conn.execute(text(f"SET search_path TO {tenant_id}"))
        conn.execute(text("REFRESH MATERIALIZED VIEW booking_summary"))
