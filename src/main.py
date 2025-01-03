from utils.terminal_display import (
    clear_terminal,
    press_any_key,
    ask_yes_no_question,
    display_menu,
)

from utils.formatted_file_io import (
    check_file_existence,
    get_theta_from_csv,
    save_theta_to_csv,
    get_data_from_csv,
)


from constants.path import DATA_FILE_PATH, THETA_FILE_PATH


def main():
    clear_terminal()
    check_file_existence(DATA_FILE_PATH)
    check_file_existence(THETA_FILE_PATH)
    theta = get_theta_from_csv()
    print(f"Theta values: {theta}")
    save_theta_to_csv((0.1123, 0.2123))
    theta = get_theta_from_csv()
    print(f"Theta values: {theta}")
    data = get_data_from_csv()
    print(f"Data: {data}")


if __name__ == "__main__":
    main()
