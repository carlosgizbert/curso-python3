def get_day_week(day):
    days = {
        1: "Domingo",
        2: "Segunda",
        3: "Terça",
        4: "Quarta",
        5: "Quinta",
        6: "Sexta",
        7: "Sábado",
    }

    return days.get(day, "** inválido **")

if __name__ == "__main__":
    for dia in range(0, 9):
        
        if get_day_week(dia) == 'Sábado' or get_day_week(dia) == 'Domingo':
            print(f"{dia}: Final de semana")
            continue
        else:
            print(f"{dia}: {get_day_week(dia)}")
