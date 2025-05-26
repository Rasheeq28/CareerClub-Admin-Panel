# # import gspread
# # from google.oauth2.service_account import Credentials
# #
# # scopes = [
# # "https://www.googleapis.com/auth/spreadsheets"
# # ]
# #
# # creds = Credentials.from_service_account_file("credentials.json", scopes = scopes)
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
# # creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
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
# # creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
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
# # creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
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
# creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
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


import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import requests
import threading
import websocket
import time

# Setup Google Sheets API client
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1QEi0D0M7Ib39W97DeaB9v69eGeLlqknkYkPoqbgolqs"
sheet = client.open_by_key(sheet_id)
worksheet = sheet.sheet1


# Load data from Google Sheets
def load_data():
    records = worksheet.get_all_records()
    df = pd.DataFrame(records)
    df.columns = df.columns.str.strip()
    df["Panel"] = df["Panel"].str.strip()
    return df


# Promote a user and notify backend
def promote_to_executive(name):
    cell = worksheet.find(name)
    if cell:
        panel_cell = worksheet.cell(cell.row, cell.col + 1)  # Assuming Panel is next column
        worksheet.update_cell(panel_cell.row, panel_cell.col, "Executive member")

        try:
            requests.post("http://localhost:8000/notify")
        except Exception as e:
            st.error(f"Failed to notify backend: {e}")

        st.success(f"{name} has been promoted to Executive Member!")


# WebSocket listener callback function
def on_message(ws, message):
    if message == "update":
        st.session_state["reload_data"] = True


def on_error(ws, error):
    print(f"WebSocket error: {error}")


def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")


def on_open(ws):
    print("WebSocket connection opened")


def ws_listen():
    ws = websocket.WebSocketApp("ws://localhost:8000/ws",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                on_open=on_open)
    ws.run_forever()


def main():
    st.set_page_config(page_title="Panel Manager", layout="wide")

    # Start WebSocket listener thread once
    if "ws_thread" not in st.session_state:
        ws_thread = threading.Thread(target=ws_listen, daemon=True)
        ws_thread.start()
        st.session_state["ws_thread"] = ws_thread

    # Reload data if flagged or first time
    if "data" not in st.session_state or st.session_state.get("reload_data", False):
        st.session_state["data"] = load_data()
        st.session_state["reload_data"] = False

    df = st.session_state["data"]
    unique_panels = ["General member", "Executive member", "Sub-executive panel", "Executive panel"]

    tabs = st.tabs(unique_panels)

    for i, panel in enumerate(unique_panels):
        with tabs[i]:
            filtered_df = df[df["Panel"].str.lower() == panel.lower()]
            st.subheader(f"{panel} Members")

            if filtered_df.empty:
                st.warning(f"No members found in '{panel}' panel.")
            else:
                # Drop columns where all values are 0
                filtered_df_nonzero = filtered_df.loc[:, (filtered_df != 0).any(axis=0)]

                st.dataframe(filtered_df_nonzero)

                # Promote button in General member tab
                if panel == "General member":
                    names = filtered_df_nonzero["Name"].tolist()
                    selected_name = st.selectbox("Select a general member to promote", names)
                    if st.button("Promote to Executive Member"):
                        promote_to_executive(selected_name)

    # Manual refresh button in case auto update misses
    if st.button("Refresh Data"):
        st.session_state["reload_data"] = True
        st.success("Data reload flagged! Please refresh the page manually if needed.")


if __name__ == "__main__":
    main()
