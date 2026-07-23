import os
import streamlit as st
from supabase import create_client

# Read from Railway environment variables first
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Fall back to Streamlit secrets for local development
if not SUPABASE_URL or not SUPABASE_KEY:
    try:
        SUPABASE_URL = st.secrets["SUPABASE_URL"]
        SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
    except Exception:
        raise RuntimeError(
            "Supabase credentials not found.\n"
            "Set SUPABASE_URL and SUPABASE_KEY as Railway environment variables "
            "or create a .streamlit/secrets.toml file for local development."
        )

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
