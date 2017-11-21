import yaml

global generic_data
generic_data = yaml.load(open('configuration/config.yml'))

def before_all(context):
    print("_____________Iniciar_Todos_los_Feature_______________")
    context.host          = generic_data['host']
    context.rootPath      = generic_data['rootPath']
    context.token         = generic_data['token']
    #print(context.token)

def after_feature(context, feature):
    if 'smoke' in feature.tags:
        print("__________Fin_Feature______________")

def before_feature(context, feature):
    if 'smoke' in feature.tags:
        print("___________Inicio_Feature_____________")
'''
def before_scenario(context, scenario):
    if 'getuser' in scenario.tags:
        print("_________Inicio_Scennario___________")

def before_step(context, step):
    print("STEP: ", step.name)
    print("KEYWORD: ", step.keyword)
    print("STATUS: ", step.status)
'''