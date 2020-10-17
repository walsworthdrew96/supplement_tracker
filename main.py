import datetime
import time
from supplement import Dose, Supplement, Nutrient
import os
import operator
import copy
from calendar import monthrange
import shelve
import sleep


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


if __name__ == "__main__":
    supplements = {"biotin":
                       Supplement("Biotin (B7)", [Nutrient("Biotin (B7)", "Biotin", 1000, "μg")]),
                   "methyl_b_complete":
                       Supplement("Methyl B Complete",
                                  [Nutrient("TMG", "Trimethylglycine", 650, "mg"),
                                   Nutrient("Riboflavin (B2)", "Riboflavin", 25, "mg"),
                                   Nutrient("Pyridoxine (B6)", "Pyridoxine", 15, "mg"),
                                   Nutrient("Methylcobalamin (B12)", "Methylcobalamin", 1000, "μg"),
                                   Nutrient("5MTHF (Active B9)", "5-methyltetrahydrofolate", 2000,
                                            "μg")
                                   ]),
                   "magnesium":
                       Supplement("Magnesium",
                                  [Nutrient("Calories", "Calories", 30, ""),
                                   Nutrient("Magnesium", "Magnesium Citrate/Oxide", 165, "mg"),
                                   ]),
                   }
    doses = [
        Dose(datetime.datetime(day=13, month=10, year=2020), supplements["biotin"], 2),
        Dose(datetime.datetime(day=14, month=10, year=2020), supplements["biotin"], 2),
        Dose(datetime.datetime(day=15, month=10, year=2020), supplements["biotin"], 2),
        Dose(datetime.datetime(minute=40, hour=17, day=15, month=10, year=2020), supplements["methyl_b_complete"], 1),
        Dose(datetime.datetime(day=15, month=10, year=2020), supplements["magnesium"], 2),
        Dose(datetime.datetime(minute=0, hour=16, day=16, month=10, year=2020), supplements["magnesium"], 2),
    ]
    #     while True:
    #         user_choice = input("""Choose an option:
    #     1. Display Nutrients for Month
    #     2. Display All Supplements
    #     3. Search for a supplement
    #     4. Quit
    # Your choice: """)
    #         clear_console()
    #         if user_choice == "1":
    #             for dose in doses:
    #                 print(dose)
    #         if user_choice == "2":
    #             for v in supplements.values():
    #                 print(v)
    #         if user_choice == "3":
    #             search_query = input("Supplement Search: ")
    #             search_results = []
    #             for v in supplements.values():
    #                 for word in search_query.strip().lower().split():
    #                     if word in v.name.lower():
    #                         search_results.append(v)
    #                         break
    #             result_counter = 1
    #             for result in search_results:
    #                 print(f"#{result_counter}: {result}")
    #                 result_counter += 1
    #         if user_choice == "4":
    #             break

    # get nutrients for each day
    nutrient_headers = [nutrient for supp in supplements.values() for nutrient in supp.nutrients]
    nutrient_headers.sort(key=operator.attrgetter('chemical_name'))
    nutrient_headers = list(enumerate(nutrient_headers))
    print('nutrient_headers:', nutrient_headers)
    nutrients_row = [0 for nutrient in nutrient_headers]

    dose_chart = [(datetime.date(day=1 + x, month=10, year=2020), copy.deepcopy(nutrients_row)) for x in
                  range(monthrange(2020, 10)[1])]
    # for dose_row in dose_chart:
    #     print(dose_row)

    for dose in doses:
        for nutrient in dose.supplement.nutrients:
            for header in nutrient_headers:
                # print('header[1]:', header[1])
                # print('nutrient.chemical_name:', nutrient.chemical_name)
                print(f"{header[1].chemical_name} == {nutrient.chemical_name} = {header[1] == nutrient.chemical_name}")
                if header[1].chemical_name == nutrient.chemical_name:
                    dose_chart[dose.date.day - 1][header[0]] = f"{nutrient.amount * dose.servings}{nutrient.unit}"

    for dose_row in dose_chart:
        # print(dose_row)
        pass

    # add database support later
