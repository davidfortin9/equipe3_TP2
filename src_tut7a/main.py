
import sys
from qcPortail import get_params_from_cli, get_params_from_user, show_solution, prompt_menu

from qcPlanner.qcSync.QcSync import QcSync


def get_route(params):
    objSync = QcSync(params=params)
    solution = objSync.solveProblem()
    show_solution(solution)


if __name__ == "__main__":

    print("\n"+ 50*"*")
    print("*****\t Outil de planification des routes \t"+5*'*')
    print("*************\t Quantum Courrier \t"+5*'*')
    print(50*"*"+"\n")
    if len(sys.argv) < 2:
        change, params = prompt_menu()
        if change == 1:
            params = get_params_from_user()
            if params is None:
                change, params = prompt_menu()
    else:
        params = get_params_from_cli()
    get_route(params)
