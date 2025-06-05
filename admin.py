import streamlit as st
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.tenant import Tenant
from models.audit import AuditLog
import uuid

DATABASE_URL = "postgresql+psycopg2://user:password@host:port/dbname"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def create_tenant_schema(tenant_id: str):
    with engine.connect() as conn:
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {tenant_id}"))
        conn.execute(text(f"SET search_path TO {tenant_id}"))
        Base.metadata.create_all(bind=conn)
        conn.execute(text("RESET search_path"))

def log_audit_event(db, actor, action, entity, detail=""):
    log = AuditLog(
        id=str(uuid.uuid4()),
        actor=actor,
        action=action,
        entity=entity,
        detail=detail
    )
    db.add(log)
    db.commit()

st.title("Admin Panel – Tenant Onboarding")

admin_user = st.text_input("Admin Username")
admin_pass = st.text_input("Password", type="password")

if admin_user == "admin" and admin_pass == "letmein":
    st.success("Authenticated")

    with SessionLocal() as db:
        st.subheader("Register New Tenant")

        tenant_name = st.text_input("Tenant Name")
        if st.button("Create Tenant"):
            tenant_id = f"tenant_{uuid.uuid4().hex[:8]}"

            new_tenant = Tenant(id=tenant_id, name=tenant_name)
            db.add(new_tenant)
            db.commit()
            st.success(f"Tenant {tenant_name} added with ID {tenant_id}")

            create_tenant_schema(tenant_id)
            log_audit_event(db, actor=admin_user, action="create_tenant", entity=tenant_id, detail=tenant_name)
            st.info(f"Schema `{tenant_id}` created successfully.")
else:
    st.warning("Enter admin credentials to proceed.")
