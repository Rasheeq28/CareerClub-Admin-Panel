# # import gspread
# # from google.oauth2.service_account import Credentials
# #
# # scopes = [
# # "https://www.googleapis.com/auth/spreadsheets"
# # ]
# #
# # creds = Credentials.from_service_account_file("credentials.toml", scopes = scopes)
# #
# # client = gspread.authorize(creds)
# #
# # sheet_id = "1QEi0D0M7Ib39W97DeaB9v69eGeLlqknkYkPoqbgolqs"
# #
# # sheet = client.open_by_key(sheet_id)
# #
# # values_list = sheet.sheet1.row_values(1)
# #
# # print(values_list)
#
#
# # loads
#
# # import streamlit as st
# # import pandas as pd
# # import gspread
# # from google.oauth2.service_account import Credentials
# #
# # # ---- Google Sheets Authentication ----
# # scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
# #
# # # Use the path to your downloaded credentials file
# # creds = Credentials.from_service_account_file("credentials.toml", scopes=scopes)
# # client = gspread.authorize(creds)
# #
# # # ---- Load Data from Google Sheet ----
# # sheet_id = "1QEi0D0M7Ib39W97DeaB9v69eGeLlqknkYkPoqbgolqs"
# # sheet = client.open_by_key(sheet_id)
# # worksheet = sheet.sheet1
# #
# #
# # @st.cache_data
# # def load_data():
# #     data = worksheet.get_all_records()
# #     df = pd.DataFrame(data)
# #     df.columns = df.columns.str.strip()  # Clean column names
# #     df["Panel"] = df["Panel"].astype(str).str.strip().str.lower()  # Clean 'Panel' column
# #     df["Name"] = df["Name"].astype(str).str.strip()  # Optional: clean name
# #     return df
# #
# #
# # # ---- Streamlit App ----
# # def main():
# #     st.set_page_config(page_title="Club Member Panel", layout="centered")
# #     st.title("Club Member Panel View")
# #
# #     df = load_data()
# #
# #     # Optional: View all unique panel names
# #     st.write("Detected Panels:", df["Panel"].unique())
# #
# #     panel_types = {
# #         "General Member": "general member",
# #         "Executive Member": "executive member",
# #         "Sub-Executive Panel": "sub-executive panel",
# #         "Executive Panel": "executive panel"
# #     }
# #
# #     tabs = st.tabs(list(panel_types.keys()))
# #
# #     for i, (label, panel_key) in enumerate(panel_types.items()):
# #         with tabs[i]:
# #             st.subheader(f"{label}")
# #             filtered_df = df[df["Panel"] == panel_key]
# #             if filtered_df.empty:
# #                 st.warning(f"No members found in '{label}' panel.")
# #             else:
# #                 st.dataframe(filtered_df[["Name"]])  # You can display more columns here if needed
# #
# #
# # if __name__ == "__main__":
# #     main()
#
#
# # promote g to e  needs to rerun
# # import streamlit as st
# # import pandas as pd
# # import gspread
# # from google.oauth2.service_account import Credentials
# #
# # # ---- Google Sheets Authentication ----
# # scopes = ["https://www.googleapis.com/auth/spreadsheets"]
# # creds = Credentials.from_service_account_file("credentials.toml", scopes=scopes)
# # client = gspread.authorize(creds)
# #
# # # ---- Load Worksheet ----
# # sheet_id = "1QEi0D0M7Ib39W97DeaB9v69eGeLlqknkYkPoqbgolqs"
# # sheet = client.open_by_key(sheet_id)
# # worksheet = sheet.sheet1
# #
# # # ---- Load Data ----
# # @st.cache_data(ttl=1)
# # def load_data():
# #     data = worksheet.get_all_records()
# #     df = pd.DataFrame(data)
# #     df.columns = df.columns.str.strip()
# #     df["Panel"] = df["Panel"].astype(str).str.strip().str.lower()
# #     df["Name"] = df["Name"].astype(str).str.strip()
# #     return df
# #
# # # ---- Update Panel in Sheet ----
# # def promote_to_executive(name):
# #     all_values = worksheet.get_all_values()
# #     header = all_values[0]
# #     panel_col_index = header.index("Panel")
# #     name_col_index = header.index("Name")
# #
# #     for idx, row in enumerate(all_values[1:], start=2):  # start=2 for 1-based indexing + header
# #         if row[name_col_index].strip() == name:
# #             worksheet.update_cell(idx, panel_col_index + 1, "Executive Member")
# #             return True
# #     return False
# #
# # # ---- Main App ----
# # def main():
# #     st.set_page_config(page_title="Club Member Panel", layout="centered")
# #     st.title("Club Member Panel Management")
# #
# #     # Only show success message after promotion
# #     if "promoted" not in st.session_state:
# #         st.session_state.promoted = False
# #
# #     df = load_data()
# #
# #     panel_types = {
# #         "General Member": "general member",
# #         "Executive Member": "executive member",
# #         "Sub-Executive Panel": "sub-executive panel",
# #         "Executive Panel": "executive panel"
# #     }
# #
# #     tabs = st.tabs(list(panel_types.keys()))
# #
# #     for i, (label, panel_key) in enumerate(panel_types.items()):
# #         with tabs[i]:
# #             st.subheader(label)
# #             filtered_df = df[df["Panel"] == panel_key]
# #             if filtered_df.empty:
# #                 st.warning(f"No members found in '{label}' panel.")
# #             else:
# #                 st.dataframe(filtered_df[["Name"]])
# #
# #                 # Promote logic for General Members only
# #                 if label == "General Member":
# #                     st.markdown("### Promote a Member")
# #                     selected_name = st.selectbox("Select a member to promote", filtered_df["Name"])
# #                     if st.button("Promote to Executive Member"):
# #                         success = promote_to_executive(selected_name)
# #                         if success:
# #                             st.session_state.promoted = True
# #                             st.experimental_rerun()
# #                         else:
# #                             st.error("Failed to promote member.")
# #
# #     if st.session_state.promoted:
# #         st.success("Member successfully promoted to Executive Member!")
# #         st.session_state.promoted = False  # reset flag
# #
# # if __name__ == "__main__":
# #     main()
#
#
# # import streamlit as st
# # import pandas as pd
# # import gspread
# # from google.oauth2.service_account import Credentials
# #
# # # Google Sheets authentication
# # scopes = ["https://www.googleapis.com/auth/spreadsheets"]
# # creds = Credentials.from_service_account_file("credentials.toml", scopes=scopes)
# # client = gspread.authorize(creds)
# # sheet_id = "1QEi0D0M7Ib39W97DeaB9v69eGeLlqknkYkPoqbgolqs"
# # sheet = client.open_by_key(sheet_id)
# # worksheet = sheet.sheet1
# #
# # # Load data from Google Sheets
# # def load_data():
# #     records = worksheet.get_all_records()
# #     df = pd.DataFrame(records)
# #     df.columns = df.columns.str.strip()
# #     df["Panel"] = df["Panel"].str.strip()
# #     return df
# #
# # # Update panel for a selected name
# # def promote_to_executive(name):
# #     cell = worksheet.find(name)
# #     if cell:
# #         panel_cell = worksheet.cell(cell.row, cell.col + 1)  # Assuming 'Panel' is next to 'Name'
# #         worksheet.update_cell(panel_cell.row, panel_cell.col, "Executive member")
# #         st.session_state["data"] = load_data()  # Refresh session data
# #
# # # Streamlit UI
# # def main():
# #     st.set_page_config(page_title="Panel Manager", layout="wide")
# #
# #     if "data" not in st.session_state:
# #         st.session_state["data"] = load_data()
# #
# #     df = st.session_state["data"]
# #     unique_panels = ["General member", "Executive member", "Sub-executive panel", "Executive panel"]
# #
# #     tabs = st.tabs(unique_panels)
# #
# #     for i, panel in enumerate(unique_panels):
# #         with tabs[i]:
# #             filtered_df = df[df["Panel"].str.lower() == panel.lower()]
# #             if filtered_df.empty:
# #                 st.warning(f"No members found in '{panel}' panel.")
# #             else:
# #                 st.subheader(f"{panel} Members")
# #                 st.dataframe(filtered_df)
# #
# #                 if panel == "General member":
# #                     names = filtered_df["Name"].tolist()
# #                     selected_name = st.selectbox("Select a general member to promote", names)
# #                     if st.button("Promote to Executive Member"):
# #                         promote_to_executive(selected_name)
# #                         st.success(f"{selected_name} has been promoted to Executive Member!")
# #
# # if __name__ == "__main__":
# #     main()
#
#


# works
# import streamlit as st
# import pandas as pd
# import gspread
# from google.oauth2.service_account import Credentials
#
# # Google Sheets authentication
# scopes = ["https://www.googleapis.com/auth/spreadsheets"]
# creds = Credentials.from_service_account_file("credentials.toml", scopes=scopes)
# client = gspread.authorize(creds)
# sheet_id = "1QEi0D0M7Ib39W97DeaB9v69eGeLlqknkYkPoqbgolqs"
# sheet = client.open_by_key(sheet_id)
# worksheet = sheet.sheet1
#
# # Load data from Google Sheets
# def load_data():
#     records = worksheet.get_all_records()
#     df = pd.DataFrame(records)
#     df.columns = df.columns.str.strip()
#     df["Panel"] = df["Panel"].str.strip()
#     return df
#
# # Promote a user and mark that data should reload
# def promote_to_executive(name):
#     cell = worksheet.find(name)
#     if cell:
#         panel_cell = worksheet.cell(cell.row, cell.col + 1)  # Assuming Panel is in next column
#         worksheet.update_cell(panel_cell.row, panel_cell.col, "Executive member")
#         st.session_state["reload_data"] = True
#         st.success(f"{name} has been promoted to Executive Member!")
#
# # Main app logic
# def main():
#     st.set_page_config(page_title="Panel Manager", layout="wide")
#
#     # Initial data load or reload flag set
#     if "data" not in st.session_state or st.session_state.get("reload_data", False):
#         st.session_state["data"] = load_data()
#         st.session_state["reload_data"] = False  # reset flag
#
#     df = st.session_state["data"]
#     unique_panels = ["General member", "Executive member", "Sub-executive panel", "Executive panel"]
#
#     tabs = st.tabs(unique_panels)
#
#     for i, panel in enumerate(unique_panels):
#         with tabs[i]:
#             filtered_df = df[df["Panel"].str.lower() == panel.lower()]
#             st.subheader(f"{panel} Members")
#
#             if filtered_df.empty:
#                 st.warning(f"No members found in '{panel}' panel.")
#             else:
#                 st.dataframe(filtered_df)
#
#                 if panel == "General member":
#                     names = filtered_df["Name"].tolist()
#                     selected_name = st.selectbox("Select a general member to promote", names)
#                     if st.button("Promote to Executive Member"):
#                         promote_to_executive(selected_name)
#
# if __name__ == "__main__":
#     main()
#
# import streamlit as st
# import pandas as pd
# import gspread
# from google.oauth2.service_account import Credentials
# import requests
# import threading
# import websocket
#
# # Setup Google Sheets API client
# scopes = ["https://www.googleapis.com/auth/spreadsheets"]
# service_account_info = st.secrets["gcp_service_account"]
# creds = Credentials.from_service_account_info(service_account_info, scopes=scopes)
# client = gspread.authorize(creds)
#
# sheet_id = "1QEi0D0M7Ib39W97DeaB9v69eGeLlqknkYkPoqbgolqs"
# sheet = client.open_by_key(sheet_id)
# worksheet = sheet.sheet1
#
# # Load data from Google Sheets
# def load_data():
#     records = worksheet.get_all_records()
#     df = pd.DataFrame(records)
#     df.columns = df.columns.str.strip()
#     df["Panel"] = df["Panel"].str.strip()
#     return df
#
# # Promote a user and notify backend
# def promote_to_executive(name):
#     cell = worksheet.find(name)
#     if cell:
#         panel_cell = worksheet.cell(cell.row, cell.col + 1)  # Assuming Panel is next column
#         worksheet.update_cell(panel_cell.row, panel_cell.col, "Executive member")
#
#         try:
#             requests.post("http://localhost:8000/notify")
#         except Exception as e:
#             st.error(f"Failed to notify backend: {e}")
#
#         st.success(f"{name} has been promoted to Executive Member!")
#
# # WebSocket listener callback function
# def on_message(ws, message):
#     if message == "update":
#         st.session_state["reload_data"] = True
#
# def on_error(ws, error):
#     print(f"WebSocket error: {error}")
#
# def on_close(ws, close_status_code, close_msg):
#     print("WebSocket closed")
#
# def on_open(ws):
#     print("WebSocket connection opened")
#
# def ws_listen():
#     ws = websocket.WebSocketApp(
#         "ws://localhost:8000/ws",
#         on_message=on_message,
#         on_error=on_error,
#         on_close=on_close,
#         on_open=on_open
#     )
#     ws.run_forever()
#
# def main():
#     st.set_page_config(page_title="Panel Manager", layout="wide")
#
#     # Start WebSocket listener thread once
#     if "ws_thread" not in st.session_state:
#         ws_thread = threading.Thread(target=ws_listen, daemon=True)
#         ws_thread.start()
#         st.session_state["ws_thread"] = ws_thread
#
#     # Reload data if flagged or first time
#     if "data" not in st.session_state or st.session_state.get("reload_data", False):
#         st.session_state["data"] = load_data()
#         st.session_state["reload_data"] = False
#
#     df = st.session_state["data"]
#     unique_panels = ["General member", "Executive member", "Sub-executive panel", "Executive panel"]
#     tabs = st.tabs(unique_panels)
#
#     for i, panel in enumerate(unique_panels):
#         with tabs[i]:
#             filtered_df = df[df["Panel"].str.lower() == panel.lower()]
#             st.subheader(f"{panel} Members")
#
#             if filtered_df.empty:
#                 st.warning(f"No members found in '{panel}' panel.")
#             else:
#                 # Drop columns where all values are 0
#                 filtered_df_nonzero = filtered_df.loc[:, (filtered_df != 0).any(axis=0)]
#                 st.dataframe(filtered_df_nonzero)
#
#                 # Promote button in General member tab
#                 if panel == "General member":
#                     names = filtered_df_nonzero["Name"].tolist()
#                     selected_name = st.selectbox("Select a general member to promote", names)
#                     if st.button("Promote to Executive Member"):
#                         promote_to_executive(selected_name)
#
#     # Manual refresh button
#     if st.button("Refresh Data"):
#         st.session_state["reload_data"] = True
#         st.success("Data reload flagged! Please refresh the page manually if needed.")
#
# if __name__ == "__main__":
#     main()

# import pandas as pd
#
# # Load the original CSV
# df = pd.read_csv(r"C:\Users\rashe\Downloads\cc - Sheet1.csv")
#
# # Add an auto-incrementing id column
# df.insert(0, 'id', range(1, len(df) + 1))
#
# # Save updated CSV (optional)
# df.to_csv("updated_cc.csv", index=False)
#
# # Upload this to Supabase or use supabase-py to upsert it
#
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from supabase import create_client
import pandas as pd
import uuid


# supabase
# from supabase import create_client, Client
# import pandas as pd
# from postgrest import APIError  # for exception handling
#
# SUPABASE_URL = "https://orjswswziiisbkvwnpye.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9yanN3c3d6aWlpc2JrdnducHllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjczNDQsImV4cCI6MjA2MzkwMzM0NH0.F2Oe53GzprWjiMYGvxMipplMwE2QeuKRRQI3Zsi7RAM"
#
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# TABLE_NAME = "cc"  # confirm exact table name here
#
# try:
#     # Fetch first 20 rows
#     response = supabase.table(TABLE_NAME).select("*").limit(20).execute()
#
#     # Print raw response data for debugging
#     print("Raw response data:", response.data)
#
#     # Convert to DataFrame
#     df = pd.DataFrame(response.data)
#
#     print("✅ First 20 rows from Supabase table:")
#     print(df)
#
# except APIError as api_err:
#     print("❌ API error:", api_err)
#
# except Exception as err:
#     print("❌ Unexpected error:", err)

#
# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
# from supabase import create_client
#
#
# # Supabase credentials
# SUPABASE_URL = "https://orjswswziiisbkvwnpye.supabase.co"
#
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9yanN3c3d6aWlpc2JrdnducHllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjczNDQsImV4cCI6MjA2MzkwMzM0NH0.F2Oe53GzprWjiMYGvxMipplMwE2QeuKRRQI3Zsi7RAM"
#
# # Initialize Supabase client
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# TABLE_NAME = "cc"  # your table name
#
#
# @st.cache_data(ttl=300)
# def fetch_data():
#     response = supabase.table(TABLE_NAME).select("*").execute()
#     data = response.data
#     return pd.DataFrame(data)
#
#
# def main():
#     st.title("Panel Members Dashboard")
#
#     df = fetch_data()
#     if df.empty:
#         st.warning("No data found in the table.")
#         return
#
#     # Get unique panels as list
#     panels = df['Panel'].unique().tolist()
#
#     # Create tabs for each panel
#     tabs = st.tabs(panels)
#
#     for tab, panel in zip(tabs, panels):
#         with tab:
#             st.header(f"Members of Panel: {panel}")
#             panel_df = df[df['Panel'] == panel]
#             st.dataframe(panel_df)
#
#
# if __name__ == "__main__":
#     main()


# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
#
# # Supabase credentials
# SUPABASE_URL = "https://orjswswziiisbkvwnpye.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9yanN3c3d6aWlpc2JrdnducHllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjczNDQsImV4cCI6MjA2MzkwMzM0NH0.F2Oe53GzprWjiMYGvxMipplMwE2QeuKRRQI3Zsi7RAM"  # Replace with actual key
#
# # Initialize Supabase client
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# # Fetch all member data
# response = supabase.table("cc").select("*").execute()
# df = pd.DataFrame(response.data)
#
# # Normalize panel names to lowercase (strip spaces too)
# df["Panel"] = df["Panel"].str.strip().str.lower()
#
# # Define the 4 known/expected panels (in lowercase)
# expected_panels = {
#     "executive panel": "Executive Panel",
#     "sub-executive panel": "Sub-executive Panel",
#     "executive member": "Executive Member",
#     "general member": "General Member",
# }
#
# # Filter dataframe to keep only valid panels
# df = df[df["Panel"].isin(expected_panels.keys())]
#
# # Create Streamlit tabs for the 4 panels
# st.title("🔍 Member Dashboard by Panel")
#
# tabs = st.tabs(list(expected_panels.values()))
#
# for i, (panel_key, panel_display) in enumerate(expected_panels.items()):
#     with tabs[i]:
#         st.subheader(panel_display)
#         panel_members = df[df["Panel"] == panel_key]
#         st.write(panel_members.reset_index(drop=True))

# supabase load
# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
# from postgrest import APIError
#
# # Supabase setup
# SUPABASE_URL = "https://orjswswziiisbkvwnpye.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9yanN3c3d6aWlpc2JrdnducHllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjczNDQsImV4cCI6MjA2MzkwMzM0NH0.F2Oe53GzprWjiMYGvxMipplMwE2QeuKRRQI3Zsi7RAM"
# TABLE_NAME = "cc"
#
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# # Fetch data
# try:
#     response = supabase.table(TABLE_NAME).select("*").execute()
#     df = pd.DataFrame(response.data)
# except APIError as e:
#     st.error(f"❌ Supabase API Error: {e}")
#     st.stop()
# except Exception as e:
#     st.error(f"❌ Unexpected error: {e}")
#     st.stop()
#
# # Ensure required column exists
# if "Panel" not in df.columns:
#     st.error("Missing 'Panel' column in your data.")
#     st.stop()
#
# # Clean 'Panel' column
# df["Panel"] = df["Panel"].astype(str).str.strip().str.lower()
#
# # Map original Panel values to user-friendly display names
# panel_labels = {
#     "executive panel": "Executive Panel",
#     "sub-executive panel": "Sub-Executive Panel",
#     "executive member": "Executive Member",
#     "general member": "General Member"
# }
#
# # Create Streamlit tabs
# tabs = st.tabs(list(panel_labels.values()))
#
# for tab, (raw_label, display_label) in zip(tabs, panel_labels.items()):
#     with tab:
#         panel_df = df[df["Panel"] == raw_label]
#
#         if panel_df.empty:
#             st.info(f"No members in {display_label}.")
#             continue
#
#         # Remove columns that contain only 0 or "0"
#         def is_all_zero(series):
#             return ((series.astype(str).str.strip() == "0") | (series == 0)).all()
#
#         filtered_df = panel_df.loc[:, ~panel_df.apply(is_all_zero)]
#
#         st.subheader(f"{display_label} Members")
#         st.dataframe(filtered_df.reset_index(drop=True))


# g-e promo
# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
# from postgrest import APIError
# import time
#
# # Supabase config
# SUPABASE_URL = "https://orjswswziiisbkvwnpye.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9yanN3c3d6aWlpc2JrdnducHllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjczNDQsImV4cCI6MjA2MzkwMzM0NH0.F2Oe53GzprWjiMYGvxMipplMwE2QeuKRRQI3Zsi7RAM"
# TABLE_NAME = "cc"
#
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# def fetch_data():
#     try:
#         response = supabase.table(TABLE_NAME).select("*").execute()
#         return pd.DataFrame(response.data)
#     except Exception as e:
#         st.error(f"Error fetching data: {e}")
#         return pd.DataFrame()
#
# def promote_member(row_id):
#     try:
#         supabase.table(TABLE_NAME).update({"Panel": "executive member"}).eq("id", row_id).execute()
#         st.success("🎉 Member promoted to Executive Member!")
#         time.sleep(1)
#         st.rerun()
#
#     except Exception as e:
#         st.error(f"Failed to promote: {e}")
#
# # Fetch data
# df = fetch_data()
#
# if "Panel" not in df.columns:
#     st.error("Missing 'Panel' column.")
#     st.stop()
#
# df["Panel"] = df["Panel"].astype(str).str.strip()
#
# panel_labels = {
#     "executive panel": "Executive Panel",
#     "sub-executive panel": "Sub-Executive Panel",
#     "executive member": "Executive Member",
#     "general member": "General Member"
# }
#
# tabs = st.tabs(list(panel_labels.values()))
#
# for tab, (raw_label, display_label) in zip(tabs, panel_labels.items()):
#     with tab:
#         panel_df = df[df["Panel"] == raw_label]
#
#         if panel_df.empty:
#             st.info(f"No members in {display_label}.")
#             continue
#
#         # Remove all-zero columns for display tabs
#         def is_all_zero(series):
#             return ((series.astype(str).str.strip() == "0") | (series == 0)).all()
#
#         filtered_df = panel_df.loc[:, ~panel_df.apply(is_all_zero)]
#
#         st.subheader(f"{display_label} Members")
#
#         if raw_label == "general member":
#             for _, row in filtered_df.iterrows():
#                 cols = st.columns([3, 3, 1])
#                 cols[0].markdown(f"**Name:** {row.get('Name', 'N/A')}")
#                 cols[1].markdown(f"**Panel:** {row.get('Panel', 'N/A').title()}")
#                 if st.button("Promote", key=f"promote_{row['id']}"):
#                     promote_member(row["id"])
#         else:
#             st.dataframe(filtered_df.reset_index(drop=True))

#
# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
# import time
#
# # Supabase config
# SUPABASE_URL = "https://orjswswziiisbkvwnpye.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9yanN3c3d6aWlpc2JrdnducHllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjczNDQsImV4cCI6MjA2MzkwMzM0NH0.F2Oe53GzprWjiMYGvxMipplMwE2QeuKRRQI3Zsi7RAM"
# TABLE_NAME = "cc"
#
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# def fetch_data():
#     try:
#         response = supabase.table(TABLE_NAME).select("*").execute()
#         return pd.DataFrame(response.data)
#     except Exception as e:
#         st.error(f"Error fetching data: {e}")
#         return pd.DataFrame()
#
# def promote_member(row_id):
#     try:
#         st.write(f"Promoting ID: {row['id']}")
#         st.write(row.to_dict())
#
#         response = supabase.table(TABLE_NAME).update({
#             "Panel": "executive member"
#         }).eq("id", row_id).execute()
#
#         if response.data:
#             st.success("🎉 Member promoted to Executive Member!")
#             time.sleep(1)
#             st.rerun()
#         else:
#             st.warning("⚠️ Promotion failed — no rows updated.")
#     except Exception as e:
#         st.error(f"❌ Failed to promote: {e}")
#
#
#
# # Fetch data
# df = fetch_data()
#
# if "Panel" not in df.columns:
#     st.error("Missing 'Panel' column.")
#     st.stop()
#
# # Clean whitespace, keep original casing
# df["Panel"] = df["Panel"].astype(str).str.strip()
#
# # Use Supabase's exact values as keys, readable titles as values
# panel_labels = {
#     "Executive panel": "Executive Panel",
#     "Sub-executive panel": "Sub-Executive Panel",
#     "executive member": "Executive Member",
#     "general member": "General Member"
# }
#
# tabs = st.tabs(list(panel_labels.values()))
#
# for tab, (raw_label, display_label) in zip(tabs, panel_labels.items()):
#     with tab:
#         panel_df = df[df["Panel"] == raw_label]
#
#         if panel_df.empty:
#             st.info(f"No members in {display_label}.")
#             continue
#
#         # Remove all-zero columns
#         def is_all_zero(series):
#             return ((series.astype(str).str.strip() == "0") | (series == 0)).all()
#
#         filtered_df = panel_df.loc[:, ~panel_df.apply(is_all_zero)]
#
#         st.subheader(f"{display_label} Members")
#
#         if raw_label == "general member":
#             for _, row in filtered_df.iterrows():
#                 cols = st.columns([3, 3, 1])
#                 cols[0].markdown(f"**Name:** {row.get('Name', 'N/A')}")
#                 cols[1].markdown(f"**Panel:** {row.get('Panel', 'N/A')}")
#                 if cols[2].button("Promote", key=f"promote_{row['id']}"):
#                     promote_member(row["id"])
#         else:
#             st.dataframe(filtered_df.reset_index(drop=True))



# workssss promo from gen to exec
# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
# import time
#
# # Supabase config
# SUPABASE_URL = "https://orjswswziiisbkvwnpye.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9yanN3c3d6aWlpc2JrdnducHllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjczNDQsImV4cCI6MjA2MzkwMzM0NH0.F2Oe53GzprWjiMYGvxMipplMwE2QeuKRRQI3Zsi7RAM"
# TABLE_NAME = "cc"
#
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# def fetch_data():
#     try:
#         response = supabase.table(TABLE_NAME).select("*").execute()
#         return pd.DataFrame(response.data)
#     except Exception as e:
#         st.error(f"Error fetching data: {e}")
#         return pd.DataFrame()
#
# def promote_member(row_id):
#     try:
#         # Confirm ID is string (important for UUID)
#         row_id = str(row_id)
#
#         # Run update
#         response = supabase.table(TABLE_NAME).update({
#             "Panel": "executive member"
#         }).eq("id", row_id).execute()
#
#         if response.data and len(response.data) > 0:
#             st.success("🎉 Member promoted to Executive Member!")
#             time.sleep(1)
#             st.rerun()
#         else:
#             st.warning(f"⚠️ Promotion failed — no rows updated. ID: {row_id}")
#     except Exception as e:
#         st.error(f"❌ Failed to promote: {e}")
#
#
# # Fetch data
# df = fetch_data()
#
# if "Panel" not in df.columns:
#     st.error("Missing 'Panel' column.")
#     st.stop()
#
# # Clean whitespace
# df["Panel"] = df["Panel"].astype(str).str.strip()
#
# # Panel labels mapping
# panel_labels = {
#     "Executive panel": "Executive Panel",
#     "Sub-executive panel": "Sub-Executive Panel",
#     "executive member": "Executive Member",
#     "general member": "General Member"
# }
#
# tabs = st.tabs(list(panel_labels.values()))
#
# for tab, (raw_label, display_label) in zip(tabs, panel_labels.items()):
#     with tab:
#         panel_df = df[df["Panel"] == raw_label]
#
#         if panel_df.empty:
#             st.info(f"No members in {display_label}.")
#             continue
#
#         # Remove all-zero columns
#         def is_all_zero(series):
#             return ((series.astype(str).str.strip() == "0") | (series == 0)).all()
#
#         filtered_df = panel_df.loc[:, ~panel_df.apply(is_all_zero)]
#
#         st.subheader(f"{display_label} Members")
#
#         if raw_label == "general member":
#             for _, row in filtered_df.iterrows():
#                 cols = st.columns([3, 3, 1])
#                 cols[0].markdown(f"**Name:** {row.get('Name', 'N/A')}")
#                 cols[1].markdown(f"**Panel:** {row.get('Panel', 'N/A')}")
#                 if cols[2].button("Promote", key=f"promote_{row['id']}"):
#                     promote_member(row["id"])
#
#         else:
#             st.dataframe(filtered_df.reset_index(drop=True))
#

# demote exec to gen
# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
# import time
#
# # Supabase config
# SUPABASE_URL = "https://orjswswziiisbkvwnpye.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9yanN3c3d6aWlpc2JrdnducHllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjczNDQsImV4cCI6MjA2MzkwMzM0NH0.F2Oe53GzprWjiMYGvxMipplMwE2QeuKRRQI3Zsi7RAM"
# TABLE_NAME = "cc"
#
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# def fetch_data():
#     try:
#         response = supabase.table(TABLE_NAME).select("*").execute()
#         return pd.DataFrame(response.data)
#     except Exception as e:
#         st.error(f"Error fetching data: {e}")
#         return pd.DataFrame()
#
# def promote_member(row_id):
#     try:
#         row_id = str(row_id)
#         response = supabase.table(TABLE_NAME).update({
#             "Panel": "executive member"
#         }).eq("id", row_id).execute()
#
#         if response.data and len(response.data) > 0:
#             st.success("🎉 Member promoted to Executive Member!")
#             time.sleep(1)
#             st.rerun()
#         else:
#             st.warning(f"⚠️ Promotion failed — no rows updated. ID: {row_id}")
#     except Exception as e:
#         st.error(f"❌ Failed to promote: {e}")
#
# def demote_member(row_id):
#     try:
#         row_id = str(row_id)
#         response = supabase.table(TABLE_NAME).update({
#             "Panel": "general member"
#         }).eq("id", row_id).execute()
#
#         if response.data and len(response.data) > 0:
#             st.success("👋 Member demoted to General Member.")
#             time.sleep(1)
#             st.rerun()
#         else:
#             st.warning(f"⚠️ Demotion failed — no rows updated. ID: {row_id}")
#     except Exception as e:
#         st.error(f"❌ Failed to demote: {e}")
#
# # Fetch data
# df = fetch_data()
#
# if "Panel" not in df.columns:
#     st.error("Missing 'Panel' column.")
#     st.stop()
#
# df["Panel"] = df["Panel"].astype(str).str.strip()
#
# panel_labels = {
#     "Executive panel": "Executive Panel",
#     "Sub-executive panel": "Sub-Executive Panel",
#     "executive member": "Executive Member",
#     "general member": "General Member"
# }
#
# tabs = st.tabs(list(panel_labels.values()))
#
# for tab, (raw_label, display_label) in zip(tabs, panel_labels.items()):
#     with tab:
#         panel_df = df[df["Panel"] == raw_label]
#
#         if panel_df.empty:
#             st.info(f"No members in {display_label}.")
#             continue
#
#         def is_all_zero(series):
#             return ((series.astype(str).str.strip() == "0") | (series == 0)).all()
#
#         filtered_df = panel_df.loc[:, ~panel_df.apply(is_all_zero)]
#
#         st.subheader(f"{display_label} Members")
#
#         if raw_label == "general member":
#             for _, row in filtered_df.iterrows():
#                 with st.container():
#                     st.markdown(
#                         f"""
#                         **Name:** {row.get('Name', 'N/A')}
#                         **Panel:** {row.get('Panel', 'N/A')}
#                         **FB ID:** {row.get('FB ID', 'N/A')}
#                         **LinkedIn ID:** {row.get('LinkedIn ID', 'N/A')}
#                         """
#                     )
#                     if st.button("🎯 Promote to Executive", key=f"promote_{row['id']}"):
#                         promote_member(row["id"])
#                     st.markdown("---")
#
#         elif raw_label == "executive member":
#             for _, row in filtered_df.iterrows():
#                 with st.container():
#                     st.markdown(
#                         f"""
#                         **Name:** {row.get('Name', 'N/A')}
#                         **Panel:** {row.get('Panel', 'N/A')}
#                         **FB ID:** {row.get('FB ID', 'N/A')}
#                         **LinkedIn ID:** {row.get('LinkedIn ID', 'N/A')}
#                         """
#                     )
#                     if st.button("↩️ Demote to General", key=f"demote_{row['id']}"):
#                         demote_member(row["id"])
#                     st.markdown("---")

# linkedin fb
# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
# import time
#
# # Supabase config
# SUPABASE_URL = "https://orjswswziiisbkvwnpye.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9yanN3c3d6aWlpc2JrdnducHllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjczNDQsImV4cCI6MjA2MzkwMzM0NH0.F2Oe53GzprWjiMYGvxMipplMwE2QeuKRRQI3Zsi7RAM"
# TABLE_NAME = "cc"
#
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# def fetch_data():
#     try:
#         response = supabase.table(TABLE_NAME).select("*").execute()
#         return pd.DataFrame(response.data)
#     except Exception as e:
#         st.error(f"Error fetching data: {e}")
#         return pd.DataFrame()
#
# def promote_member(row_id):
#     try:
#         row_id = str(row_id)
#         response = supabase.table(TABLE_NAME).update({"Panel": "executive member"}).eq("id", row_id).execute()
#         if response.data and len(response.data) > 0:
#             st.success("🎉 Member promoted to Executive Member!")
#             time.sleep(1)
#             # st.experimental_rerun()  <-- remove or comment out
#         else:
#             st.warning(f"⚠️ Promotion failed — no rows updated. ID: {row_id}")
#     except Exception as e:
#         st.error(f"❌ Failed to promote: {e}")
#
# def demote_member(row_id):
#     try:
#         row_id = str(row_id)
#         response = supabase.table(TABLE_NAME).update({"Panel": "general member"}).eq("id", row_id).execute()
#         if response.data and len(response.data) > 0:
#             st.success("👋 Member demoted to General Member.")
#             time.sleep(1)
#             # st.experimental_rerun()  <-- remove or comment out
#         else:
#             st.warning(f"⚠️ Demotion failed — no rows updated. ID: {row_id}")
#     except Exception as e:
#         st.error(f"❌ Failed to demote: {e}")
#
#
# # Fetch data
# df = fetch_data()
#
# if "Panel" not in df.columns:
#     st.error("Missing 'Panel' column.")
#     st.stop()
#
# df["Panel"] = df["Panel"].astype(str).str.strip()
#
# panel_labels = {
#     "Executive panel": "Executive Panel",
#     "Sub-executive panel": "Sub-Executive Panel",
#     "executive member": "Executive Member",
#     "general member": "General Member"
# }
#
# tabs = st.tabs(list(panel_labels.values()))
#
# # ... same imports and setup above ...
#
# for tab, (raw_label, display_label) in zip(tabs, panel_labels.items()):
#     with tab:
#         panel_df = df[df["Panel"] == raw_label]
#
#         if panel_df.empty:
#             st.info(f"No members in {display_label}.")
#             continue
#
#         def is_all_zero(series):
#             return ((series.astype(str).str.strip() == "0") | (series == 0)).all()
#
#         filtered_df = panel_df.loc[:, ~panel_df.apply(is_all_zero)]
#
#         st.subheader(f"{display_label} Members")
#
#         if raw_label == "general member":
#             for _, row in filtered_df.iterrows():
#                 cols = st.columns([3, 3, 3, 3, 1])
#                 cols[0].markdown(f"**Name:** {row.get('Name', 'N/A')}")
#                 cols[1].markdown(f"**Panel:** {row.get('Panel', 'N/A')}")
#                 cols[2].markdown(f"**fb id:** {row.get('fb id', 'N/A')}")
#                 cols[3].markdown(f"**linkedin id:** {row.get('linkedin id', 'N/A')}")
#                 if cols[4].button("Promote", key=f"promote_{row['id']}"):
#                     promote_member(row["id"])
#
#         elif raw_label == "executive member":
#             for _, row in filtered_df.iterrows():
#                 cols = st.columns([3, 3, 3, 3, 1])
#                 cols[0].markdown(f"**Name:** {row.get('Name', 'N/A')}")
#                 cols[1].markdown(f"**Panel:** {row.get('Panel', 'N/A')}")
#                 cols[2].markdown(f"**fb id:** {row.get('fb id', 'N/A')}")
#                 cols[3].markdown(f"**linkedin id:** {row.get('linkedin id', 'N/A')}")
#                 if cols[4].button("Demote", key=f"demote_{row['id']}"):
#                     demote_member(row["id"])
#         else:
#             st.dataframe(filtered_df.reset_index(drop=True))
# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
# import time
#
# # Supabase config
# SUPABASE_URL = "https://orjswswziiisbkvwnpye.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9yanN3c3d6aWlpc2JrdnducHllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjczNDQsImV4cCI6MjA2MzkwMzM0NH0.F2Oe53GzprWjiMYGvxMipplMwE2QeuKRRQI3Zsi7RAM"
# TABLE_NAME = "cc"
#
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# def fetch_data():
#     try:
#         response = supabase.table(TABLE_NAME).select("*").execute()
#         return pd.DataFrame(response.data)
#     except Exception as e:
#         st.error(f"Error fetching data: {e}")
#         return pd.DataFrame()
#
# def promote_member(row_id):
#     try:
#         row_id = str(row_id)
#         response = supabase.table(TABLE_NAME).update({"Panel": "executive member"}).eq("id", row_id).execute()
#         if response.data and len(response.data) > 0:
#             st.success("🎉 Member promoted to Executive Member!")
#             time.sleep(1)
#         else:
#             st.warning(f"⚠️ Promotion failed — no rows updated. ID: {row_id}")
#     except Exception as e:
#         st.error(f"❌ Failed to promote: {e}")
#
# def demote_member(row_id):
#     try:
#         row_id = str(row_id)
#         response = supabase.table(TABLE_NAME).update({"Panel": "general member"}).eq("id", row_id).execute()
#         if response.data and len(response.data) > 0:
#             st.success("👋 Member demoted to General Member.")
#             time.sleep(1)
#         else:
#             st.warning(f"⚠️ Demotion failed — no rows updated. ID: {row_id}")
#     except Exception as e:
#         st.error(f"❌ Failed to demote: {e}")
#
# # Fetch data
# df = fetch_data()
#
# if "Panel" not in df.columns:
#     st.error("Missing 'Panel' column.")
#     st.stop()
#
# df["Panel"] = df["Panel"].astype(str).str.strip()
#
# panel_labels = {
#     "Executive panel": "Executive Panel",
#     "Sub-executive panel": "Sub-Executive Panel",
#     "executive member": "Executive Member",
#     "general member": "General Member"
# }
#
# tabs = st.tabs(list(panel_labels.values()))
#
# for tab, (raw_label, display_label) in zip(tabs, panel_labels.items()):
#     with tab:
#         panel_df = df[df["Panel"] == raw_label]
#
#         if panel_df.empty:
#             st.info(f"No members in {display_label}.")
#             continue
#
#         st.subheader(f"{display_label} Members")
#
#         # Select columns to show
#         display_cols = ["Name", "Panel", "fb id", "linkedin id"]
#
#         # Display dataframe neatly
#         st.dataframe(panel_df[display_cols].reset_index(drop=True))
#
#         # Action buttons only for "general member" and "executive member"
#         if raw_label in ["general member", "executive member"]:
#             for idx, row in panel_df.iterrows():
#                 cols = st.columns([4, 1])
#                 cols[0].markdown(f"**{row['Name']}**")
#                 if raw_label == "general member":
#                     if cols[1].button("Promote", key=f"promote_{row['id']}"):
#                         promote_member(row["id"])
#                         st.info("Please refresh the page to see updates.")
#                 elif raw_label == "executive member":
#                     if cols[1].button("Demote", key=f"demote_{row['id']}"):
#                         demote_member(row["id"])
#                         st.info("Please refresh the page to see updates.")
# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
#
# # Supabase config
# SUPABASE_URL = "https://orjswswziiisbkvwnpye.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9yanN3c3d6aWlpc2JrdnducHllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjczNDQsImV4cCI6MjA2MzkwMzM0NH0.F2Oe53GzprWjiMYGvxMipplMwE2QeuKRRQI3Zsi7RAM"
# TABLE_NAME = "cc"
#
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# def fetch_data():
#     try:
#         response = supabase.table(TABLE_NAME).select("*").execute()
#         return pd.DataFrame(response.data)
#     except Exception as e:
#         st.error(f"Error fetching data: {e}")
#         return pd.DataFrame()
#
# def promote_member(row_id):
#     row_id = str(row_id)
#     response = supabase.table(TABLE_NAME).update({"Panel": "executive member"}).eq("id", row_id).execute()
#     if response.data and len(response.data) > 0:
#         st.success("🎉 Member promoted to Executive Member!")
#         st.session_state['needs_refresh'] = True
#     else:
#         st.warning(f"⚠️ Promotion failed — no rows updated. ID: {row_id}")
#
# def demote_member(row_id):
#     row_id = str(row_id)
#     response = supabase.table(TABLE_NAME).update({"Panel": "general member"}).eq("id", row_id).execute()
#     if response.data and len(response.data) > 0:
#         st.success("👋 Member demoted to General Member.")
#         st.session_state['needs_refresh'] = True
#     else:
#         st.warning(f"⚠️ Demotion failed — no rows updated. ID: {row_id}")
#
# # Initialize flag
# if 'needs_refresh' not in st.session_state:
#     st.session_state['needs_refresh'] = False
#
# # Your UI and button logic here...
#
# # After all UI code but still top-level:
# if st.session_state['needs_refresh']:
#     st.session_state['needs_refresh'] = False
#     st.experimental_rerun()
#
#
# # Fetch data
# df = fetch_data()
#
# if "Panel" not in df.columns:
#     st.error("Missing 'Panel' column.")
#     st.stop()
#
# df["Panel"] = df["Panel"].astype(str).str.strip()
#
# panel_labels = {
#     "Executive panel": "Executive Panel",
#     "Sub-executive panel": "Sub-Executive Panel",
#     "executive member": "Executive Member",
#     "general member": "General Member"
# }
#
# tabs = st.tabs(list(panel_labels.values()))
#
# for tab, (raw_label, display_label) in zip(tabs, panel_labels.items()):
#     with tab:
#         panel_df = df[df["Panel"] == raw_label]
#
#         if panel_df.empty:
#             st.info(f"No members in {display_label}.")
#             continue
#
#         display_cols = ["Name", "Panel", "fb id", "linkedin id"]
#
#         st.subheader(f"{display_label} Members")
#
#         # Show data table
#         st.dataframe(panel_df[display_cols].reset_index(drop=True))
#
#         # Buttons only for general/executive members
#         if raw_label in ["general member", "executive member"]:
#             st.markdown("---")
#             for idx, row in panel_df.iterrows():
#                 cols = st.columns([4, 1])
#                 cols[0].markdown(f"**{row['Name']}**")
#                 if raw_label == "general member":
#                     if cols[1].button("Promote", key=f"promote_{row['id']}"):
#                         promote_member(row["id"])
#                 elif raw_label == "executive member":
#                     if cols[1].button("Demote", key=f"demote_{row['id']}"):
#                         demote_member(row["id"])


# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
# import time
#
# # Supabase config
# SUPABASE_URL = "https://orjswswziiisbkvwnpye.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9yanN3c3d6aWlpc2JrdnducHllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjczNDQsImV4cCI6MjA2MzkwMzM0NH0.F2Oe53GzprWjiMYGvxMipplMwE2QeuKRRQI3Zsi7RAM"
# TABLE_NAME = "cc"
#
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# def fetch_data():
#     try:
#         response = supabase.table(TABLE_NAME).select("*").execute()
#         return pd.DataFrame(response.data)
#     except Exception as e:
#         st.error(f"Error fetching data: {e}")
#         return pd.DataFrame()
#
# def promote_member(row_id):
#     try:
#         row_id = str(row_id)
#         response = supabase.table(TABLE_NAME).update({
#             "Panel": "executive member"
#         }).eq("id", row_id).execute()
#
#         if response.data and len(response.data) > 0:
#             st.success("🎉 Member promoted to Executive Member!")
#             time.sleep(1)
#             st.rerun()
#         else:
#             st.warning(f"⚠️ Promotion failed — no rows updated. ID: {row_id}")
#     except Exception as e:
#         st.error(f"❌ Failed to promote: {e}")
#
# def demote_member(row_id):
#     try:
#         row_id = str(row_id)
#         response = supabase.table(TABLE_NAME).update({
#             "Panel": "general member"
#         }).eq("id", row_id).execute()
#
#         if response.data and len(response.data) > 0:
#             st.success("👋 Member demoted to General Member.")
#             time.sleep(1)
#             st.rerun()
#         else:
#             st.warning(f"⚠️ Demotion failed — no rows updated. ID: {row_id}")
#     except Exception as e:
#         st.error(f"❌ Failed to demote: {e}")
#
# # Fetch data
# df = fetch_data()
#
# if "Panel" not in df.columns:
#     st.error("Missing 'Panel' column.")
#     st.stop()
#
# df["Panel"] = df["Panel"].astype(str).str.strip()
#
# panel_labels = {
#     "Executive panel": "Executive Panel",
#     "Sub-executive panel": "Sub-Executive Panel",
#     "executive member": "Executive Member",
#     "general member": "General Member"
# }
#
# tabs = st.tabs(list(panel_labels.values()))
#
# for tab, (raw_label, display_label) in zip(tabs, panel_labels.items()):
#     with tab:
#         panel_df = df[df["Panel"] == raw_label]
#
#         if panel_df.empty:
#             st.info(f"No members in {display_label}.")
#             continue
#
#         def is_all_zero(series):
#             return ((series.astype(str).str.strip() == "0") | (series == 0)).all()
#
#         filtered_df = panel_df.loc[:, ~panel_df.apply(is_all_zero)]
#
#         st.subheader(f"{display_label} Members")
#
#         if raw_label == "general member":
#             for _, row in filtered_df.iterrows():
#                 with st.container():
#                     st.markdown(
#                         f"""
#                         **Name:** {row.get('Name', 'N/A')}
#                         **Panel:** {row.get('Panel', 'N/A')}
#                         **FB ID:** {row.get('FB ID', 'N/A')}
#                         **LinkedIn ID:** {row.get('LinkedIn ID', 'N/A')}
#                         """
#                     )
#                     if st.button("🎯 Promote to Executive", key=f"promote_{row['id']}"):
#                         promote_member(row["id"])
#                     st.markdown("---")
#
#         elif raw_label == "executive member":
#             for _, row in filtered_df.iterrows():
#                 with st.container():
#                     st.markdown(
#                         f"""
#                         **Name:** {row.get('Name', 'N/A')}
#                         **Panel:** {row.get('Panel', 'N/A')}
#                         **FB ID:** {row.get('FB ID', 'N/A')}
#                         **LinkedIn ID:** {row.get('LinkedIn ID', 'N/A')}
#                         """
#                     )
#                     if st.button("↩️ Demote to General", key=f"demote_{row['id']}"):
#                         demote_member(row["id"])
#                     st.markdown("---")


# add button
# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
# import uuid
# import time
#
# # Supabase config
# SUPABASE_URL = "https://orjswswziiisbkvwnpye.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9yanN3c3d6aWlpc2JrdnducHllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjczNDQsImV4cCI6MjA2MzkwMzM0NH0.F2Oe53GzprWjiMYGvxMipplMwE2QeuKRRQI3Zsi7RAM"
# TABLE_NAME = "cc"
#
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# # Fetch existing data
# def fetch_data():
#     try:
#         response = supabase.table(TABLE_NAME).select("*").execute()
#         return pd.DataFrame(response.data)
#     except Exception as e:
#         st.error(f"Error fetching data: {e}")
#         return pd.DataFrame()
#
# # Promote / Demote logic
# def promote_member(row_id):
#     try:
#         row_id = str(row_id)
#         response = supabase.table(TABLE_NAME).update({
#             "Panel": "executive member"
#         }).eq("id", row_id).execute()
#         if response.data and len(response.data) > 0:
#             st.success("🎉 Member promoted to Executive Member!")
#             time.sleep(1)
#             st.rerun()
#         else:
#             st.warning(f"⚠️ Promotion failed — no rows updated. ID: {row_id}")
#     except Exception as e:
#         st.error(f"❌ Failed to promote: {e}")
#
# def demote_member(row_id):
#     try:
#         row_id = str(row_id)
#         response = supabase.table(TABLE_NAME).update({
#             "Panel": "general member"
#         }).eq("id", row_id).execute()
#         if response.data and len(response.data) > 0:
#             st.success("👋 Member demoted to General Member.")
#             time.sleep(1)
#             st.rerun()
#         else:
#             st.warning(f"⚠️ Demotion failed — no rows updated. ID: {row_id}")
#     except Exception as e:
#         st.error(f"❌ Failed to demote: {e}")
#
# # Add new member
# def add_member(name, panel, department, designation, fb_id, linkedin_id):
#     try:
#         new_id = str(uuid.uuid4())
#         response = supabase.table(TABLE_NAME).insert({
#             "id": new_id,
#             "Name": name,
#             "Panel": panel,
#             "Department": department,
#             "Designation": designation,
#             "FB ID": fb_id,
#             "LinkedIn ID": linkedin_id
#         }).execute()
#
#         if response.data and len(response.data) > 0:
#             st.success("✅ New member added successfully!")
#             time.sleep(1)
#             st.rerun()
#         else:
#             st.warning("⚠️ Member insertion failed.")
#     except Exception as e:
#         st.error(f"❌ Failed to add member: {e}")
#
# # Load and validate data
# df = fetch_data()
#
# if "Panel" not in df.columns:
#     st.error("Missing 'Panel' column.")
#     st.stop()
#
# df["Panel"] = df["Panel"].astype(str).str.strip()
#
# # Tabs
# panel_labels = {
#     "Executive panel": "Executive Panel",
#     "Sub-executive panel": "Sub-Executive Panel",
#     "executive member": "Executive Member",
#     "general member": "General Member"
# }
#
# tabs = st.tabs(list(panel_labels.values()) + ["➕ Add Member"])
#
# # Existing panel tabs
# for tab, (raw_label, display_label) in zip(tabs[:-1], panel_labels.items()):
#     with tab:
#         panel_df = df[df["Panel"] == raw_label]
#
#         if panel_df.empty:
#             st.info(f"No members in {display_label}.")
#             continue
#
#         def is_all_zero(series):
#             return ((series.astype(str).str.strip() == "0") | (series == 0)).all()
#
#         filtered_df = panel_df.loc[:, ~panel_df.apply(is_all_zero)]
#
#         st.subheader(f"{display_label} Members")
#
#         if raw_label == "general member":
#             for _, row in filtered_df.iterrows():
#                 with st.container():
#                     st.markdown(
#                         f"""
#                         **Name:** {row.get('Name', 'N/A')}
#                         **Panel:** {row.get('Panel', 'N/A')}
#                         **FB ID:** {row.get('fb id', 'N/A')}
#                         **LinkedIn ID:** {row.get('linkedin id', 'N/A')}
#                         """
#                     )
#                     if st.button("🎯 Promote to Executive", key=f"promote_{row['id']}"):
#                         promote_member(row["id"])
#                     st.markdown("---")
#
#         elif raw_label == "executive member":
#             for _, row in filtered_df.iterrows():
#                 with st.container():
#                     st.markdown(
#                         f"""
#                         **Name:** {row.get('Name', 'N/A')}
#                         **Panel:** {row.get('Panel', 'N/A')}
#                         **FB ID:** {row.get('fb id', 'N/A')}
#                         **LinkedIn ID:** {row.get('linkedin id', 'N/A')}
#                         """
#                     )
#                     if st.button("↩️ Demote to General", key=f"demote_{row['id']}"):
#                         demote_member(row["id"])
#                     st.markdown("---")
#
# # Add Member Tab
# with tabs[-1]:
#     st.subheader("➕ Add New Member")
#
#     with st.form("add_member_form"):
#         name = st.text_input("Name")
#         panel = st.selectbox("Panel", ["general member", "executive member", "Executive panel", "Sub-executive panel"])
#         department = st.text_input("Department")
#         designation = st.text_input("Designation")
#         fb_id = st.text_input("Facebook ID")
#         linkedin_id = st.text_input("LinkedIn ID")
#
#         submitted = st.form_submit_button("Add Member")
#
#         if submitted:
#             if not name:
#                 st.warning("⚠️ Name is required.")
#             else:
#                 add_member(name, panel, department, designation, fb_id, linkedin_id)
#
#

# add member
# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
# import uuid
# import time
#
# # Supabase config
# SUPABASE_URL = "https://orjswswziiisbkvwnpye.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9yanN3c3d6aWlpc2JrdnducHllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjczNDQsImV4cCI6MjA2MzkwMzM0NH0.F2Oe53GzprWjiMYGvxMipplMwE2QeuKRRQI3Zsi7RAM"
# TABLE_NAME = "cc"
#
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# # Fetch existing data
# def fetch_data():
#     try:
#         response = supabase.table(TABLE_NAME).select("*").execute()
#         return pd.DataFrame(response.data)
#     except Exception as e:
#         st.error(f"Error fetching data: {e}")
#         return pd.DataFrame()
#
# # Promote / Demote logic
# def promote_member(row_id):
#     try:
#         row_id = str(row_id)
#         response = supabase.table(TABLE_NAME).update({
#             "Panel": "executive member"
#         }).eq("id", row_id).execute()
#         if response.data and len(response.data) > 0:
#             st.success("🎉 Member promoted to Executive Member!")
#             time.sleep(1)
#             st.rerun()
#         else:
#             st.warning(f"⚠️ Promotion failed — no rows updated. ID: {row_id}")
#     except Exception as e:
#         st.error(f"❌ Failed to promote: {e}")
#
# def demote_member(row_id):
#     try:
#         row_id = str(row_id)
#         response = supabase.table(TABLE_NAME).update({
#             "Panel": "general member"
#         }).eq("id", row_id).execute()
#         if response.data and len(response.data) > 0:
#             st.success("👋 Member demoted to General Member.")
#             time.sleep(1)
#             st.rerun()
#         else:
#             st.warning(f"⚠️ Demotion failed — no rows updated. ID: {row_id}")
#     except Exception as e:
#         st.error(f"❌ Failed to demote: {e}")
#
# # Add new member
# def add_member(name, panel, department, designation, fb_id, linkedin_id):
#     try:
#         new_id = str(uuid.uuid4())
#         response = supabase.table(TABLE_NAME).insert({
#             "id": new_id,
#             "Name": name,
#             "Panel": panel,
#             "Department": department,
#             "Designation": designation,
#             "fb id": fb_id,
#             "linkedin id": linkedin_id
#         }).execute()
#
#         if response.data and len(response.data) > 0:
#             st.success("✅ New member added successfully!")
#             time.sleep(1)
#             st.rerun()
#         else:
#             st.warning("⚠️ Member insertion failed.")
#     except Exception as e:
#         st.error(f"❌ Failed to add member: {e}")
#
#
# # Load and validate data
# df = fetch_data()
#
# if "Panel" not in df.columns:
#     st.error("Missing 'Panel' column.")
#     st.stop()
#
# df["Panel"] = df["Panel"].astype(str).str.strip()
#
# # Tabs
# panel_labels = {
#     "Executive panel": "Executive Panel",
#     "Sub-executive panel": "Sub-Executive Panel",
#     "executive member": "Executive Member",
#     "general member": "General Member"
# }
#
# tabs = st.tabs(list(panel_labels.values()) + ["➕ Add Member"])
#
# # Existing panel tabs
# for tab, (raw_label, display_label) in zip(tabs[:-1], panel_labels.items()):
#     with tab:
#         panel_df = df[df["Panel"] == raw_label]
#
#         if panel_df.empty:
#             st.info(f"No members in {display_label}.")
#             continue
#
#         def is_all_zero(series):
#             return ((series.astype(str).str.strip() == "0") | (series == 0)).all()
#
#         filtered_df = panel_df.loc[:, ~panel_df.apply(is_all_zero)]
#
#         st.subheader(f"{display_label} Members")
#
#         for _, row in filtered_df.iterrows():
#             with st.container():
#                 st.markdown(
#                     f"""
#                     **Name:** {row.get('Name', 'N/A')}
#                     **Panel:** {row.get('Panel', 'N/A')}
#                     **Department:** {row.get('Department', 'N/A')}
#                     **Designation:** {row.get('Designation', 'N/A')}
#                     **FB ID:** {row.get('FB ID', 'N/A')}
#                     **LinkedIn ID:** {row.get('LinkedIn ID', 'N/A')}
#                     """
#                 )
#                 if raw_label == "general member":
#                     if st.button("🎯 Promote to Executive", key=f"promote_{row['id']}"):
#                         promote_member(row["id"])
#                 elif raw_label == "executive member":
#                     if st.button("↩️ Demote to General", key=f"demote_{row['id']}"):
#                         demote_member(row["id"])
#                 st.markdown("---")
#
# # Add Member Tab
# with tabs[-1]:
#     st.subheader("➕ Add New Member")
#
#     with st.form("add_member_form"):
#         name = st.text_input("Name")
#         panel = st.selectbox("Panel", list(panel_labels.keys()))
#         department = st.text_input("Department")
#         designation = st.text_input("Designation")
#         fb_id = st.text_input("Facebook ID")
#         linkedin_id = st.text_input("LinkedIn ID")
#
#         submitted = st.form_submit_button("Add Member")
#
#         if submitted:
#             if not name:
#                 st.warning("⚠️ Name is required.")
#             else:
#                 add_member(name, panel, department, designation, fb_id, linkedin_id)



# senior exec added
# import streamlit as st
# import pandas as pd
# from supabase import create_client, Client
# import uuid
# import time
#
# # Supabase config
# SUPABASE_URL = "https://orjswswziiisbkvwnpye.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9yanN3c3d6aWlpc2JrdnducHllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjczNDQsImV4cCI6MjA2MzkwMzM0NH0.F2Oe53GzprWjiMYGvxMipplMwE2QeuKRRQI3Zsi7RAM"
# TABLE_NAME = "cc"
#
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# # Fetch existing data
# def fetch_data():
#     try:
#         response = supabase.table(TABLE_NAME).select("*").execute()
#         return pd.DataFrame(response.data)
#     except Exception as e:
#         st.error(f"Error fetching data: {e}")
#         return pd.DataFrame()
#
# # Promote / Demote logic
# def promote_member(row_id):
#     try:
#         response = supabase.table(TABLE_NAME).update({
#             "Panel": "executive member"
#         }).eq("id", str(row_id)).execute()
#         if response.data:
#             st.success("🎉 Member promoted to Executive Member!")
#             time.sleep(1)
#             st.rerun()
#     except Exception as e:
#         st.error(f"❌ Failed to promote: {e}")
#
# def demote_member(row_id):
#     try:
#         response = supabase.table(TABLE_NAME).update({
#             "Panel": "general member"
#         }).eq("id", str(row_id)).execute()
#         if response.data:
#             st.success("👋 Member demoted to General Member.")
#             time.sleep(1)
#             st.rerun()
#     except Exception as e:
#         st.error(f"❌ Failed to demote: {e}")
#
# # Add new member
# def add_member(name, panel, department, designation, fb_id, linkedin_id, photo_url):
#     try:
#         new_id = str(uuid.uuid4())
#         response = supabase.table(TABLE_NAME).insert({
#             "id": new_id,
#             "Name": name,
#             "Panel": panel,
#             "Department": department,
#             "Designation": designation,
#             "fb id": fb_id,
#             "linkedin id": linkedin_id,
#             "photo": photo_url  # <-- Include photo
#         }).execute()
#         if response.data:
#             st.success("✅ New member added successfully!")
#             time.sleep(1)
#             st.rerun()
#     except Exception as e:
#         st.error(f"❌ Failed to add member: {e}")
#
#
# # Delete member by ID + show img + add img
# def delete_member(row_id):
#     try:
#         response = supabase.table(TABLE_NAME).delete().eq("id", str(row_id)).execute()
#         if response.data:
#             st.success("🗑️ Member deleted successfully!")
#             time.sleep(1)
#             st.rerun()
#     except Exception as e:
#         st.error(f"❌ Failed to delete member: {e}")
#
# # Load data
# df = fetch_data()
# if "Panel" not in df.columns:
#     st.error("Missing 'Panel' column.")
#     st.stop()
#
# df["Panel"] = df["Panel"].astype(str).str.strip()
#
# # Panel Labels
# panel_labels = {
#     "Executive panel": "Executive Panel",
#     "Sub-executive panel": "Sub-Executive Panel",
#     "executive member": "Executive Member",
#     "senior executive": "Senior Executive",  # ✅ New entry
#     "general member": "General Member",
# }
#
#
# tabs = st.tabs(list(panel_labels.values()) + ["➕ Add Member", "🗑️ Delete Member"])
#
# # View Members Tabs
# for tab, (raw_label, display_label) in zip(tabs[:-2], panel_labels.items()):
#     with tab:
#         panel_df = df[df["Panel"] == raw_label]
#         if panel_df.empty:
#             st.info(f"No members in {display_label}.")
#             continue
#
#         def is_all_zero(series):
#             return ((series.astype(str).str.strip() == "0") | (series == 0)).all()
#
#         filtered_df = panel_df.loc[:, ~panel_df.apply(is_all_zero)]
#
#         st.subheader(f"{display_label} Members")
#         for _, row in filtered_df.iterrows():
#             with st.container():
#                 cols = st.columns([1, 3])
#                 with cols[0]:
#                     photo_url = row.get("photo", "")
#                     if photo_url and photo_url.strip().lower() != "n/a":
#                         st.image(photo_url, width=100)
#                     else:
#                         st.markdown("🚫 No Photo")
#
#                 with cols[1]:
#                     st.markdown(
#                         f"""
#                         **Name:** {row.get('Name', 'N/A')}
#                         **Panel:** {row.get('Panel', 'N/A')}
#                         **Department:** {row.get('Department', 'N/A')}
#                         **Designation:** {row.get('Designation', 'N/A')}
#                         **FB ID:** {row.get('fb id', 'N/A')}
#                         **LinkedIn ID:** {row.get('linkedin id', 'N/A')}
#                         """
#                     )
#
#                 if raw_label == "general member":
#                     if st.button("🎯 Promote to Executive", key=f"promote_{row['id']}"):
#                         promote_member(row["id"])
#                 elif raw_label == "executive member":
#                     if st.button("↩️ Demote to General", key=f"demote_{row['id']}"):
#                         demote_member(row["id"])
#                 st.markdown("---")
#
# # Add Member Tab
# # Add Member Tab
# with tabs[-2]:
#     st.subheader("➕ Add New Member")
#     with st.form("add_member_form"):
#         name = st.text_input("Name")
#         panel = st.selectbox("Panel", list(panel_labels.keys()))
#         department = st.text_input("Department")
#         designation = st.text_input("Designation")
#         fb_id = st.text_input("Facebook ID")
#         linkedin_id = st.text_input("LinkedIn ID")
#         photo_url = st.text_input("Photo URL (optional)")
#
#         submitted = st.form_submit_button("Add Member")
#         if submitted:
#             if not name:
#                 st.warning("⚠️ Name is required.")
#             else:
#                 add_member(name, panel, department, designation, fb_id, linkedin_id, photo_url)
#
#
# # Delete Member Tab
# with tabs[-1]:
#     st.subheader("🗑️ Delete Member")
#     search_name = st.text_input("Search by Name")
#     if search_name:
#         filtered = df[df["Name"].str.contains(search_name, case=False, na=False)]
#
#         if filtered.empty:
#             st.info("No matching members found.")
#         else:
#             for _, row in filtered.iterrows():
#                 with st.container():
#                     cols = st.columns([1, 3])
#                     with cols[0]:
#                         photo_url = row.get("photo", "")
#                         if photo_url and photo_url.strip().lower() != "n/a":
#                             st.image(photo_url, width=100)
#                         else:
#                             st.markdown("🚫 No Photo")
#
#                     with cols[1]:
#                         st.markdown(
#                             f"""
#                             **Name:** {row.get('Name', 'N/A')}
#                             **Panel:** {row.get('Panel', 'N/A')}
#                             **Department:** {row.get('Department', 'N/A')}
#                             **Designation:** {row.get('Designation', 'N/A')}
#                             **FB ID:** {row.get('fb id', 'N/A')}
#                             **LinkedIn ID:** {row.get('linkedin id', 'N/A')}
#                             """
#                         )
#
#                     if st.button("🗑️ Delete", key=f"delete_{row['id']}"):
#                         delete_member(row["id"])
#
#


# update tab
import streamlit as st
import pandas as pd
from supabase import create_client, Client
import uuid
import time

# Supabase config
SUPABASE_URL = "https://orjswswziiisbkvwnpye.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9yanN3c3d6aWlpc2JrdnducHllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzMjczNDQsImV4cCI6MjA2MzkwMzM0NH0.F2Oe53GzprWjiMYGvxMipplMwE2QeuKRRQI3Zsi7RAM"
  # Replace with your actual key
TABLE_NAME = "cc"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Fetch data
def fetch_data():
    try:
        response = supabase.table(TABLE_NAME).select("*").execute()
        return pd.DataFrame(response.data)
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()

# Add member
def add_member(name, panel, department, designation, fb_id, linkedin_id, photo_url):
    try:
        new_id = str(uuid.uuid4())
        response = supabase.table(TABLE_NAME).insert({
            "id": new_id,
            "Name": name,
            "Panel": panel,
            "Department": department,
            "Designation": designation,
            "fb id": fb_id,
            "linkedin id": linkedin_id,
            "photo": photo_url
        }).execute()
        if response.data:
            st.success("✅ New member added successfully!")
            time.sleep(1)
            st.rerun()
    except Exception as e:
        st.error(f"❌ Failed to add member: {e}")

# Delete member
def delete_member(row_id):
    try:
        response = supabase.table(TABLE_NAME).delete().eq("id", str(row_id)).execute()
        if response.data:
            st.success("🗑️ Member deleted successfully!")
            time.sleep(1)
            st.rerun()
    except Exception as e:
        st.error(f"❌ Failed to delete member: {e}")

# Promote / Demote
def promote_member(row_id):
    try:
        response = supabase.table(TABLE_NAME).update({
            "Panel": "executive member"
        }).eq("id", str(row_id)).execute()
        if response.data:
            st.success("🎉 Member promoted to Executive Member!")
            time.sleep(1)
            st.rerun()
    except Exception as e:
        st.error(f"❌ Failed to promote: {e}")

def demote_member(row_id):
    try:
        response = supabase.table(TABLE_NAME).update({
            "Panel": "general member"
        }).eq("id", str(row_id)).execute()
        if response.data:
            st.success("👋 Member demoted to General Member.")
            time.sleep(1)
            st.rerun()
    except Exception as e:
        st.error(f"❌ Failed to demote: {e}")

# Update member
def update_member(row_id, name, panel, department, designation, fb_id, linkedin_id, photo_url):
    try:
        response = supabase.table(TABLE_NAME).update({
            "Name": name,
            "Panel": panel,
            "Department": department,
            "Designation": designation,
            "fb id": fb_id,
            "linkedin id": linkedin_id,
            "photo": photo_url
        }).eq("id", str(row_id)).execute()
        if response.data:
            st.success("✅ Member updated successfully!")
            time.sleep(1)
            st.rerun()
    except Exception as e:
        st.error(f"❌ Failed to update member: {e}")

# Main
df = fetch_data()
if "Panel" not in df.columns:
    st.error("Missing 'Panel' column.")
    st.stop()

df["Panel"] = df["Panel"].astype(str).str.strip()

panel_labels = {
    "Executive panel": "Executive Panel",
    "Sub-executive panel": "Sub-Executive Panel",
    "executive member": "Executive Member",
    "senior executive": "Senior Executive",
    "general member": "General Member",
}

tabs = st.tabs(list(panel_labels.values()) + ["➕ Add Member", "✏️ Update Member", "🗑️ Delete Member"])

# View Members
for tab, (raw_label, display_label) in zip(tabs[:-3], panel_labels.items()):
    with tab:
        panel_df = df[df["Panel"] == raw_label]
        if panel_df.empty:
            st.info(f"No members in {display_label}.")
            continue

        def is_all_zero(series):
            return ((series.astype(str).str.strip() == "0") | (series == 0)).all()

        filtered_df = panel_df.loc[:, ~panel_df.apply(is_all_zero)]

        st.subheader(f"{display_label} Members")
        for _, row in filtered_df.iterrows():
            with st.container():
                cols = st.columns([1, 3])
                with cols[0]:
                    photo_url = row.get("photo", "")
                    if photo_url and photo_url.strip().lower() != "n/a":
                        st.image(photo_url, width=100)
                    else:
                        st.markdown("🚫 No Photo")

                with cols[1]:
                    st.markdown(
                        f"""
                        **Name:** {row.get('Name', 'N/A')}  
                        **Panel:** {row.get('Panel', 'N/A')}  
                        **Department:** {row.get('Department', 'N/A')}  
                        **Designation:** {row.get('Designation', 'N/A')}  
                        **FB ID:** {row.get('fb id', 'N/A')}  
                        **LinkedIn ID:** {row.get('linkedin id', 'N/A')}
                        """
                    )

                if raw_label == "general member":
                    if st.button("🎯 Promote to Executive", key=f"promote_{row['id']}"):
                        promote_member(row["id"])
                elif raw_label == "executive member":
                    if st.button("↩️ Demote to General", key=f"demote_{row['id']}"):
                        demote_member(row["id"])
                st.markdown("---")

# Add Member
with tabs[-3]:
    st.subheader("➕ Add New Member")
    with st.form("add_member_form"):
        name = st.text_input("Name")
        panel = st.selectbox("Panel", list(panel_labels.keys()))
        department = st.text_input("Department")
        designation = st.text_input("Designation")
        fb_id = st.text_input("Facebook ID")
        linkedin_id = st.text_input("LinkedIn ID")
        photo_url = st.text_input("Photo URL (optional)")

        submitted = st.form_submit_button("Add Member")
        if submitted:
            if not name:
                st.warning("⚠️ Name is required.")
            else:
                add_member(name, panel, department, designation, fb_id, linkedin_id, photo_url)

# Update Member
with tabs[-2]:
    st.subheader("✏️ Update Member")
    search_name = st.text_input("Search member to update by name")
    if search_name:
        filtered = df[df["Name"].str.contains(search_name, case=False, na=False)]
        if filtered.empty:
            st.info("No matching members found.")
        else:
            for _, row in filtered.iterrows():
                with st.form(f"update_form_{row['id']}"):
                    st.markdown(f"#### Updating: **{row['Name']}**")
                    name = st.text_input("Name", value=row["Name"])
                    panel = st.selectbox("Panel", list(panel_labels.keys()), index=list(panel_labels.keys()).index(row["Panel"]))
                    department = st.text_input("Department", value=row.get("Department", ""))
                    designation = st.text_input("Designation", value=row.get("Designation", ""))
                    fb_id = st.text_input("Facebook ID", value=row.get("fb id", ""))
                    linkedin_id = st.text_input("LinkedIn ID", value=row.get("linkedin id", ""))
                    photo_url = st.text_input("Photo URL", value=row.get("photo", ""))

                    submitted = st.form_submit_button("Update Member")
                    if submitted:
                        update_member(row["id"], name, panel, department, designation, fb_id, linkedin_id, photo_url)

# Delete Member
with tabs[-1]:
    st.subheader("🗑️ Delete Member")
    search_name = st.text_input("Search by Name")
    if search_name:
        filtered = df[df["Name"].str.contains(search_name, case=False, na=False)]

        if filtered.empty:
            st.info("No matching members found.")
        else:
            for _, row in filtered.iterrows():
                with st.container():
                    cols = st.columns([1, 3])
                    with cols[0]:
                        photo_url = row.get("photo", "")
                        if photo_url and photo_url.strip().lower() != "n/a":
                            st.image(photo_url, width=100)
                        else:
                            st.markdown("🚫 No Photo")

                    with cols[1]:
                        st.markdown(
                            f"""
                            **Name:** {row.get('Name', 'N/A')}  
                            **Panel:** {row.get('Panel', 'N/A')}  
                            **Department:** {row.get('Department', 'N/A')}  
                            **Designation:** {row.get('Designation', 'N/A')}  
                            **FB ID:** {row.get('fb id', 'N/A')}  
                            **LinkedIn ID:** {row.get('linkedin id', 'N/A')}
                            """
                        )

                    if st.button("🗑️ Delete", key=f"delete_{row['id']}"):
                        delete_member(row["id"])
