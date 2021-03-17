import streamlit as st


def main():
    check = st.sidebar.radio("Navigation", ["Files", "Folder"])
    if check == 'Files':
        path_ = st.file_uploader("Browser Files", accept_multiple_files=True, type=["png", "jpg", "jpeg"])
        # create_dataset_files(path_)
    else:
        path_ = st.text_input("Browser PATH\n")
        # create_dataset_folder(path_)




if __name__ == '__main__':
    main()
