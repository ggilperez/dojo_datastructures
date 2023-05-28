"""
Create a menu to ask information about csv data
"""

import csv
import os
import sys
from pathlib import Path

cwd = Path(__file__).parent
csv_filename = "data.csv"
csv_path = cwd / csv_filename
reports_path = cwd / "reports"


def not_implemented():
    raise Exception("NOT IMPLEMENTED")


def load_data():
    with open(csv_path) as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def get_student_by_city(data):
    city = input("Inserte la ciudad deseada: ")
    return [student for student in data if student["ciudad"] == city]


MENU = [
    {
        "method": get_student_by_city,
        "text": "Obtener todos los estudiantes que pertenezcan a una ciudad dada."
    },
    {
        "method": not_implemented,
        "text": "Obtener todos los estudiantes que vivan en un país dado."
    },
    {
        "method": not_implemented,
        "text": "Obtener todos los estudiantes que estén dentro del rango de edades dado."
    },
    {
        "method": not_implemented,
        "text": "Obtener todas las ciudades de residencia de los estudiantes."
    },
    {
        "method": not_implemented,
        "text": "Identificar la edad promedio por carrera."
    },
    {
        "method": not_implemented,
        "text": "Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad."
    },
    {
        "method": not_implemented,
        "text": "Agrupa los estudiantes en diferentes rangos de edad (18-25, 26-35, mayores de 35)."
    },
    {
        "method": not_implemented,
        "text": "Identifica la ciudad que tienen la mayor variedad de carreras universitarias entre los estudiantes."
    },
    {
        "method": sys.exit,
        "text": "Salir."
    }
]


def show_menu():
    for i, row in enumerate(MENU, start=1):
        print(f'{i}. {row["text"]}')


def select_menu_option():
    option = -1
    while len(MENU) < option or option <= 0:
        try:
            option = int(input("Selecciona una opción: "))
        except ValueError:
            pass  # not a valid number, try again

    return MENU[option - 1]


def show_results(results):
    if isinstance(results, list):
        for row in results:
            print(row)


def create_report(results, selected_option):
    report_filename = f'{selected_option["method"].__name__}.csv'
    report_filepath = reports_path / report_filename

    if not reports_path.exists():
        os.makedirs(reports_path)

    with open(report_filepath, "w+") as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    csv_data = load_data()
    show_menu()
    selected_option = select_menu_option()
    result = selected_option["method"](csv_data)
    create_report(result, selected_option)
