import yaml

global generic_data
generic_data = yaml.load(open('configuration/config.yml'))

def before_all(context):
    print("**********Before All************")
    context.host   = generic_data['host']
    context.rootPath = generic_data['rootPath']
    context.token   = generic_data['token']
    context.authorization = generic_data['authorization']
    context.user = generic_data['user']
    print(context.host, context.rootPath, context.token, context.user)

def after_feature(context, feature):
    if 'userFeature' in feature.tags:
        print("///////feature TEST 1 ALL///////")

def before_feature(context, feature):
    if 'userFeature' in feature.tags:
        print("///////feature TEST 1 ALL///////")

def before_scenario(context, scenario):
    if 'getuser' in scenario.tags:
        print("///////Scenario tag///////")

def before_step(context, step):
    print("STEP", step.name)
    print("KEYWORD", step.keyword)
    print("STATUS", step.status)
