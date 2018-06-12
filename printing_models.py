#출력할 디자인으로 시작합니다.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#남은것이 없을 때까지 각 디자인의 출력을 시뮬레이트 합니다.
#출력한 각 디자인을 completed_models 로 옮깁니다.
while unprinted_designs:
    current_design = unprinted_designs.pop()

    print("Printing model: " + current_design)
    completed_models.append(current_design)

print("\nthe following models have been printed:")
for completed_models in completed_models:
    print(completed_models)



def print_models(unprinted_designs, completed_models):
    """
    남은것이 없을 때까지 각 디자인의 출력을 시뮬레이트합니다.
    출력한 각 디자인을 completed_models로 옮깁니다.
    
    Args:
        unprinted_designs (TYPE): Description
        completed_models (TYPE): Description
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_printed_models(completed_models):
    """출력이 끝난 모델 모두 표시
    
    Args:
        completed_models (TYPE): Description
    """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

umprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_printed_models(completed_models)


        
