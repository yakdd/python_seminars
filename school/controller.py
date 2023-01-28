import view
import demo
import mod_import
import mod_export
import score


def start():
    hr = '\n-------------------------------\n'
    print(hr)
    dict_Units = {}

    while True:
        action = view.select_action()
        if action == 0:
            break

        if action == 1:
            # добавить студента
            mod_import.import_unit(dict_Units)
            print(hr)

        if action == 2:
            # добавить предмет
            mod_import.add_discipl(dict_Units)
            print(hr)

        if action == 3:
            # добавить оценки ученику по предмету
            score.add_score(dict_Units)
            print(hr)

        if action == 4:
            # показать список учеников
            mod_export.unit_list(dict_Units)
            print(hr)

        if action == 5:
            # показать лист оценок ученика
            mod_export.rating_list(dict_Units)
            print(hr)

        if action == 6:
            # показать среднюю оценку ученика по предметам
            score.average_rating(dict_Units)
            print(hr)

        if action == 7:
            # показать средний балл по школе по конкретному предмету
            score.average_mark(dict_Units)
            print(hr)

        if action == 8:
            # показать медалистов
            print('Медалисты:')
            medalists = score.medalists_show(dict_Units)
            mod_export.output(medalists)
            print(hr)

        if action == 9:
            # показать все данные
            mod_export.output(dict_Units)
            print(hr)

        if action == 77:
            # экспортировать данные в файл
            mod_export.export_journal(dict_Units)
            break

        if action == 88:
            # импортировать данные из файла
            import_dict_Units = mod_import.import_journal()
            if import_dict_Units:
                dict_Units = import_dict_Units
                mod_export.output(dict_Units)
            print(hr)

        if action == 99:
            # создать демо-версию журнала
            demo.demo_dict(dict_Units)
            mod_export.output(dict_Units)
            print(hr)
