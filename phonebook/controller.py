import view
import initialization
import import_mod
import export_mod
import sorting


def start():
    initialization.new_phonebook()
    while True:
        action = view.select_action()
        if action == 1:
            import_mod.input_person()
        elif action == 2:
            export_mod.output_info()
        elif action == 3:
            sorting.sorting_phonebook(2)
        elif action == 4:
            sorting.sorting_phonebook(0)
        elif action == 5:
            export_mod.output_fio()
        elif action == 0:
            break
